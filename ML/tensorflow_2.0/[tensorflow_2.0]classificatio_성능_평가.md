# Classification 모델 평가 기준

[송호연님의 글을 보고 정리한 글입니다](https://brunch.co.kr/@chris-song/54)

[구글 머신러닝 단기 집중 과정도 참고했습니다.](https://developers.google.com/machine-learning/crash-course)



### Classification 모델을 평가하는 기준

* 주로 두 가지 값을 확인 함.
  * **accuracy**
  * **loss**

* 그러나 이외에도 판단의 기준이 될 수 있는 몇 가지 지표들이 있음. 
  * 대표적으로 **Precision**과 **Recall**임



### 측정 항목 계산

* 이 값들을 구하기 위해 먼저 **Confusion Matrix**를 그려봐야 함.

  * 예컨대 "늑대가 나타났다"라고 외치는 양치기 소년으로 confusion matrix를 만들어보자.

    <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200324181029206.png" alt="image-20200324181029206" style="zoom:30%;" />

  * 이를 바탕으로 다음을 구할 수 있음.

  * **accuracy(정확성) = (TP+TN) / (TP+TN+FP+FN) => 총 예측 중 맞춘 예측의 비율**

  * **precision(정밀도) = TP / (TP+FP) => positive로 예측된 사례 중 맞춘 비율**

  * **recall(재현율) = TP / (TP+FN) => 실제 positive 중 positve로 예측된 비율**

  

### 왜 다양한 지표가 필요한가?

* 정확도 만으로는 왜 부족한가?

1. 불균형적인 데이터 세트

   * 악성 종양이 9, 양성 종양이 91 있고 이를 예측했다고 가정하자.

   * 악성(positive) 종양을 하나 맞췄고(true), 양성(negative) 종양을 90개 맞췄다.

     | positive | negative |
     | :------: | :------: |
     |  TP = 1  |  FP = 1  |
     |  FN = 8  | TN = 90  |

     결론적으로 정확성 = 0.91

   * 높은 수치지만 이 예측은 엉터리다. 악성 종양 9개 중 하나만 맞췄다. 예컨대, 항상 양성(negative)를 반환하는 모델(예측능력 0)도 같은 accuracy를 가진다.

   * 위 예시에서 precision = 0.5, recall = 0.11 이다. 여기서 recall, precision의 필요성이 느껴진다.



### 오차 선택하기

* 오차가 없는 모델은 존재할 수 없음. 따라서 우리는 오차를 선택해야 함.
  * A 모델: Classification으로 스팸 메일을 검출
  * B 모델: Classification으로 암 환자를 진단

* A 모델의 경우

  * 스팸 메일을 정상 메일함에 보내는 경우 (FN)
  * 정상 메일을 스팸 메일함에 보내는 경우 (FP)
  * 여기서 치명적인 오차는, 후자(FP)임

* B 모델의 경우

  * 암 환자를 정상으로 분류 (FN)
  * 정상 환자를 암으로 분류 (FT)
  * 여기서 치명적인 오차는 전자(FN)임.

* A는 FP을, B는 FN을 줄이고 싶어함. 이는 accuracy만으로 힘듬 => precision, recall의 필요성 

  

  <img src="https://i1.wp.com/i.imgur.com/cJDJU.png" alt="Precision, recall" style="zoom:75%;" />[^1]

  * precision(정밀도) = TP / (TP+**FP**), recall(재현율) = TP / (TP+**FN**) 이므로 A는 정밀도를, B는 재현율을 주의해서 체크해야할 것임.

    

  

* 이외에도 **Fall-out(FPR)** 과 **AUC** 등의 대표적인 평가 기준들이 존재함.

  

[^1]:https://uberpython.wordpress.com/2012/01/01/precision-recall-sensitivity-and-specificity/