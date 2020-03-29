# RNN 개념

## 개념

* 기존의 FNN(Feedforward Neuarl Network)은 activation function을 지난 값을 오직 output layer로만 보냈다. 한 번 일어난 이벤트는 그걸로 끝이다. 하지만 사람은 그렇지 않다. 한 번 지난 이벤트를 기억한다. RNN은 이런 작용을 구현하고자 등장한 신경망이다.

* <img src="https://user-images.githubusercontent.com/46865281/77843847-f75c0180-71db-11ea-9cfd-4f2cc73e727b.png" alt="image" style="zoom:50%;" />

  * RNN은 위의 두 가지 모양으로 보통 표현된다, 자기 자신을 순환하는 모양, 이를 늘어놓은 모양
  * RNN은 입력층, 은닉층, 출력층 셋으로 구분된다. 은닉층은 memory cell이라고도 불린다.
  * 다양한 형태로 응용될 수 있다. 예컨대 스팸 메일 같은 경우 마지막 출력층만 확인하면 되지만 nlp에서 각 단어에 대해 알아야 하는 경우(ex 품사 태깅) 각각 출력층을 확인해야 할 것이다.

  

* <img src="https://user-images.githubusercontent.com/46865281/77843842-e7dcb880-71db-11ea-9f57-0e57aa91fa33.png" alt="image" style="zoom:50%;" />
  
  * RNN 연산에는 가중치 셋이 포함된다. 이 셋은 은닉층마다 동일하다.



