# seq2seq 이론

[Eddie 님의 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)을 정리한 내용



* seq2seq은 기계 번역에서 대표적으로 사용되는 모델

  <img src="https://user-images.githubusercontent.com/46865281/78332087-46ca7500-75c2-11ea-8c4c-6e0c8b960399.png" alt="image" style="zoom:80%;" />



* seq2seq는 인코더와 디코더로 구성된다.
  * 인코더는 문장의 단어들을 순차적으로 입력받은 뒤 압축해서 하나의 벡터로 만듬. 이를 context vector 라고 함.
  * 디코더는 컨텍스트 벡터를 받아서 번역된 단어를 순차적으로 출력함



* <img src="https://user-images.githubusercontent.com/46865281/78332250-9741d280-75c2-11ea-980a-f95f147cade4.png" alt="image" style="zoom:80%;" />

  1. 인코더, 디코더는 각각 RNN 아키텍처로 구성됐음. 보통 LSTM 또는 GRU를 씀.
     * 토큰화된 단어 각각을 셀에 넣고 인코더의 마지막 hidden state를 디코더 셀로 넘겨주는데 이것이 context vector임.
     * context vector는 디코더 RNN 셀의 첫 번째 hidden state로 사용됨

  2. 테스트 과정에서, 디코더는 초기 입력으로 문장의 시작을 의미하는 심볼 `<sos>`가 들어감. 디코더는 `<sos>` 가 입력되면 다음에 등장할 확률이 높은 단어를 예측하기 시작함. 
  3. seq2seq의 훈련 과정은 테스트 과정과 조금 다름. **교사 강요**



* 입, 출력 부분을 좀 더 자세히 보자.

  <img src="https://user-images.githubusercontent.com/46865281/78332842-bc831080-75c3-11ea-8444-c710c89bf531.png" alt="image" style="zoom:80%;" />

  <img src="https://user-images.githubusercontent.com/46865281/78332990-010eac00-75c4-11ea-8ec2-9aa1004b8823.png" alt="image" style="zoom:100%;" />

  * 머신은 텍스트보다 숫자를 잘 처리하므로, seq2seq는 임베딩 된 단어 벡들을 입력으로 받음.
  * 위 그림과 같이 I am, a, student 각각 단어가 임베딩 벡터로 표현되어 쓰임



* 디코더를 좀 더 자세히 보자.

  <img src="https://user-images.githubusercontent.com/46865281/78333160-49c66500-75c4-11ea-9543-3a237e7eaaf6.png" alt="image" style="zoom:100%;" />

  * 디코더 첫 번째 셀의 hidden state 값은 context vector(인코더의 마지막 hidden state) 임
  * 디코더의 첫 번째 셀은, 이 context vector 값과 현재 t(time step)에서 입렵값인 `<sos>`로부터 다음에 등장할 단어를 예측함
  * 이 예측된 단어는 t+1의 입렵값이 되고 t+1 셀은 이 입렵값과 t에서의 hidden state로부터 t+1에서의 출력 벡터를 예측함. 이 출력 값이 다음 time step의 입력값이 됨
  * 디코더 각 time step에서 출력 벡터를 softmax 함수에 넣어 각 단어별 확률 값을 구함.이를 보고 디코더는 출력 단어를 결정함.

