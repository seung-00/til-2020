# LSTM을 이용한 텍스트 생성

[Eddie 님의 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)을 정리한 내용



## 전처리

```python
import pandas as pd
from string import punctuation
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from tensorflow.keras.utils import to_categorical
```

```python
df=pd.read_csv('ArticlesApril2018.csv 파일의 경로')
df.head()
```

* Null 값을 체크한다

  ```python
  df['headline'].isnull().values.any()
  # False
  ```

```python
headline = [] # 리스트 선언
headline.extend(list(df.headline.values)) # 헤드라인의 값들을 리스트로 저장
headline[:5] # 상위 5개만 출력
```

```python
['Former N.F.L. Cheerleaders’ Settlement Offer: $1 and a Meeting With Goodell',
 'E.P.A. to Unveil a New Rule. Its Effect: Less Science in Policymaking.',
 'The New Noma, Explained',
 'Unknown',
 'Unknown']
```

* 헤드 값을 체크했을 때 Unknown 이라는 노이즈가 보임. 제거해주자.

  ```python
  print('총 샘플의 개수 : {}'.format(len(headline)) # 현재 샘플의 개수
  # 총 샘플의 개수 : 1324
  ```

  ```python
  headline = [n for n in headline if n != "Unknown"] # Unknown 값을 가진 샘플 제거
  print('노이즈값 제거 후 샘플의 개수 : {}'.format(len(headline)) # 제거 후 샘플의 개수
  # 노이즈값 제거 후 샘플의 개수 : 1214
  ```

* 구두점 제거와 소문자

  ```python
  def repreprocessing(s):
      s=s.encode("utf8").decode("ascii",'ignore')
      return ''.join(c for c in s if c not in punctuation).lower() # 구두점 제거와 동시에 소문자화
  
  text = [repreprocessing(x) for x in headline]
  text[:5]
  ```

  ```python
  ['former nfl cheerleaders settlement offer 1 and a meeting with goodell',
   'epa to unveil a new rule its effect less science in policymaking',
   'the new noma explained',
   'how a bag of texas dirt  became a times tradition',
   'is school a place for selfexpression']
  ```

* 토크나이징

  ```python
  t = Tokenizer()
  vocab_size = len(t.word_index) + 1
  print('단어 집합의 크기 : %d' % vocab_size)
  # 단어 집합의 크기 : 3494
  ```

* 정수 인코딩

  ```python
  sequences = list()
  
  for line in text: # 1,214 개의 샘플에 대해서 샘플을 1개씩 가져온다.
      encoded = t.texts_to_sequences([line])[0] # 각 샘플에 대한 정수 인코딩
      for i in range(1, len(encoded)):
          sequence = encoded[:i+1]
          sequences.append(sequence)
  
  sequences[:11] # 11개의 샘플 출력
  ```

  ```python
  [[99, 269], # former nfl
   [99, 269, 371], # former nfl cheerleaders
   [99, 269, 371, 1115], # former nfl cheerleaders settlement
   [99, 269, 371, 1115, 582], # former nfl cheerleaders settlement offer
   [99, 269, 371, 1115, 582, 52], # 'former nfl cheerleaders settlement offer 1
   [99, 269, 371, 1115, 582, 52, 7], # former nfl cheerleaders settlement offer 1 and
   [99, 269, 371, 1115, 582, 52, 7, 2], # ... 이하 생략 ...
   [99, 269, 371, 1115, 582, 52, 7, 2, 372],
   [99, 269, 371, 1115, 582, 52, 7, 2, 372, 10],
   [99, 269, 371, 1115, 582, 52, 7, 2, 372, 10, 1116], # 모든 단어가 사용된 완전한 첫번째 문장
   # 바로 위의 줄 : former nfl cheerleaders settlement offer 1 and a meeting with goodell
   [100, 3]] # epa to에 해당되며 두번째 문장이 시작됨.
  ```

* index_to_word 딕셔너리를 만듬(정수, 단어 매핑)

  ```python
  index_to_word={}
  for key, value in t.word_index.items(): # 인덱스를 단어로 바꾸기 위해 index_to_word를 생성
      index_to_word[value] = key
  
  print('빈도수 상위 582번 단어 : {}'.format(index_to_word[582]))
  ```

  ```python
  빈도수 상위 582번 단어 : offer
  ```

* 패딩 전에 샘플 최대 길이 확인

  ```python
  max_len=max(len(l) for l in sequences)
  print('샘플의 최대 길이 : {}'.format(max_len))
  ```

* 패딩

  ```python
  sequences = pad_sequences(sequences, maxlen=max_len, padding='pre')
  print(sequences[:3])
  ```

  ```python
  [[ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0    0    0   99  269]
   [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0    0   99  269  371]
   [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0   99  269  371 1115]
  ```

* 레이블 분리

  ```python
  sequences = np.array(sequences)
  X = sequences[:,:-1]
  y = sequences[:,-1]
  ```

* y 원-핫 인코딩

  ```python
  y = to_categorical(y, num_classes=vocab_size)
  ```

  

## 모델 설계

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM
```

* 훈련

  * 각 단어의 임베딩 벡터는 10차원을 가지고 128의 은닉 상태 크기를 가지는 LSTM 사용

  ```python
  model = Sequential()
  model.add(Embedding(vocab_size, 10, input_length=max_len-1))
  # y데이터를 분리하였으므로 이제 X데이터의 길이는 기존 데이터의 길이 - 1
  model.add(LSTM(128))
  model.add(Dense(vocab_size, activation='softmax'))
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  model.fit(X, y, epochs=200, verbose=2)
  ```

* 테스트

  ```python
  def sentence_generation(model, t, current_word, n): # 모델, 토크나이저, 현재 단어, 반복할 횟수
      init_word = current_word # 처음 들어온 단어도 마지막에 같이 출력하기위해 저장
      sentence = ''
      for _ in range(n): # n번 반복
          encoded = t.texts_to_sequences([current_word])[0] # 현재 단어에 대한 정수 인코딩
          encoded = pad_sequences([encoded], maxlen=23, padding='pre') # 데이터에 대한 패딩
          result = model.predict_classes(encoded, verbose=0)
      # 입력한 X(현재 단어)에 대해서 y를 예측하고 y(예측한 단어)를 result에 저장.
          for word, index in t.word_index.items(): 
              if index == result: # 만약 예측한 단어와 인덱스와 동일한 단어가 있다면
                  break # 해당 단어가 예측 단어이므로 break
          current_word = current_word + ' '  + word # 현재 단어 + ' ' + 예측 단어를 현재 단어로 변경
          sentence = sentence + ' ' + word # 예측 단어를 문장에 저장
      # for문이므로 이 행동을 다시 반복
      sentence = init_word + sentence
      return sentence
  ```

  ```python
  # 임의의 단어 'i'에 대해서 10개의 단어를 추가 생성
  print(sentence_generation(model, t, 'i', 10))
  ```
  
```python
  #출력 결과
  i disapprove of school vouchers can i still apply for them
  ```
  
  