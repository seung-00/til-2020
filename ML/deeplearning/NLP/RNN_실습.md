# RNN을 이용한 텍스트 생성

[Eddie 님의 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)을 정리한 내용



## 전처리

* **정수 인코딩**: 텍스트 단어들을 정수들로 매핑시킴

  * 케라스 tokenizer.fit_on_texts를 사용(코퍼스 인자로 주면 빈도수를 기준으로 단어 집합 생성)

* 모델이 문장을 학습하도록 다음과 같은 데이터를 재구성해야 함.

  | samples | X                          | y      |
  | :------ | :------------------------- | :----- |
  | 1       | 경마장에                   | 있는   |
  | 2       | 경마장에 있는              | 말이   |
  | 3       | 경마장에 있는 말이         | 뛰고   |
  | 4       | 경마장에 있는 말이 뛰고    | 있다   |
  | 5       | 그의                       | 말이   |
  | 6       | 그의 말이                  | 법이다 |
  | 7       | 가는                       | 말이   |
  | 8       | 가는 말이                  | 고와야 |
  | 9       | 가는 말이 고와야           | 오는   |
  | 10      | 가는 말이 고와야 오는      | 말이   |
  | 11      | 가는 말이 고와야 오는 말이 | 곱다   |

  ```python
  from tensorflow.keras.preprocessing.text import Tokenizer
  from tensorflow.keras.preprocessing.sequence import pad_sequences
  import numpy as np
  from tensorflow.keras.utils import to_categorical
  
  text = """경마장에 있는 말이 뛰고 있다\n그의 말이 법이다\n가는 말이 고와야 오는 말이 곱다\n"""
  
  t = Tokenizer()
  t.fit_on_texts([text])  # 정수 인코딩
  vocab_size = len(t.word_index) + 1
  # 케라스 토크나이저의 정수 인코딩은 인덱스가 1부터 시작하지만,
  # 케라스 원-핫 인코딩에서 배열의 인덱스가 0부터 시작하기 때문에
  # 배열의 크기를 실제 단어 집합의 크기보다 +1로 생성해야하므로 미리 +1 선언 
  print(f'단어 집합의 크기 : {vocab_size}')
  
  #print(t.word_index)
  
  sequences = []
  for line in text.split('\n'): # \n을 기준으로 문장 토큰화
    # texts_to_sequences()는 입력으로 들어온 코퍼스에 대해서 각 단어를 이미 정해진 인덱스로 변환합니다.
    encoded = t.texts_to_sequences([line])[0]
    for i in range(1, len(encoded)):
      sequence = encoded[:i+1]
      sequences.append(sequence)
  print(f"학습에 사용할 샘플의 수: {len(sequences)}")
  
  print(sequences)
  ```

  ```python
  [[2, 3], [2, 3, 1], [2, 3, 1, 4], [2, 3, 1, 4, 5], [6, 1], [6, 1, 7], [8, 1], [8, 1, 9], [8, 1, 9, 10], [8, 1, 9, 10, 1], [8, 1, 9, 10, 1, 11]]
  ```

* 레이블을 분리해서 훈련 데이터를 만들자. 가장 우측 데이터에 대해서 분리하면 됨.

* 먼저 전체 샘플 길이를 일칫시켜 줘야 함. 가장 긴 샘플의 길이를 기준으로 함.

  ```python
  max_len=max(len(l) for l in sequences) # 모든 샘플에서 길이가 가장 긴 샘플의 길이 출력
  print(f'샘플의 최대 길이 : {max_len}')
  # 샘플의 최대 길이 : 6
  ```

* 전체 샘플의 길이를 6으로 패딩함.

  ```python
  sequences = pad_sequences(sequences, maxlen=max_len, padding='pre') # pre를 주면 길이가 maxlen보다 짧은 샘플의 앞을 0으로 채움
  # pad_sequences은 np.array를 리턴함
  print(sequences)
  ```

  ```python
  [[ 0  0  0  0  2  3]
   [ 0  0  0  2  3  1]
   [ 0  0  2  3  1  4]
   [ 0  2  3  1  4  5]
   [ 0  0  0  0  6  1]
   [ 0  0  0  6  1  7]
   [ 0  0  0  0  8  1]
   [ 0  0  0  8  1  9]
   [ 0  0  8  1  9 10]
   [ 0  8  1  9 10  1]
   [ 8  1  9 10  1 11]
  ```

* 레이블 분리

  ```python
  # Numpy로 레이블 분리
  X = sequences[:,:-1]
  y = sequences[:, -1]  # lable
  ```

  ```python
  print(X)
  ```

  ```python
  [[ 0  0  0  0  2]
   [ 0  0  0  2  3]
   [ 0  0  2  3  1]
   [ 0  2  3  1  4]
   [ 0  0  0  0  6]
   [ 0  0  0  6  1]
   [ 0  0  0  0  8]
   [ 0  0  0  8  1]
   [ 0  0  8  1  9]
   [ 0  8  1  9 10]
   [ 8  1  9 10  1]]
  ```

  ```python
  print(y)
  ```

  ```python
  [ 3  1  4  5  1  7  1  9 10  1 11]
  ```

* 원-핫 인코딩

  ```python
  y = to_categorical(y, num_classes=vocab_size)
  print(y)
  ```

  ```python
  [[0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.] # 3에 대한 원-핫 벡터
   [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] # 1에 대한 원-핫 벡터
   [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.] # 4에 대한 원-핫 벡터
   [0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0.] # 5에 대한 원-핫 벡터
   [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] # 1에 대한 원-핫 벡터
   [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.] # 7에 대한 원-핫 벡터
   [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0.] 
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.] 
   [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] # 1에 대한 원-핫 벡터
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]] # 11에 대한 원-핫 벡터
  ```

  
## 모델 설계

* 훈련

  ```python
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Embedding, Dense, SimpleRNN
  ```

  ```python
  model = Sequential()
  model.add(Embedding(vocab_size, 10, input_length=max_len-1)) # 레이블을 분리하였으므로 이제 X의 길이는 5
  model.add(SimpleRNN(32))
  model.add(Dense(vocab_size, activation='softmax'))
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  model.fit(X, y, epochs=200, verbose=2)
  ```

  * 바닐라 RNN 사용, 단어의 임베딩 벡터는 10차원을 가지고, 32의 은닉 상태 크기를 가짐
  * embedding 레이어
    * ``input_dm`` 단어 사전의 크기
    * ``output_dim`` 단어를 인코딩 한 후 나오는 벡터 크기
    * `input_length` 단어의 수(문장의 길이). 임베딩 레이어의 출력 크기는 `샘플 수 * output_dim*input_length` 가 됨. 임베딩 레이어 다음에 `Flatten` 레이어가 온다면 반드시 지정해야 함. 입력 크기를 알아야 이를 1차원으로 만들어서 `Dense`로 전달할 수 있기 때문



* 테스트 해보기

  ```python
  def sentence_generation(model, t, current_word, n): # 모델, 토크나이저, 현재 단어, 반복할 횟수
    init_word = current_word  # 처음 들어온 단어도 마지막에 같이 출력하기 위에 저장
    sentence = ''
    for _ in range(n):
      encoded = t.texts_to_sequences([current_word])[0] # 현재 단어에 대한 정수 인코딩
      encoded = pad_sequences([encoded], maxlen=5, padding='pre') # 패딩
      result = model.predict_classes(encoded, verbose=0)  # 예측한 단어(Y) 저장
      for word, index in t.word_index.items():
        if index == result: # 만약 예측한 단어와 동일한 단어가 있다면
          break
      current_word = current_word + ' ' + word  # 현재 단어 -> 현재단어 + 예측 단어
      sentence = sentence + ' ' + word  # 예측 단어 저장
    sentence = init_word + sentence
    return sentence
  ```

  ```python
  print(sentence_generation(model, t, "경마장에", 4))
  # 경마장에 뒤에 4개의 단어가 있으므로 4번 예측
  print(sentence_generation(model, t, "그의", 2))
  # 2번 예측
  print(sentence_generation(model, t, "가는", 5))
  # 5번 예측
  ```

  



**print**('열의 개수: ',len(df.columns)) print(df.columns)



df['headline'].isnull().values.any()



```
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
# y데이터를 분리하였으므로 이제 X데이터의 길이는 기존 데이터의 길이 - 1
model.add(LSTM(128))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=2)
```

