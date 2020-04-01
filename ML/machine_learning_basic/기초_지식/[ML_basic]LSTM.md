# 장단기 메모리(LSTM)

아래 두 자료를 많이 참고했습니다. 

[Eddie 님의 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)

[KAIST 딥러닝 홀로서기 세미나](https://github.com/heartcored98/Standalone-DeepLearning)





## 1. 바닐라 RNN의 한계

<img src="https://user-images.githubusercontent.com/46865281/77921438-c1517700-72da-11ea-9713-42c9e00d9057.png" alt="image" style="zoom:80%;" />

* 바닐라 RNN은 비교적 짧은 시퀸스에 대해서만 효과를 보이는 단점이 있음. 바닐라 RNN의 시점이 길어질 수록, 앞의 정보가뒤로 충분히 전달이 안 됨. 위 그림에서, 첫 번째 입력 값인 x1의 정보량은 뒤로 갈 수록 소실됨(색깔로 표현).
* 어쩌면 가장 중요한 정보가 시점의 앞에 위치할 수도 있기 때문에 위험함. 
  * 예컨대, "모스크바에 여행을 왔는데 건물도 예쁘고 음식도 맛있었어. 그런데 글쎄 직장 상상한테 전화가 왔어. 어디냐고 묻더라고 나는 말했지. 저 여행왔는데요 여기___"
  * 다음 단어를 에측하기 위해서 맨 앞에 나온 모스크바 단어 정보가 필요함. RNN이 충분한 기억력을 가지고 있지 않다면 문제 발생
* **Vanishing Gradient Problem** 

* LSTM idea: 지금은 하나의 Information Flow가 출력과 전달을 둘다 담당하고 있음. 추가시키면 어떨까?

  

## 2. 바닐라 RNN 내부 뜯어보기

<img src="https://user-images.githubusercontent.com/46865281/77922008-7421d500-72db-11ea-9b50-93e1a31b45c8.png" alt="image" style="zoom:70%;" />

* `ht = tanh(Wx*xt + Wh*ht-1 + b)`



## 3. LSTM(Long short Term Memory)

<img src="https://user-images.githubusercontent.com/46865281/77930869-5efe7380-72e6-11ea-9186-13e18c6dbaa2.png" alt="image" style="zoom:80%;" />

* iead: 잊을 건 잊고 남길 건 남겨서 전달하자!
  * how?

    1. 새로운 cell state

    2. 게이트

       

  ### 게이트

  <img src="https://user-images.githubusercontent.com/46865281/78131275-c38c1080-7455-11ea-8549-7a6415315ba7.png" alt="image" style="zoom:30%;" />

  * 기존 **C_t-1**에 **G**를 통과시켜서 중요한 데이터만 남기도록 함.
  * 그럼 그 계수를 어떻게 정하는가?
    * <img src="https://user-images.githubusercontent.com/46865281/78131911-cc311680-7456-11ea-9b6c-5a384b66b745.png" alt="image" style="zoom:30%;" />

  

  ### cell state

  <img src="https://user-images.githubusercontent.com/46865281/78132231-56797a80-7457-11ea-99d2-cad3216d7f45.png" alt="image" style="zoom:30%;" />

* cell state: 가치 있는 정보들만 전달해주는 벡터

* hidden state: 각각 time step의 결과 값

* 로직

  1. **C_t-1**에서 불필요한 정보를 지움
  2. **C_t-1**에 새로운 input **x_t**와 **h_t-1**를 보고 중요한 정보를 넣음.
  3. 위 과정을 통해 새로운 **C_t**를 만듬
  4. **C_t**를 적당히 가공해 해당 t에서 **h_t**를 만듬
  5. **C_t**와 **h_t**를 다음 스텝 t+1로 전달함

* 삭제 게이트(forget gate), 입력 게이트, 출력 게이트 에는 공통적으로 시그모이드 함수가 존재함. 시그모이드 함수를 지나면 0과 1사이의 값이 나오게 되는데 이 값들을 가지고 게이트를 조절함

  

### 1) forget gate

<img src="https://user-images.githubusercontent.com/46865281/78132775-49a95680-7458-11ea-902f-cc2905b05396.png" alt="image" style="zoom:30%;" /><img src="https://user-images.githubusercontent.com/46865281/78135820-7744ce80-745d-11ea-9244-1a505a43fc66.png" alt="image" style="zoom:40%;" />

* forget gate는 **C_t-1**에서 불필요한 정보를 지움(여기서 계수를 연산하고 뒤에서 이 연산을 씀)
* 0에 가까울 수록 많은 정보가 삭제된 것이고, 1에 가까울수록 정보를 온전히 기억한 것임. 이를 가지고 cell state 를 구하게 됨.



### 2) input gate

<img src="https://user-images.githubusercontent.com/46865281/78133046-bc1a3680-7458-11ea-92c7-fe52628ccdc7.png" alt="image" style="zoom:30%;" /><img src="https://user-images.githubusercontent.com/46865281/78135918-abb88a80-745d-11ea-8eaf-ec923a7317dd.png" alt="image" style="zoom:40%;" />

* input gate 는 현재 정보(**x_t**와 **h_t-1**)를 기억하기 위한 게이트임.

* 시그모이드 함수를 지나 0~1 사이의 값, 하이퍼볼릭탄젠트 함수를 지나 -1~1 사이의 값 두 개가 나오게 됨. 이 두개의 값을 가지고 이번에 선택될 기억의 정보의 양을 정함. 구체적인 건 아래의 셀 상태 수식!

  

### 3)  cell state (장기 상태)

<img src="https://user-images.githubusercontent.com/46865281/78136227-39947580-745e-11ea-8a41-1ccdda630a9d.png" alt="image" style="zoom:33%;" />

* **f_t**, **임시 C_t**를 이용해서 중요한 정보만 남기고 cell state(**C_t**)를 update 
* forget gate, input gate: 이전 상태의 입력 값, 현재 상태의 입력 값을 반영하는 정도
  * 만약 forget gate 출력 값인 **f_t**가 0이 된다면, 이전 시점의 cell state 값인 **C_t-1**은 현재 시점의 셀 상태 값을 결정하기 위한 영향력이 0이 됨. 즉, **input gate의 결과만이 현재 시점의 셀 상태값 C_t를 결정할 수 있음** forget gate가 완전히 닫고 input gate만을 연 상태를 의미함. 
  * 반대로, input gate의 **i_t** 값을 0이라고 한다면, 현재 시점의 셀 상태 값 **C_t**는 오직 이전 시점의 셀 상태값에만 의존함 이는 input gate를 닫고 forget gate만을 연 상태를 의미함.



### 4) output gate, hidden state(단기 상태)

<img src="https://user-images.githubusercontent.com/46865281/78136718-128a7380-745f-11ea-966b-019a44074eb8.png" alt="image" style="zoom:33%;" />

* **o_t**는 output gate 현재 시점의 hidden state를 결정함
* 만약 **o_t** 값이 1이라면 현재 스텝에서 **tanh(C_t)**를 그대로 보내는 것이고, 0이면 지금 스텝에서 그 값을 무시한다. 
* 은닉 상태를 단기 상태라고도 함. 은닉 상태는 장기 상태의 값이 tanh 함수를 지나 -1~1 사이의 값이 된 것. 해당 값은 output gate의 값과 연산되면서 값이 걸러짐. 
* 단기 상태의 값은 또한 출력층으로도 향함.



### 정리

![image-20200401213028298](/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200401213028298.png)

* 전부 h 디멘션임



### So, How LSTM could overcome vanishing gradient problem

<img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200401224304954.png" alt="image-20200401224304954" style="zoom:30%;" />

* 예컨대, 시작 시점의 단어를 마자막 시점에서 가져와야 하는 경우
  * 바닐라 RNN은 tanh 를 계속해서 곱하기 때문에 나중에 back propagation 하면  값이 사라진다
  * 하지만 LSTM에는 cell state 가 있음. cell state는  non-linear function 을 거치지 않음. 덕분에 vanishing gradient problem이 상당 부분 해결됨 





## GRU(Gated Recurrent Unit)

<img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200401225545244.png" alt="image-20200401225545244" style="zoom:30%;" />



* LSTM을 좀 더 간결하게 개선한 모델
  * Update, Reset 게이트 사용
  * cell state가 아닌 hidden state만으로 vanishing gradient 문제 해결
  * 성능은 LSTM과 비슷

