# RNN 구현

[Eddie 님의 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)을 정리한 내용

[toc]

## 0. 텐서

* 3D 텐서

  ```python
  d=np.array([
              [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [10, 11, 12, 13, 14]],
              [[15, 16, 17, 18, 19], [19, 20, 21, 22, 23], [23, 24, 25, 26, 27]]
              ])
  print(d.ndim)
  print(d.shape)
  ```

  ```python
  3
  (2, 3, 5)
  ```

  * 3D 텐서(shape)의 (samples, timesteps, word_dim)은 (batch_size, timesteps, word_dim)이라 생각할 수 있음

* 텐서 크기

  * 텐서 연산

  ![image](https://user-images.githubusercontent.com/46865281/77853292-64908680-721e-11ea-9902-8afdfe1b2cb5.png)

  <img src="https://user-images.githubusercontent.com/46865281/77853298-6d815800-721e-11ea-8330-23ebefc8639d.png" alt="image" style="zoom:50%;" />

  * 텐서 크기

    * xt는 입력 벡터임. NLP에서 입력 벡터는 대부분 단어 벡터로 간주할 수 있음. 단어 벡터의 차원을 d,  은닉 상태의 크기를 Dh라 가정했을 때 각 텐서의 크기는 다음과 같음

      <img src="https://user-images.githubusercontent.com/46865281/77852734-33628700-721b-11ea-8f51-767df372926e.png" alt="image" style="zoom:50%;" />

    * 배치 크기가 1이고 d와 Dh 두 값 모두 4로 가정했을 때 RNN 은닉층 연산은 아래와 같음

  <img src="https://user-images.githubusercontent.com/46865281/77853305-770ac000-721e-11ea-9ca6-a83be9b9af66.png" alt="image" style="zoom:50%;" />

## 1. 케라스로 RNN 구현하기

* 케라스 API로 RNN 구현

* 은닉층 추가

  * `input_shape`는 배치 크기를 제외하고 차원(input_length, input_dim)을 지정함.

  * ```python
    hidden_size = 3
    timesteps = 3
    input_dim = 3
    model.add(SimpleRNN(hidden_size,input_shape=(timesteps, input_dim))) # 아래와 동일
    model.add(SimpleRNN(hidden_size, input_length = timesteps, input_dim = input_dim))
    ```

    * hidden_size = 은닉 상태의 크기를 정의, 메모리 셀이 다음 시점의 메모리 셀과 출력층으로 보내는 값의 크기(output_dim)와도 동일. RNN의 용량(capacity)를 늘린다고 보면 됨. 중소형 모델의 경우 보통 128, 256, 512, 1024 등의 값을 가짐
    * timesteps = 입력 시퀸스의 길이(input_length)라고도 표현됨. 시점의 수
    * input_dim = 입력의 크기
    * <img src="https://user-images.githubusercontent.com/46865281/77844147-e06ade80-71de-11ea-813b-a3f76fa73e55.png" alt="image" style="zoom:80%;" />

  * 헷갈리지 말아야 하는 점은 위 코드가 출력층까지 포함한 ANN 코드가 아니라 은닉층에 대한 코드라는 것임. 해당 코드가 리턴하는 결과값은 출력층의 결과가 아니라 하나의 은닉 상태 또는 정의하기에 따라 다수의 은닉 상태임

    <img src="https://user-images.githubusercontent.com/46865281/77844163-f8426280-71de-11ea-8546-7e91afd1f0e0.png" alt="image" style="zoom:80%;" />

* 위에서 설명한 3D 텐서를 받아서 은닉 상태를 출력해보자. RNN층은 사용자 설정에 따라 두 가지 종류의  출력을 내보낸다.

* 메모리 셀의 최종 시점의 은닉 상태만을 리턴하고자 한다면 `(batch_size, output_dim)` 크기의 텐서를 리턴한다(output_dim은 앞서 코드에 정의한 hidden_size의 값으로 설정됨)

* 메모리의 각 시점(time step)의 은닉 상태값들을 모아서 전체 시퀸스를 리턴하고자 한다면 `(batch_size, timesteps, output_dim)` 크기의 3D 텐서를 리턴함. RNN층의 `return_sequences` 매개변수 True를 넣어서 설정

  * <img src="https://user-images.githubusercontent.com/46865281/77853199-c69cbc00-721d-11ea-80ca-0aac22f397ea.png" alt="image" style="zoom:80%;" />

    1. 출력값이 (batch_size, output_dim) 크기의 2D 텐서일 때, output_dim은 hidden_size의 값인 3임. 이 경우 batch_size를 현 단계에서는 알 수 없으므로 (None, 3)이 됨.

       ```python
       model = Sequential()
       model.add(SimpleRNN(3, input_shape=(2,10)))
       # model.add(SimpleRNN(3, input_length=2, input_dim=10))와 동일함.
       model.summary()
       ```

       ```python
       _________________________________________________________________
       Layer (type)                 Output Shape              Param #   
       =================================================================
       simple_rnn_1 (SimpleRNN)     (None, 3)                 42        
       =================================================================
       Total params: 42
       Trainable params: 42
       Non-trainable params: 0
       _________________________________________________________________
       ```

       

    2. batch_size를 8로 기재하자 출력의 크기가 (8, 3)이 됐음. 

       ```python
       model = Sequential()
       model.add(SimpleRNN(3, input_shape=(2,10)))
       # model.add(SimpleRNN(3, input_length=2, input_dim=10))와 동일함.
       model.summary()
       ```

       ```python
       _________________________________________________________________
       Layer (type)                 Output Shape              Param #   
       =================================================================
       simple_rnn_2 (SimpleRNN)     (8, 3)                    42        
       =================================================================
       Total params: 42
       Trainable params: 42
       Non-trainable params: 0
       _________________________________________________________________
       ```

    

    3. `return_sequences` 매개 변수에 True를 넣어서 출력 값으로 (batch_size, teimesteps, output_dim) 크기의 3D 텐서를 리턴하도록 함

       ```python
       model = Sequential()
       model.add(SimpleRNN(3, batch_input_shape=(8,2,10)))
       model.summary()
       ```

       ```python
       Layer (type)                 Output Shape              Param #   
       =================================================================
       simple_rnn_3 (SimpleRNN)    (8, 2, 3)                 42        
       =================================================================
       Total params: 42
       Trainable params: 42
       Non-trainable params: 0
       _________________________________________________________________
       ```

       

## 2. 파이썬으로 RNN 구현하기

* Numpy로 RNN 층을 구현해보자.

* 의사 코드

  ```python
  hidden_state_t = 0	# 초기 은닉 상태를 0으로 초기화
  for input_t in input_length:	# 각 시점 마다 입력을 받음
    output_t = tanh(input_t, hidden_state_t)	# 각 시점에 대해서 입력과 은닉 상태를 가지고 연산
    hidden_state_t = output_t	# 계산 결과는 현재 시점의 은닉 상태가 됨
  ```

  * 입력 데이터의 길이(`input_length`)는 곧 총 시점의 수(`timesteps`)가 됨

* 실제 코드

  *  `(timesteps, input_dim)` 크기의 2D 텐서를 입력으로 받았다고 가정. 실제 케라스에서는 `(batch_size timesteps, input_dim)` 크기의 3D 텐서를 입력으로 받음

    ```python
    timesteps = 10	# 시점의 수, NLP에서 보통 문장의 길이
    input_dim = 4		# 입력의 차원, NLP에서 보통 단어 벡터의 차원
    hidden_size = 8	# 은닉 상태의 크기, 메모리 셀의 용량
    
    inputs = np.random.random((timesteps, input_dim))	# 입력에 해당되는 2D 텐서
    
    hidden_state_t = np.zeros((hidden_size,))	# 초기 은닉 상태 0으로 초기화
    # print(hidden_state_t)
    # [0. 0. 0. 0. 0. 0. 0. 0.]
    ```

  * 가중치와 편향을 정의하자.

    ```python
    Wx = np.random.random((hidden_size, input_dim))		# (8, 4) 크기의 2D 텐서 생성. 입력에 대한 가중치
    Wh = np.random.random((hidden_size, hidden_size))	# (8, 8) 크기의 2D 텐서 생성. 은닉 상태에 대한 가중치
    b = np.random.random((hidden_size,))	# (8,) 크기의 1D 텐서 생성. 편향 값
    ```

    ```python 
    print(np.shape(Wx))
    print(np.shape(Wh))
    print(np.shape(b))
    
    # (8, 4)
    # (8, 8)
    # (8,)
    ```

  * RNN 동작

    ```python
    total_hidden_states = []
    
    # 메모리 셀 동작
    for input_t in inputs:	# 각 시점에 따라서 입력 값이 입력됨
      output_t = np.tanh(np.dot(Wx, input_t) + np.dot(Wh, hidden_state_t) + b)	# Wx * Wt + Wh * Ht-1 + bias
      total_hidden_states.append(list(output_t))	# 각 시점의 은닉 상태의 값을 축적
      print(np.shape(total.hidden_states))	# 각 시점 t 별 메모리 셀의 출력 크기는 (timestep, output_dim)
      hidden_statet_t = output_t
    
    total_hidden_states = np.stack(total_hidden_states, axis = 0)	# 출력 시 값을 깔끔하게 해줌
    print(total_hidden_states)	# (timesteps, output_dim)의 크기를 가지는 메모리 셀의 2D 텐서 출력
    ```

    ```python
    (1, 8)
    (2, 8)
    (3, 8)
    (4, 8)
    (5, 8)
    (6, 8)
    (7, 8)
    (8, 8)
    (9, 8)
    (10, 8)
    [[0.93836572 0.94239977 0.61089493 0.85625564 0.97119515 0.94672841
      0.83126293 0.94114758]
     [0.96256592 0.96564838 0.6640777  0.94291938 0.98926012 0.96586418
      0.91825437 0.9838136 ]
     [0.89173082 0.9072339  0.52118547 0.66452701 0.88351775 0.91137092
      0.59220838 0.75496938]
     [0.90538905 0.91895338 0.63750278 0.84511139 0.97612684 0.91623235
      0.90784462 0.96360081]
     [0.9501785  0.95824322 0.55813525 0.89875341 0.94828819 0.95436944
      0.7005903  0.91960607]
     [0.90236551 0.91699475 0.57515166 0.91516117 0.96110816 0.87794687
      0.8165194  0.95267371]
     [0.98657398 0.98447833 0.6989226  0.96283024 0.99566207 0.98924038
      0.9191156  0.98853013]
     [0.90206802 0.88313661 0.58269213 0.72558216 0.96271124 0.90068083
      0.7297956  0.85361707]
     [0.79271956 0.79229045 0.58470809 0.48462526 0.94034204 0.81324114
      0.80872776 0.82680339]
     [0.96664011 0.95968941 0.65668382 0.88107166 0.98880112 0.97257098
      0.86287557 0.95847878]]
    ```

    

  

