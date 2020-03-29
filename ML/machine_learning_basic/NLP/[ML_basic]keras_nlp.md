# keras API for NLP

[Eddie 님의 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)을 정리한 내용

[toc]

## 1. 전처리(Preprocessing)

* Tokenizer()

  * ```python
    from tensorflow.keras.preprocessing.text import Tokenizer
    t  = Tokenizer()
    fit_text = "The earth is an awesome place live"
    t.fit_on_texts([fit_text])
    
    test_text = "The earth is an great place live"
    sequences = t.texts_to_sequences([test_text])[0]
    
    print("sequences : ",sequences) # great는 단어 집합(vocabulary)에 없으므로 출력되지 않는다.
    print("word_index : ",t.word_index) # 단어 집합(vocabulary) 출력
    
    
    #sequences :  [1, 2, 3, 4, 6, 7]
    #word_index :  {'the': 1, 'earth': 2, 'is': 3, 'an': 4, 'awesome': 5, 'place': 6, 'live': 7}
    ```

    

* pad_sequence()

  * 정해준 길이보다 길이가 긴 샘플은 자르고, 짧으면 0을 채움

  * ```python
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    pad_sequences([[1, 2, 3], [3, 4, 5, 6], [7, 8]], maxlen=3, padding='pre')
    # 전처리가 끝나서 각 단어에 대한 정수 인코딩이 끝났다고 가정하고, 3개의 데이터를 입력으로 합니다.
    
    
    #array([[1, 2, 3],
    #       [4, 5, 6],
    #       [0, 7, 8]], dtype=int32)
    ```

    * 첫 번째 인자 = 패딩할 데이터
    * maxlen = 정규화할 길이
    * padding = pre 를 선택하면 앞에 0을 채우고 post를 선택하면 뒤에 0을 채움



## 2. 워드 임베딩





## 3. 모델링

* Sequential()

  * ```python
    from tensorflow.keras.models import Sequential
    model = Sequential()
    model.add(...)	# 층 추가
    model.add(...)	# 층 추가
    model.add(...)	# 층 추가
    ```



* 임베딩

  * 임베딩 층 또한 인공 신경망의 층의 하나이므로 추가시킨다

  * ```python
    from tensorflow.keras.models import Sequential
    model = Sequential()
    model.add(Embedding(vocabulary, output_dim, input_length))
    ```

  

* Dense()

  * 전결합층(fully-conntected layer)을 추가한다.

  * ```python
    from tensorflowl.keras.models import Sequential
    from tensorflowl.keras.layers import Dense
    model = Sequential()
    model.add(Dense(1, input_dim=3, activation='relu'))
    ```

    * 첫 번째 인자 = 출력 뉴런의 수
    * input_dim = 입력 뉴런의 수(입력의 차원)
    * activation =  활성화 함수

    <img src="https://wikidocs.net/images/page/32105/neural_network1_final.PNG" alt="img" style="zoom:100%;" />

  * ```python
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    model = Sequential()
    model.add(Dense(8, input_dim=4, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))	# 출력층
    ```

    <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200328220709505.png" alt="image-20200328220709505" style="zoom:80%;" />

    * 두 번째 `Dense()`에 `input_dim` 인자가 없음. 이는 이미 이전층의 뉴런의 수가 8개라는 사실을 아고 있기 때문임



* summary()

  * ```python
    model.summary()
    ```

  * <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200328221214367.png" alt="image-20200328221214367" style="zoom:50%;" />



## 4. 컴파일(Compile)과 훈련(Training)

* compile()

  * 모델을 기계가 이해하도록 컴파일함. 오차 함수, 최적화 방법, 메트릭 함수를 선택 가능

  * ```python
    from tensorflow.keras.layers import SimpleRNN, Embedding, Dense
    from tensorflow.keras.models import Sequential
    max_features = 10000
    
    model = Sequential()
    model.add(Embedding(max_features, 32))
    model.add(SimpleRNN(32))
    model.add(Dense(1, activation = 'sigmoid'))
    model.compile(optimizer = 'rmsprop', loss = 'binary_cross')
    ```

    * optimizer = 훈련 과정을 설정하는 옵티마이저 설정, 'adam', 'sgd' 등
    * loss = 훈련 과정에서 사용할 손실함수를 설정
    * mertircs = 훈련을 모니터링하기 위한 지표를 선택

  * 대표적으로 쓰이는 손실 함수

    <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200328222705875.png" alt="image-20200328222705875" style="zoom:50%;" />



* fit(): 모델을 학습(훈련, fitting)함. 모델이 오차로부터 매개 변수를 업데이트 시키는 과정

  * ```python
    model.fit(x_train, y_train, epochs=10, batch_size=32)
    ```

    * 첫 번째 인자 = 훈련 데이터에 해당
    * 두 번째 인자 = 지도 학습에서 레이블 데이터에 해당
    * epochs = 총 훈련 횟수, 에포크 1은 전체 데이터를 한 차례 훑고 지나갔음을 의미함. 
    * batch_size = 배치 크기. 기본 값은 32, 미니 배치 경사 하강법을 사용하고 싶지 않다면 `batch_size = None` 입력

  * 더 많은 인자를 사용하는 경우

    ```python
    model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0, validation_data(X_val,y_val))
    ```

    * validation_data(x_val,  y_val) = 검증 데이터를 사용함. 검증 데이터를 사용하면 각 에포크마다 검증 데이터의 정확도도 함께 출력됨. **검증 데이터의 loss가 낮아지다가 높아지기 시작하면 이는 과적합(overfitting)의 신호**

    * validation_split = validation_data 대신 사용할 수 있음. 검증 데이터를 사용하는 건 동일하지만, 별도로 존재하는 검증 데이터를 주는게 아니라 X_train과 y_trian에서 일정 비율을 분리해서 이를 검증데이터로 사용함. validation_data와 마찬가지로 훈련에 반영되지 않고 훈련 과정을 지켜보기 위한 용도로 사용

      ```python
      # 훈련 데이터의 20%를 검증 데이터로 사용
      validation_data(X_train, y_train, epochs=10, batch_size=32, verbose=0, validation_split=0.2)
      ```

    * verbose = 학습 중 출력되는 문구를 설정

      * `0` : 출력 x

      * `1` : 훈련의 진행도를 보여주는 진행막대

        * ```python
          # verbose = 1일 경우.
          Epoch 88/100
          7/7 [==============================] - 0s 143us/step - loss: 0.1029 - acc: 1.0000
          ```

      * `2` 미니 배치마다 손실 정보를 출력함

        * ```python
          # verbose = 2일 경우.
          Epoch 88/100
           - 0s - loss: 0.1475 - acc: 1.0000
          ```

    

## 5. 평가와 예측

* evaluate()

  * 테스트 데이터를 통해 학습된 모델에 대한 정확도를 평가

    ```python
    model.evaluate(X_test, y_test, batch_size=32)
    ```

    * 첫 번째 인자 = 테스트 데이터에 해당
    * 두 번째 인자 = 지도 학습에서 레이블 리스트 데이터에 해당
    * batch_size = 배치 크기

  

* predict()

  * 입력에 대한 모델의 출력 값 확인

    ```python
    model.predict(X_input, batch_size=32)
    ```

    * 첫 번쨰 인자 = 예측하고자 하는 데이터
    * batch_size = 배치 크기



## 6. 모델의 저장과 로드

* 모델을 저장한다는 것은 학습이 끝난 신경망의 구조를 보존하고 계속해서 사용할 수 있다는 의미

* save()

  * ann 모델을 hdf5 파일에 저장함

    ```python
    model.save("model_name.h5")
    ```



* load_model()

  * 저장해둔 모델을 불러옴

    ```python
    from tensorflow.keras.models import load_model
    model = load_model("model_name.h5")
    ```

    



# Keras Functional API for NLP

* sequential API는 여러층을 공유하거나 다양한 종류의 입력과 출력을 사용하는 등의 복잡한 모델을 만드는 일을 하기에 한계가 있음. functional API를 써보자

## sequential API로 만든 모델

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model=Sequential()
model.add(Dense(3, input_dim=4, activation='softmax'))
```

* 직관적이고 편하지만, 단순히 층을 쌓는 것만으로는 구현할 수 없는 복잡한 ANN을 구현할 수 없음



## functional API로 만든 모델

* functional API는 각 층을 일종의 함수로 정의함. 그리고 각 함수를 조합하기 위한 연산자들을 제공함. 이를 이용해 신경망을 설계.

* 아래 두 코드는 동일한 표기임

  ```python
  encoder = Dense(128)(input)
  ```

  ```python
  encoder = Dense(128)
  encoder(input)
  ```



### 1) 전결합 피드 포워드 신경망(Fully-connected FFNN)

* sequential API와 다르게 입력 데이터의 크기(shape)를 인자로 입력층에 정의해줘야함. 여기서 입력의 차원이 1인 FNNN을 만든다고 가정해보겠음

  ```python
  from tensorflow.keras.layers import Input
  # 텐서를 리턴한다
  inputs = Input(shape(10,0))
  ```

* 위 코드는 10개 입력층을 받았음. 이제 위의 코드에 은닉층과 출력층을 추가해보자.

  ```python
  from tensorflow.keras.layers import Input, Dense
  inputs = Input(shape(10,0))
  hidden1 = Dense(64, activation='relu')(inputs)
  hidden2 = Dense(64, acitvation='relu')(hidden1)
  output = Dense(1, acitvation='sigmoid')(hidden2)
  ```

* 이제 하나의 모델을 구성해보자. 이는 모델에 입력 텐서와 출력텐서를 넣어서 완성됨.

  ```python
  from tensorflow.keras.layers import Input, Dense
  from tensorflow.keras.models import Model
  inputs = Input(shape=(10,))
  hidden1 = Dense(64, activation='relu')(inputs)
  hidden2 = Dense(64, activation='relu')(hidden1)
  output = Dense(1, activation='sigmoid')(hidden2)
  model = Model(inputs=inputs, outputs=output)
  ```

* 지금까지 내용을 정리해보자.

  * `Input()` 함수에 입력의 크기 정의

  * 각 층들을 연결해줌

  * `Model()` 함수에 입력과 출력 정의

    

* 이를  모델에 저장하면 sequential API를 사용할 때처럼 model.compile, model.fit 등을 사용 가능함

  ```python
  model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
  model.fit(data, labels)
  ```

* 은닉층과 출력층의 변수명을 통일해서 FFNN을 다시 만들어보자.

  ```python
  inputs = Input(shape=(10,))
  x = Dense(8, activation="relu")(inputs)
  x = Dense(4, activation="relu")(x)
  x = Dense(2, activation="linear")(x)
  model = Model(inputs, x)
  ```

  

### 2) 선형 회귀

```python
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
import numpy as np

dat_test=np.array([1,2,3,4,5,6,7,8,9]) # 공부하는 시간
y_cts_test=np.array([11,22,33,44,53,66,77,87,95]) # 각 공부하는 시간에 맵핑되는 성적

inputs = Input(shape=(1,))
output = Dense(1, activation='linear')(inputs)
linear_model = Model(inputs, output)

linear_model.compile(optimizer='sgd', loss='mse')
linear_model.fit(x=dat_test, y=y_cts_test, epochs=300, verbose=1)
```

```python
%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(dat_test, linear_model.predict(dat_test), 'b', dat_test, y_cts_test, 'k.')
```

```python
print(linear_model.predict([9.5]))

# [[101.930046]]
```



### 3) 로지스틱 회귀

```python
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

inputs = Input(shape=(3,))
output = Dense(1, activation='sigmoid')(inputs)
logistic_model = Model(inputs, output)

logistic_model.compile(optimizer='sgd', loss = 'binary_crossentropy', metrics=['accuracy'])
logistic_model.optimizer.lr = 0.001
logistic_model.fit(x=dat_train, y=y_classifier_train, epochs = 5, validation_data = (dat_test, y_classifier_test))
```



### 4) 다중 입력을 받는 모델

```python
from tensorflow.keras.layers import Input, Dense, concatenate
from tensorflow.keras.models import Model

# 두 개의 입력층을 정의
inputA = Input(shape=(64,))
inputB = Input(shape=(128,))

# 첫번째 입력층으로부터 분기되어 진행되는 인공 신경망을 정의
x = Dense(16, activation="relu")(inputA)
x = Dense(8, activation="relu")(x)
x = Model(inputs=inputA, outputs=x)

# 두번째 입력층으로부터 분기되어 진행되는 인공 신경망을 정의
y = Dense(64, activation="relu")(inputB)
y = Dense(32, activation="relu")(y)
y = Dense(8, activation="relu")(y)
y = Model(inputs=inputB, outputs=y)

# 두개의 인공 신경망의 출력을 연결(concatenate)
result = concatenate([x.output, y.output])

# 연결된 값을 입력으로 받는 밀집층을 추가(Dense layer)
z = Dense(2, activation="relu")(result)
# 선형 회귀를 위해 activation=linear를 설정
z = Dense(1, activation="linear")(z)

# 결과적으로 이 모델은 두 개의 입력층으로부터 분기되어 진행된 후 마지막에는 하나의 출력을 예측하는 모델이 됨.
model = Model(inputs=[x.input, y.input], outputs=z)
```



### 5) RNN 은닉층 사용

```python
from tensorflow.keras.layers import Input, Dense, LSTM
from tensorflow.keras.models import Model
inputs = Input(shape=(50,1))
lstm_layer = LSTM(10)(inputs) # RNN의 일종인 LSTM을 사용
x = Dense(10, activation='relu')(lstm_layer)
output = Dense(1, activation='sigmoid')(x)
model = Model(inputs=inputs, outputs=output)
```

