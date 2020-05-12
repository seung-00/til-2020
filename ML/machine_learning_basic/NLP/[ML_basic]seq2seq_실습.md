# seq2seq 실습

[Eddie 님의 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)을 정리한 내용



## 글자 레벨 기계 번역기 구현



### 1) 병렬 코퍼스 데이터에 대한 이해와 전처리

* 병령 코퍼스 데이터: 2개 국어 이상의 번역된 문서를 모은 말뭉치, 입력 시퀸스 출력 시퀸스의 길이가 다를 수 있음

* 실습에서 사용되는 [데이터(fra-eng.zip)](http://www.manythings.org/anki) 는 영어 - 프랑스어 문장 사이에 탭으로 구분되는 구조가 하나의 sample임. 이와 같은 형식으로 16만개의 병렬 문장 샘플을 포함하고 있음. `Watch me	Regardez-moi`

  ```python
  import pandas as pd
  lines = pd.read_csv('/Users/seungyoungoh/Downloads/fra-eng/fra.txt', names=['col1', 'col2', 'col3'], sep='\t')
  print(len(lines))
  # 175623
  ```

* ```python
  lines.head()
  ```

  ```python
     col1      col2                                               col3
  0   Go.      Va !  CC-BY 2.0 (France) Attribution: tatoeba.org #2...
  1   Hi.   Salut !  CC-BY 2.0 (France) Attribution: tatoeba.org #5...
  2   Hi.    Salut.  CC-BY 2.0 (France) Attribution: tatoeba.org #5...
  3  Run!   Cours !  CC-BY 2.0 (France) Attribution: tatoeba.org #9...
  4  Run!  Courez !  CC-BY 2.0 (France) Attribution: tatoeba.org #9...
  ```

* col3 을 잘라내자.

  ```python
  lines = lines[["col1", "col2"]]
  lines.columns = ['src', 'tar']	# src 는 source, tar은 target
  lines.head()
  ```

  ```python
      src       tar
  0   Go.      Va !
  1   Hi.   Salut !
  2   Hi.    Salut.
  3  Run!   Cours !
  4  Run!  Courez !
  ```

* 175623개 샘플 중 8만개만 쓰자.

  ```python
  lines = lines[0:80000] # 8만개만 저장
  lines.sample(10)
  ```

  ```python
                                src                                       tar
  49240     It's like one of those.           C'est comme l'une de celles-là.
  20830          The joke's on you.                      On se moque de vous.
  4167                Keep working.                   Continue à travailler !
  5883               I'm motivated.                          Je suis motivée.
  38634       What is he aiming at?                        Quel est son but ?
  38628       What happened to you?                       Que t'arrive-t-il ?
  31578        They handcuffed Tom.                      Ils ont menotté Tom.
  29324        I hope I'm not next.  J'espère que je ne suis pas le prochain.
  66678  Do you want to discuss it?                      Tu veux en discuter?
  26417         Tom is very stupid.                     Tom est très stupide.
  ```

  

* `<sos>` 와 `<eos>` 를 넣어야 함. 여기선 `\t` 와 `\n`를 시작, 종료 심볼로 간주하여 추가함

  ```python
  lines.tar = lines.tar.apply(lambda x : '\t '+ x + ' \n')
  # 판다스 apply lamda 조합은 많이 쓰임
  lines.sample(10) # 랜덤으로 10개 출력
  ```

  ```python
                                 src                                         tar
  47755      I have another job now.       \t J'ai désormais un autre boulot. \n
  40722       He's not always happy.        \t Il n'est pas toujours heureux. \n
  2309                  I recovered.                    \t Je me suis remise. \n
  38489        We're still fighting.             \t Nous nous battons encore. \n
  75836  I hope you understand that.     \t J'espère que vous comprenez cela. \n
  38225        Was anybody in there?         \t Quiconque se trouvait-il là ? \n
  53267     Give me another example.          \t Donnez-moi un autre exemple. \n
  44694       We know all about you.            \t Nous savons tout sur vous. \n
  75563  I don't think that's right.  \t Je ne pense pas que ce soit correct. \n
  69546   I'll never understand you.        \t Je ne vous comprendrai jamais. \n
  ```

* 글자 집합(set)을 생성하자(토큰 단위가 단어가 아닌 글자임!)

  ```python
  # 글자 집합 구축
  src_vocab=set()
  for line in lines.src: # 1줄씩 읽음
      for char in line: # 1개의 글자씩 읽음
          src_vocab.add(char)
  
  tar_vocab=set()
  for line in lines.tar:
      for char in line:
          tar_vocab.add(char)
  ```

* 글자 크기 확인

  ```python
  src_vocab_size = len(src_vocab)+1
  tar_vocab_size = len(tar_vocab)+1
  print(src_vocab_size)
  print(tar_vocab_size)
  
  # 80
  # 100
  ```

  * 영어와 프랑스어에는 각각 양 80, 100개의 글자가 존재함. 토큰화가 잘 되었음을 확인할 수 있음.

* `set`은 인덱싱이 안 되므로 list로 순서를 정해준 뒤에 사용하자.

  ```python
  src_vocab = sorted(list(src_vocab))
  tar_vocab = sorted(list(tar_vocab))
  print(src_vocab[45:75])
  print(tar_vocab[45:75])
  
  #['W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  #['T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']
  
  ```

* 각 글자에 숫자를 매핑시킴

  ```python
  src_to_index = dict([(word, i+1) for i, word in enumerate(src_vocab)])
  tar_to_index = dict([(word, i+1) for i, word in enumerate(tar_vocab)])
  print(src_to_index)
  print(tar_to_index)
  ```

  ```python
  {' ': 1, '!': 2, '"': 3, '$': 4, '%': 5, '&': 6, "'": 7, ',': 8, '-': 9, '.': 10, '/': 11, '0': 12, '1': 13, '2': 14, '3': 15, '4': 16, '5': 17, '6': 18, '7': 19, '8': 20, '9': 21, ':': 22, '?': 23, 'A': 24, 'B': 25, 'C': 26, 'D': 27, 'E': 28, 'F': 29, 'G': 30, 'H': 31, 'I': 32, 'J': 33, 'K': 34, 'L': 35, 'M': 36, 'N': 37, 'O': 38, 'P': 39, 'Q': 40, 'R': 41, 'S': 42, 'T': 43, 'U': 44, 'V': 45, 'W': 46, 'X': 47, 'Y': 48, 'Z': 49, 'a': 50, 'b': 51, 'c': 52, 'd': 53, 'e': 54, 'f': 55, 'g': 56, 'h': 57, 'i': 58, 'j': 59, 'k': 60, 'l': 61, 'm': 62, 'n': 63, 'o': 64, 'p': 65, 'q': 66, 'r': 67, 's': 68, 't': 69, 'u': 70, 'v': 71, 'w': 72, 'x': 73, 'y': 74, 'z': 75, 'ç': 76, 'é': 77, '’': 78, '€': 79}
  
  {'\t': 1, '\n': 2, ' ': 3, '!': 4, '"': 5, '$': 6, '%': 7, '&': 8, "'": 9, '(': 10, ')': 11, ',': 12, '-': 13, '.': 14, '0': 15, '1': 16, '2': 17, '3': 18, '4': 19, '5': 20, '6': 21, '7': 22, '8': 23, '9': 24, ':': 25, '?': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52, 'a': 53, 'b': 54, 'c': 55, 'd': 56, 'e': 57, 'f': 58, 'g': 59, 'h': 60, 'i': 61, 'j': 62, 'k': 63, 'l': 64, 'm': 65, 'n': 66, 'o': 67, 'p': 68, 'q': 69, 'r': 70, 's': 71, 't': 72, 'u': 73, 'v': 74, 'w': 75, 'x': 76, 'y': 77, 'z': 78, '\xa0': 79, '«': 80, '»': 81, 'À': 82, 'Ç': 83, 'É': 84, 'Ê': 85, 'Ô': 86, 'à': 87, 'â': 88, 'ç': 89, 'è': 90, 'é': 91, 'ê': 92, 'ë': 93, 'î': 94, 'ï': 95, 'ô': 96, 'ù': 97, 'û': 98, 'œ': 99, 'С': 100, '\u2009': 101, '\u200b': 102, '‘': 103, '’': 104, '\u202f': 105}
  
  ```

* 훈련 데이터에 정수 인코딩

  * 영어 데이터(인코더의 입력)

  ```python
  encoder_input = []
  for line in lines.src: #입력 데이터에서 1줄씩 문장을 읽음
      temp_X = []
      for w in line: #각 줄에서 1개씩 글자를 읽음
        temp_X.append(src_to_index[w]) # 글자를 해당되는 정수로 변환
      encoder_input.append(temp_X)
  print(encoder_input[:5])
  ```

  ```python
  [[30, 64, 10], [31, 58, 10], [31, 58, 10], [41, 70, 63, 2], [41, 70, 63, 2]]
  ```

  * 프랑스어 데이터(디코더의 입력)

  ```python
  decoder_input = []
  for line in lines.tar:
      temp_X = []
      for w in line:
        temp_X.append(tar_to_index[w])
      decoder_input.append(temp_X)
  print(decoder_input[:5])
  ```

  ```python
  [[1, 3, 48, 53, 3, 4, 3, 2], [1, 3, 45, 53, 64, 73, 72, 3, 4, 3, 2], [1, 3, 45, 53, 64, 73, 72, 14, 3, 2], [1, 3, 29, 67, 73, 70, 71, 105, 4, 3, 2], [1, 3, 29, 67, 73, 70, 57, 78, 105, 4, 3, 2]]
  ```

* 디코코더의 예측값과 비교하기 위한 실제 값 또한, 정수 인코딩 해야함

* 근데 이 실제 값에는 `<sos>`가 있을 필요가 없음

  ```python
  decoder_target = []
  for line in lines.tar:
      t=0
      temp_X = []
      for w in line:
        if t>0:
          temp_X.append(tar_to_index[w])
        t=t+1
      decoder_target.append(temp_X)
  print(decoder_target[:5])
  ```

  ```python
  [[3, 48, 53, 3, 4, 3, 2], [3, 45, 53, 64, 73, 72, 3, 4, 3, 2], [3, 45, 53, 64, 73, 72, 14, 3, 2], [3, 29, 67, 73, 70, 71, 105, 4, 3, 2], [3, 29, 67, 73, 70, 57, 78, 105, 4, 3, 2]]
  ```

  * decorder_input 모든 문장 앞에 붙어있던 숫자 1이 제거된 것을 볼 수 있음. \t가 1이기 때문

* 패딩하기 위해 길이 체크

  ```python
  max_src_len = max([len(line) for line in lines.src])
  max_tar_len = max([len(line) for line in lines.tar])
  print(max_src_len)
  print(max_tar_len)
  
  # 25
  # 76
  ```

* 병렬 데이터 영어와 프랑스어의 길이는 하나의 쌍이어도 전부 길이가 다르므로, 패딩을 할 때도 둘의 길이를 동일하게 맞춰줄 필요가 없음. 각각 언어끼리 맞춰줘야 함. 가장 긴 샘플 길이 맞춰서 25, 76이 되도록 영어와 프랑스어를 패딩

  ```python
  from tensorflow.keras.preprocessing.sequence import pad_sequences
  encoder_input = pad_sequences(encoder_input, maxlen=max_src_len, padding='post')
  decoder_input = pad_sequences(decoder_input, maxlen=max_tar_len, padding='post')
  decoder_target = pad_sequences(decoder_target, maxlen=max_tar_len, padding='post')
  ```

전처리 끝!



### 2) 교사 강요

* seq2seq 이론 파일에 정리했듯이, 디코더 셀은 이전 디코더 셀의 출력을 입력으로 받음. 그런데 위 코드에서는 `decoder_input`을 정의하고 있음.  왜 필요할까?
* 훈련 과정에서는 t(이전 시점)의 디코더 셀의 출력을 t+1(현재 시점)의 입력으로 넣어주는 방식이 아니라, t의 실제 값을 t+1의 입력 값으로 사용하는 방식을 사용함. 
  * 그 까닭은, t의 예측이 틀렸는데 이를 t+1의 예측으로 사용한다면 t+1의 예측도 잘못될 가능성이 높아지고, 연쇄적으로 디코더 전체의 예측을 어렵게 하기 때문임
  * 이런 상황이 반복되면 훈련 시간이 느려짐. 이를 방지하기 위해 t의 예측 값 대신 실제 값을 t+1의 입력으로 사용하는 것임
  * 이를 교사 강요라고 함.

### 3) seq2seq 번역기 훈련



### 3) seq2seq2 기계 번역기 훈련

```python
from tensorflow.keras.layers import Input, LSTM, Embedding, Dense
from tensorflow.keras.models import Model

encoder_inputs = Input(shape=(None, src_vocab_size))
encoder_lstm = LSTM(units=256, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)
# encoder_outputs도 같이 리턴받기는 했지만 여기서는 필요없으므로 이 값은 버림.
encoder_states = [state_h, state_c]
# LSTM은 바닐라 RNN과는 달리 상태가 두 개. 바로 은닉 상태와 셀 상태.
```

* 인코더를 보면, functional API를 사용한다는 것 외에는 다른 실습의 LSTM의 설계와 크게 다르지 않음. LSTM의 hidden state 크기는 256으로 선택함. 인코더의 내부 상태를 디코더로 넘겨주어야 되기 때문에, `return_state = True` 로 설정함. 
* LSTM은 state_h와 state_c를 리턴함. 이 두 상태를 `encoder_states`에 저장함. 이 두 상태를 모두 디코더로 전달함. 이것이 앞서 정리한 context vector임.

```python
decoder_inputs = Input(shape=(None, tar_vocab_size))
decoder_lstm = LSTM(units=256, return_sequences=True, return_state=True)
decoder_outputs, _, _= decoder_lstm(decoder_inputs, initial_state=encoder_states)
# 디코더의 첫 상태를 인코더의 은닉 상태, 셀 상태로 합니다.
decoder_softmax_layer = Dense(tar_vocab_size, activation='softmax')
decoder_outputs = decoder_softmax_layer(decoder_outputs)

model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.compile(optimizer="rmsprop", loss="categorical_crossentropy")

```

```python
model.fit(x=[encoder_input, decoder_input], y=decoder_target, batch_size=64, epochs=50, validation_split=0.2)
```

* 디코더는 인코더의 마지막 hidden state를 초기 hidden statef로 사용함. 디코더도 은닉 상태, 셀 상태를 리턴하기는 하지만 훈련 과정에서 사용하지 않음. 출력 층에 프랑스어 단어 집합의 크기만큼 뉴런을 배치한 후 소프트맥스 함수를 이용해서 실제 값과의 오차를 구함
* 입력으로 `encoder_input`, `decoder_input`이 들어가고, 디코더 실제 값인 `decoder_target`도 필요함(교사 강요) 배치 크기는 64, 총 50 에포크를 학습함. 
* 사실 위에서 설정한 hidden state 크기와 epoch 수는 실제로 훈련 데이터에 과적합을 일으킴. 중간부터 검증 데이터에 대한 오차인  val_loss 값이 올라감. 이번 실습에서는 과적합 이슈를 해결하지는 않음. seq2seq의 성능에 대한 확인에 중점을 두고 과적합 된 상태로 동작 단계로 넘어가도록 함.



### 동작

* 앞서 언급했듯 seq2seq 훈련과 동작은 방식이 조금 다름

  1. 번역하고자 하는 입력 문장이 인코더로 들어가서 hidden, cell state를 얻음
  2. context vector와 `<sos>`에 해당되는 `\t`를 디코더로 보냄
  3. 디코더가 `<EOS>`에 해당하는 `\n`이 나올 때까지 다음 문자를 예측하는 행동을 반복함

  

```python
encoder_model = Model(inputs=encoder_inputs, outputs=encoder_states)
```



```python
# 이전 시점의 상태들을 저장하는 텐서
decoder_state_input_h = Input(shape=(256,))
decoder_state_input_c = Input(shape=(256,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
decoder_outputs, state_h, state_c = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
# 문장의 다음 단어를 예측하기 위해서 초기 상태(initial_state)를 이전 시점의 상태로 사용. 이는 뒤의 함수 decode_sequence()에 구현
decoder_states = [state_h, state_c]
# 훈련 과정에서와 달리 LSTM의 리턴하는 은닉 상태와 셀 상태인 state_h와 state_c를 버리지 않음.
decoder_outputs = decoder_softmax_layer(decoder_outputs)
decoder_model = Model(inputs=[decoder_inputs] + decoder_states_inputs, outputs=[decoder_outputs] + decoder_states)
```

```python
index_to_src = dict((i, char) for char, i in src_to_index.items())
index_to_tar = dict((i, char) for char, i in tar_to_index.items())
```

* 단어들로부터 인데스를 얻는 것이 아니라, 인덱스들로부터 단어를 얻을 수 있는 두 dict를 만들었음.

```python
def decode_sequence(input_seq):
    # 입력으로부터 인코더의 상태를 얻음
    states_value = encoder_model.predict(input_seq)

    # <SOS>에 해당하는 원-핫 벡터 생성
    target_seq = np.zeros((1, 1, tar_vocab_size))
    target_seq[0, 0, tar_to_index['\t']] = 1.

    stop_condition = False
    decoded_sentence = ""

    # stop_condition이 True가 될 때까지 루프 반복
    while not stop_condition:
        # 이점 시점의 상태 states_value를 현 시점의 초기 상태로 사용
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)

        # 예측 결과를 문자로 변환
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = index_to_tar[sampled_token_index]

        # 현재 시점의 예측 문자를 예측 문장에 추가
        decoded_sentence += sampled_char

        # <eos>에 도달하거나 최대 길이를 넘으면 중단.
        if (sampled_char == '\n' or
           len(decoded_sentence) > max_tar_len):
            stop_condition = True

        # 현재 시점의 예측 결과를 다음 시점의 입력으로 사용하기 위해 저장
        target_seq = np.zeros((1, 1, tar_vocab_size))
        target_seq[0, 0, sampled_token_index] = 1.

        # 현재 시점의 상태를 다음 시점의 상태로 사용하기 위해 저장
        states_value = [h, c]

    return decoded_sentence
```

```python
import numpy as np
for seq_index in [3,50,100,300,1001]: # 입력 문장의 인덱스
    input_seq = encoder_input[seq_index: seq_index + 1]
    decoded_sentence = decode_sequence(input_seq)
    print(35 * "-")
    print('입력 문장:', lines.src[seq_index])
    print('정답 문장:', lines.tar[seq_index][1:len(lines.tar[seq_index])-1]) # '\t'와 '\n'을 빼고 출력
    print('번역기가 번역한 문장:', decoded_sentence[:len(decoded_sentence)-1]) # '\n'을 빼고 출력
```



```python
# 출력 결과
-----------------------------------
입력 문장: Run!
정답 문장:  Courez ! 
번역기가 번역한 문장:  Courre ! 
-----------------------------------
입력 문장: I paid.
정답 문장:  J’ai payé. 
번역기가 번역한 문장:  J'ai payé. 
-----------------------------------
입력 문장: Come in.
정답 문장:  Entrez ! 
번역기가 번역한 문장:  Entrez ! 
-----------------------------------
입력 문장: I looked.
정답 문장:  J’ai regardé. 
번역기가 번역한 문장:  J'ai parlé. 
-----------------------------------
입력 문장: Who knows?
정답 문장:  Qui sait ? 
번역기가 번역한 문장:  Qui sait ? 
```

