# 첫 번째 신경망 훈련하기: 기초적인 분류 문제



```python
# tensorflow와 tf.keras를 임포트합니다
import tensorflow as tf
from tensorflow import keras

# 헬퍼(helper) 라이브러리를 임포트합니다from __future__ import absolute_import, division, print_function, unicode_literals, unicode_literals

import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)
```

```python
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
```

>패션 MNIST는 컴퓨터 비전 분야의 "Hello, World" 프로그램격인 고전 [MNIST](http://yann.lecun.com/exdb/mnist/) 데이터셋을 대신해서 자주 사용됩니다. MNIST 데이터셋은 손글씨 숫자(0, 1, 2 등)의 이미지로 이루어져 있습니다. 여기서 사용하려는 옷 이미지와 동일한 포맷입니다.
>
>패션 MNIST는 일반적인 MNIST 보다 조금 더 어려운 문제이고 다양한 예제를 만들기 위해 선택했습니다. 두 데이터셋은 비교적 작기 때문에 알고리즘의 작동 여부를 확인하기 위해 사용되곤 합니다. 코드를 테스트하고 디버깅하는 용도로 좋습니다.
>
>네트워크를 훈련하는데 60,000개의 이미지를 사용합니다. 그다음 네트워크가 얼마나 정확하게 이미지를 분류하는지 10,000개의 이미지로 평가하겠습니다. 패션 MNIST 데이터셋은 텐서플로에서 바로 임포트하여 적재할 수 있습니다:



* load_data() 함수를 호출하면 네 개의 넘파이(NumPy) 배열이 반환됩니다.
  * `train_images`와 `train_labels` 배열은 모델 학습에 사용되는 *훈련 세트*입니다
  * `test_images`와 `test_labels` 배열은 모델 테스트에 사용되는 *테스트 세트*입니다.

* 이미지는 28x28 크기의 넘파이 배열이고 픽셀 값은 0과 255 사이입니다. *레이블*(label)은 0에서 9까지의 정수 배열입니다. 이 값은 이미지에 있는 옷의 *클래스*(class)를 나타냅니다. 

<img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200322191906700.png" alt="image-20200322191906700" style="zoom:50%;" />

* 각 이미지는 하나의 레이블에 매핑되어 있는데, 데이터셋에 클래스 이름이 들어있지 않기 때문에 나중에 이미 출력할 때 사용하기 위해 별도 변수를 만들어 저장해두자.

```python
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
```



### 데이터 탐색

* 모델을 훈련하기 전에 데이터셋 구조를 살펴보자. 

* 다음 코드는 훈련 세트에 60,000개의 이미지가 있다는 것을 보여줍니다. 각 이미지는 28x28 픽셀로 표현됩니다.

  ```python
  train_images.shape
  # (60000, 28, 28)
  ```

* 훈련 세트에는 60,000 개의 레이블이 있음, 각 레이블은 0과 9 사이의 정수임

  ```python
  len(train_labels)
  # 60000
  
  train_labels
  # array([9, 0, 0, ..., 3, 0, 5], dtype=uint8)
  ```

* 마찬가지로, 테스트 세트에는 10,000개의 이미지가 있으며 10,000개의 이미지에 대한 레이블을 가지고 있음

  ```python
  test_images.shape
  # (10000, 28, 28)
  
  len(test_labels)
  # 100000
  ```

  

### 데이터 전처리

네트워크를 훈련하기 전에 데이터를 전처리해야 함. 

* 훈련 세트에 있는 첫 번째 이미지를 보면 픽셀 값 범위가 0~255로 표시되는 것을 알 수 있음

```python
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
```

<img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200322201921794.png" alt="image-20200322201921794" style="zoom:50%;" />

* 신경망 모델에 주입하기 전에 이 값의 범위를 0~1 사이로 조정하겠음. 이렇게 하려면 255로 나누어야 함. *훈련 세트* 와 *테스트 세트* 를 동일한 방법으로 전처리 하는 것이 중요함.

  ```python
  train_images = train_images / 255.0
  
  test_images = test_images / 255.0
  ```

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200322202427863.png" alt="image-20200322202427863" style="zoom:50%;" />

* 데이터 포맷이 올바른지 확인하고 네트워크 구성과 훈련할 준비를 마칩니다.

  ```python
  plt.figure(figsize=(10,10))
  for i in range(25):
      plt.subplot(5,5,i+1)
      plt.xticks([])
      plt.yticks([])
      plt.grid(False)
      plt.imshow(train_images[i], cmap=plt.cm.binary)
      plt.xlabel(class_names[train_labels[i]])
  plt.show()
  ```

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200322202909129.png" alt="image-20200322202909129" style="zoom:50%;" />



### 모델 구성

신경망 모델을 만들려면 모델의 층을 구성한 다음 모델을 컴파일 함



### 층 설정

* 신경망의 기본 구성 요소는 층(layer)임. 층은 주입된 데이터에서 표현(representation)을 추출함. 

* 대부분의 딥러닝은 간단한 층을 연결하여 구성됨. `tf.keras.layers.Dense` 와 같은 층들의 가중치는 훈련하는 동안 학습됨

  ```python
  model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),	# 28x28 행렬 데이터를 한 줄로 나열
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(10, activation = 'softmax')	# 마지막에 10개 들어가는 숫자들의 합이 1이 되도록(확률 분포)
  ])
  ```

  * 이 네트워크의 첫 번째 층인 `tf.keras.layers.Flatten` 은 2차원 배열(28x28 픽셀) 의 이미지 포맷을 28*28 =784 픽셀의 1차원 배열로 변환함. 이 층은 이미지에 있는 픽셀의 행을 펼쳐서 일렬로 늘림. 이 층은 학습되는 가중치가 없고 데이터를 변환하기만 함.

  * 픽셀을 펼친 후에는 두 개의 `tf,keras.layers.Dense` 층을 연속되어 연결됨.  이 층을 밀집 연결 또는 완전 연결층이라 부름. 첫 번째 `Dense` 층은 128개의 노드(뉴런)를 가짐. 두 번째 층은 10개의 노드의 `softmax` 층임. 이 층은 10개의 확률을 반환하고 반환된 값의 전체 합은 1임. 각 노드는 현재 이미지가 10개 클래스 중 하나에 속할 확률을 출력함.



### 모델 컴파일

모델을 훈련하기 전에 필요한 몇 가지 설정이 *컴파일*  단계에서 추가됨

* **손실함수(Loss Function)** 훈련하는 동안 모델의 오차를 측정함. 모델의 학습이 올바른 방향으로 향하도록 이 함수를 최소화 해야함.
* **옵티마이저(Optimize)** 데이터와 손실 함수를 바탕으로 모델의업데이트 방법을 결정함.
* **지표(Metrics)** 훈련 단계와 테스트 단계를 모니터링 하기 위해 사용함. 여기서는 올바르게 분류된 이미지의 비율인 **정확도**를 사용함

```python
model.compile(optimizer='adam',	# 일반적으로 성능이 가장 좋음
              loss='sparse_categorical_crossentropy',	# 예측과 정답을 CEE로
              metrics=['accuracy'])	# 직관적인 평가 지표
```



### 모델 훈련

* 신경망 모델을 훈련하는 단계
  1. 훈련 데이터를 모델에 주입함. 여기서는 `train_images`와 `train_labels` 배열임
  2. 모델이 이미지와 레이블을 매핑하는 방법을 배움
  3. 테스트 세트에 대한 모델의 예측을 만듬. 여기서는 `test_images` 배열. 이 예측이 `test_labels` 배열의 레이블과 맞는지 확인함
* 훈련을 시작하기 위해 `model.fit` 메서드를 호출하면 모델이 훈련 데이터를 학습함
  * 모델이 훈련되면서 손실과 정확도 지표가 출력됨. 이 모델은 훈련 세트에서 약 0.88(88%)의 정확도를 달성함.

```python
model.fit(train_images, train_labels, epochs=5)	# 학습 시킴. epochs은 학습 횟수
```

<img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200323233428878.png" alt="image-20200323233428878" style="zoom:50%;" />



### 정확도 평가

```python
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\n테스트 정확도:', test_acc)
```

* 테스트 세트의 정확도가 훈련 세트의 정확도보다 조금 낮음. 이는 **과적합(overfiting)** 때문임. 과적합은 머신러닝 모델이 훈련 데이터보다 새로운 데이터에서 성능이 낮아지는 현상을 말함.



### 예측 만들기 1

* 훈련된 모델을 사용해서 이미지에 대한 예측을 만들자.

* 먼저 **테스트 세트**에 있는 각 이미지의 레이블을 예측한다.

  ```python
  predictions = model.predict(test_images)
  predictions[0]
  
  # array([3.4482646e-06, 4.1379584e-09, 4.4699373e-08, 5.8572351e-09,
  #        8.5153900e-08, 3.8340772e-03, 1.4574939e-06, 1.2962911e-02,
  #        2.8518116e-06, 9.8319513e-01], dtype=float32)
  ```

  * 첫 번째 예측을 했음. 10개의 숫자 배열로 나타남. 이 값은 10개의 옷 품목에 상응하는 모델의 신뢰도(confidence)를 나타냄.

  

* 가장 높은 신뢰도를 가진 레이블을 보자.

  ```python
  np.argmax(predictions[0])
  
  test_labels[0]
  # 9
  # 9
  ```

  * 모델은 이미지가 앵클 부츠(`class_name[9]`)  라고 확신하고 있음

  * 실제 테스트 레이블을 확인해보니 9가 맞음

    

* 10개 클래스에 대한 예측을 모두 그래프로 구현해보자.

  ```python
  def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
  
    plt.imshow(img, cmap=plt.cm.binary)
  
    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:	# 맞으면
      color = 'blue'
    else:
      color = 'red'
  
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                  100*np.max(predictions_array),
                                  class_names[true_label]),
                                  color=color)
  
  def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)
  
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
  ```

  

* 0 번째 원소의 이미지, 예측, 신뢰도 점수를 확인해보자

  ```python
  i = 0
  plt.figure(figsize=(6,3))
  plt.subplot(1,2,1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(1,2,2)
  plot_value_array(i, predictions,  test_labels)
  plt.show()
  ```

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200323234855765.png" alt="image-20200323234855765" style="zoom:50%;" />

  

* 이미지 여러개를 예측하고 출력해보자.

  ```python
  # 처음 X 개의 테스트 이미지와 예측 레이블, 진짜 레이블을 출력합니다
  # 올바른 예측은 파랑색으로 잘못된 예측은 빨강색으로 나타냅니다
  num_rows = 5
  num_cols = 3
  num_images = num_rows*num_cols
  plt.figure(figsize=(2*2*num_cols, 2*num_rows))
  for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions, test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions, test_labels)
  plt.show()
  ```

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200323235206969.png" alt="image-20200323235206969" style="zoom:50%;" />



### 예측 만들기 2

* 마지막으로 훈련된 모델을 사용해서 한 이미지에 대한 예측을 만든다.

  ```python
  # 테스트 세트에서 이미지 하나를 선택합니다
  img = test_images[0]
  
  print(img.shape)
  # (28, 28)
  ```



* `tf.keras` 모델은 한 번의 샘플의 묶음 또는 **배치(batch)** 로 예측을 만드는데 최적화 되어있음. 하나의 이미지를 사용할 때도 2차원 배열로 만들어야 함

  ```python
  # 이미지 하나만 사용할 때도 배치에 추가합니다
  img = (np.expand_dims(img,0))
  
  print(img.shape)
  # (1, 28, 28)
  ```

  

* 이제 이 이미지의 예측을 만든다.

  ```python
  predictions_single = model.predict(img)
  
  print(predictions_single)
  
  plot_value_array(0, predictions_single, test_labels)
  _ = plt.xticks(range(10), class_names, rotation=45)
  ```

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200324001310543.png" alt="image-20200324001310543" style="zoom:50%;" />

  ```python
  np.argmax(predictions_single[0])
  
  # 9
  ```

  * 이전과 마찬가지로 모델의 예측은 9임.

