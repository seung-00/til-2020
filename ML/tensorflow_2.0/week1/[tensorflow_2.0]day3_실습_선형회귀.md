# 실습  - 텐서플로우 첫걸음, 선형 회귀

[구글 텐서플로우 첫 걸음 실습 정리 문서](https://colab.research.google.com/notebooks/mlcc/synthetic_features_and_outliers.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=syntheticfeatures-colab&hl=ko)

[TOC]

### 학습 목표

* 텐서플로우의 기초 개념을 학습한다

* 텐서플로우의 `LinearRegressor` 클래스를 사용하여 입력 특성 하나를 기반으로 지역별 주택 가격 중앙값을 예측한다

* 평균 제곱근 오차(RMSE)를 사용하여 모델 예측의 정확성을 평가한다

* 초매개변수를 조정하여 모델의 정확성을 개선한다
* 데이터의 출처는 1990년 캘리포니아 인구조사 자료임.



### 설정

```python
#1. 첫 번째 셀에서 필요한 라이브러리 로드
from __future__ import print_function

import math

from IPython import display
from matplotlib import cma
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
%tensorflow_version 1.x
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

#2. 데이터 세트 로드
california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

#3. 확률적 경사하강법의 성능에 악영향을 줄 수 있는 의도치 않은 정렬 효과를 방지하고자 데이터를 무작위 추출.
#4. 일반적으로 사용하는 학습률 범위에서 학습할 수 있도록 median_house_val을 천 단위로 조정

california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0
california_housing_dataframe
```



3. 확률적 경사하강법(SGD)은 데이터 세트에서 example을 무작위로 고르게 하여 배치를 줄이는 방법이다. 반복당 1example을 선택하며 노이즈가 심한 방법이다.

   `DataFrame.reindex()` 는 색인을 기준으로 행의 순서를 재정렬한다. 이 코드에서 reindex 파라미터로 NumPy의 random.permutation 함수를 넣어서 인덱스를 섞도록 했다.

4. DataFrame은 기본적인 파이썬 연산을 지원한다. `col/=1000.0` 을 함으로써 해당 열 값들을 1000으로 나눠줬다.



### 첫 번째 모델 만들기

* 라벨은 타겟이라고도 한다. 이 실습에서 예측하고자 하는 라벨은 `median_hpuse_value` 이다. 입력 특성으로는 `totl_rooms` 가 쓰인다(해당 지역의 전체 방 수를 의미함). 
* 모델을 학습시키기 위해 tf.estimator API가 제공하는 LinearRegressor 인터페이스를 사용한다.



### 1단계: 특성 정의 및 특성 열 구성

```python
# Define the input feature: total_rooms.
my_feature = california_housing_dataframe[["total_rooms"]]

#1. total_rooms이라는 수치 데이터를 사용함
# Configure a numeric feature column for total_rooms.
feature_columns = [tf.feature_column.numeric_column("total_rooms")]
print(feature_columns)
```

* 학습 데이터를 텐서플로우로 가져오기 위해 각 특성에 들어있는 데이터 유형을 지정해야 함.
  * 범주형 데이터: 텍스트로 이루어진 데이터
  * 수치 데이터: 정수 또는 부동 소수점 숫자이며 숫자로 취급하려는 데이터

1. 특성의 데이터 유형을 지정하기 위해 `feature_colums` 라는 구조체를 사용함. 여기서 `numeric_colums` 으로 해당 데이터가 숫자임을 지정했음



### 2단계: 타겟 정의

 ```python
#타겟인 median_house_value를 정의함
targets = california_housing_dataframe["median_house_value"]
 ```



### 3단계: LinearRegressor 구성

```python
#1. 최적화 위해 경사하강법 사용
my_optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

#2. 선형 모델 구성
linear_regressor = tf.estimator.LinearRegressor(
    feature_columns=feature_columns,
    optimizer=my_optimizer
)
```

1. SGD를 구현하는 `GradientDescentOptimizer` 사용함 `learning_rate` 인수로 경사 단계의 크기를 조절함

   안전을 위해 옵티마이저에 `clip_gradients_by_norm()` 을 통해 경사 제한을 적용함. 경사 제한은 학습 중 경사가 너무 커져서 경사하강법이 실패하는 경우가 나타나지 않도록 제한함

2. tf.estimator의 LinearRegressor 사용



### 4단계: 입력 함수 정의

```python
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """Trains a linear regression model of one feature.
  
    Args:
      features: pandas DataFrame of features
      targets: pandas DataFrame of targets
      batch_size: Size of batches to be passed to the model
      shuffle: True or False. Whether to shuffle the data.
      num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
    Returns:
      Tuple of (features, labels) for next data batch
    """
  
    #1. pandas feature 데이터 -> Numpy dict로
    features = {key:np.array(value) for key,value in dict(features).items()}                                           
 
    #2. 데이터 셋을 만들고 배치 사이즈 크기로 나누어 지정한 만큼 반복
    ds = Dataset.from_tensor_slices((features,targets)) # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)
    
    #3. 데이터 셔플
    if shuffle:
      ds = ds.shuffle(buffer_size=10000)
    
    #4. Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels
```

* 데이터를 `LinearRegressor` 로 가져오기 위해 텐서플로우에 데이터 전처리 방법 및 모델 학습 중 일괄 처리, 셔플, 반복 방법을 알려주는 입력 함수를 정의해야 한다.

1. df.pandas 데이터를 np.dict 데이터로 바꾼다. my_feature이 들어갈텐데, my_feature은 행렬 명 total_rooms와 수치데이터들로 구성된 열이다. 이걸 컴프리헨션을 사용해 행렬 명을 키로 두고 수치데이터를 여기에 매핑시킨다.

2. 텐서플로우의 Dataset API를 이용해 데이터로부터 데이터 세트 객체를 만들고 입력받은 배치 사이즈대로 나눈다. 그리고 지정한 횟수(`num_epochs`) 만큼 반복한다.

3. 셔플에 True 값을 주었을 시, 학습 중 데이터가 모델에 무작위로 전달되도록 섞인다. 이때 `buffer_size` 인수는 셔플에서 무작위로 추출할 데이터 세트의 크기를 지정함. 셔플 함수는 고정된 버퍼 크기로 데이터를 섞는데, 데이터가 완전히 랜덤으로 섞이게 하기 위해 입력된 데이터 크기보다 큰 수를 입력해줘야 함.

4. `ds.make_one_shot_iterator()`은 tf.data.iterator를 생성한다. `Iterator.get_next() ` 은 다음 항목에 연결되어 있는 tf.Tensor 객체를 리턴한다. 



### 5단계: 모델 학습

```python
_ = linear_regressor.train(
    input_fn = lambda:my_input_fn(my_feature, targets),
    steps=100)
```

* `linear_regressor`로부터 train()을 호출하여 모델을 학습시킨다. 입력함수를 `lamda`에 매핑시켜 특성과 라벨을 전달하도록 한다. 100 step 진행



### 6단계: 모델 평가

```python
# Create an input function for predictions.
# Note: Since we're making just one prediction for each example, we don't 
# need to repeat or shuffle the data here.
prediction_input_fn =lambda: my_input_fn(my_feature, targets, num_epochs=1, shuffle=False)

# Call predict() on the linear_regressor to make predictions.
predictions = linear_regressor.predict(input_fn=prediction_input_fn)

# Format predictions as a NumPy array, so we can calculate error metrics.
predictions = np.array([item['predictions'][0] for item in predictions])

# Print Mean Squared Error and Root Mean Squared Error.
mean_squared_error = metrics.mean_squared_error(predictions, targets)
root_mean_squared_error = math.sqrt(mean_squared_error)
print("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
print("Root Mean Squared Error (on training data): %0.3f" % root_mean_squared_error)
```

```python
# 출력 결과
Mean Squared Error (on training data): 56367.025
Root Mean Squared Error (on training data): 237.417
```

* MSE는 해석하기가 어려울 수 있어서 평균 제곱근 오차(RMSE)를 대신 참고하는 경우가 많음. RMSE의 장점은 원래 타겟과 동일한 척도로 해석할 수 있다는 거임.



```python
min_house_value = california_housing_dataframe["median_house_value"].min()
max_house_value = california_housing_dataframe["median_house_value"].max()
min_max_difference = max_house_value - min_house_value

print("Min. Median House Value: %0.3f" % min_house_value)
print("Max. Median House Value: %0.3f" % max_house_value)
print("Difference between Min. and Max.: %0.3f" % min_max_difference)
print("Root Mean Squared Error: %0.3f" % root_mean_squared_error)
```

```python
# 출력 결과

Min. Median House Value: 14.999
Max. Median House Value: 500.001
Difference between Min. and Max.: 485.002
Root Mean Squared Error: 237.417
```

* RMSE를 타겟의 최대값 최소값 차와 비교해봤음. 오차 범위가 타겟 값 범위의 절반에 달하는 높은 수치임. 오차를 이보다 어떻게 줄일 수 있을지 생각해보자.



```python
calibration_data = pd.DataFrame()
calibration_data["predictions"] = pd.Series(predictions)
calibration_data["targets"] = pd.Series(targets)
calibration_data.describe()
```

<img src="https://user-images.githubusercontent.com/46865281/76698128-83e9c880-66e2-11ea-9fd4-22dec5c7741b.png" alt="image" style="zoom:45%;" />



* 가장 처음에 할 수 있는 일은 요약 통계를 참조하여 예측과 타겟의 일치율을 조사하는 것임



```python
# 1. 균일한 무작위 데이터 샘플을 추출함.
sample = california_housing_dataframe.sample(n=300)

# Get the min and max total_rooms values.
x_0 = sample["total_rooms"].min()
x_1 = sample["total_rooms"].max()

# Retrieve the final weight and bias generated during training.
weight = linear_regressor.get_variable_value('linear/linear_model/total_rooms/weights')[0]
bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

# Get the predicted median_house_values for the min and max total_rooms values.
y_0 = weight * x_0 + bias 
y_1 = weight * x_1 + bias

# Plot our regression line from (x_0, y_0) to (x_1, y_1).
plt.plot([x_0, x_1], [y_0, y_1], c='r')

# Label the graph axes.
plt.ylabel("median_house_value")
plt.xlabel("total_rooms")

# Plot a scatter plot from our data sample.
plt.scatter(sample["total_rooms"], sample["median_house_value"])

# Display graph.
plt.show()
```

<img src="https://user-images.githubusercontent.com/46865281/76698243-ebecde80-66e3-11ea-9624-9d6331e4f6ee.png" alt="image" style="zoom:45%;" />

* 이번에는 평균 값을 모델의 RMSE와 비교해보자. 선형회귀를 시각화한다.



### 모델 초매개변수 조정

```python
def train_model(learning_rate, steps, batch_size, input_feature="total_rooms"):
  """Trains a linear regression model of one feature.
  
  Args:
    learning_rate: A `float`, the learning rate.
    steps: A non-zero `int`, the total number of training steps. A training step
      consists of a forward and backward pass using a single batch.
    batch_size: A non-zero `int`, the batch size.
    input_feature: A `string` specifying a column from `california_housing_dataframe`
      to use as input feature.
  """
  
  periods = 10
  steps_per_period = steps / periods

  my_feature = input_feature
  my_feature_data = california_housing_dataframe[[my_feature]]
  my_label = "median_house_value"
  targets = california_housing_dataframe[my_label]

  # Create feature columns.
  feature_columns = [tf.feature_column.numeric_column(my_feature)]
  
  # Create input functions.
  training_input_fn = lambda:my_input_fn(my_feature_data, targets, batch_size=batch_size)
  prediction_input_fn = lambda: my_input_fn(my_feature_data, targets, num_epochs=1, shuffle=False)
  
  # Create a linear regressor object.
  my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
  my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
  linear_regressor = tf.estimator.LinearRegressor(
      feature_columns=feature_columns,
      optimizer=my_optimizer
  )

  # Set up to plot the state of our model's line each period.
  plt.figure(figsize=(15, 6))
  plt.subplot(1, 2, 1)
  plt.title("Learned Line by Period")
  plt.ylabel(my_label)
  plt.xlabel(my_feature)
  sample = california_housing_dataframe.sample(n=300)
  plt.scatter(sample[my_feature], sample[my_label])
  colors = [cm.coolwarm(x) for x in np.linspace(-1, 1, periods)]

  # Train the model, but do so inside a loop so that we can periodically assess
  # loss metrics.
  print("Training model...")
  print("RMSE (on training data):")
  root_mean_squared_errors = []
  for period in range (0, periods):
    # Train the model, starting from the prior state.
    linear_regressor.train(
        input_fn=training_input_fn,
        steps=steps_per_period
    )
    # Take a break and compute predictions.
    predictions = linear_regressor.predict(input_fn=prediction_input_fn)
    predictions = np.array([item['predictions'][0] for item in predictions])
    
    # Compute loss.
    root_mean_squared_error = math.sqrt(
        metrics.mean_squared_error(predictions, targets))
    # Occasionally print the current loss.
    print("  period %02d : %0.2f" % (period, root_mean_squared_error))
    # Add the loss metrics from this period to our list.
    root_mean_squared_errors.append(root_mean_squared_error)
    # Finally, track the weights and biases over time.
    # Apply some math to ensure that the data and line are plotted neatly.
    y_extents = np.array([0, sample[my_label].max()])
    
    weight = linear_regressor.get_variable_value('linear/linear_model/%s/weights' % input_feature)[0]
    bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

    x_extents = (y_extents - bias) / weight
    x_extents = np.maximum(np.minimum(x_extents,
                                      sample[my_feature].max()),
                           sample[my_feature].min())
    y_extents = weight * x_extents + bias
    plt.plot(x_extents, y_extents, color=colors[period]) 
  print("Model training finished.")

  # Output a graph of loss metrics over periods.
  plt.subplot(1, 2, 2)
  plt.ylabel('RMSE')
  plt.xlabel('Periods')
  plt.title("Root Mean Squared Error vs. Periods")
  plt.tight_layout()
  plt.plot(root_mean_squared_errors)

  # Output a table with calibration data.
  calibration_data = pd.DataFrame()
  calibration_data["predictions"] = pd.Series(predictions)
  calibration_data["targets"] = pd.Series(targets)
  display.display(calibration_data.describe())

  print("Final RMSE (on training data): %0.2f" % root_mean_squared_error)
```

* 편의를 위해 위 코드들의 기능을 단일 함수에 넣었음.

  

### 작업 1: 180 이하의 RMSE 달성

```python
train_model(
    learning_rate=0.00001,
    steps=100,
    batch_size=1
)
```

![image](https://user-images.githubusercontent.com/46865281/76698494-d927d900-66e6-11ea-95d5-857e75275dd3.png)

* 위 코드대로 학습 시켰을 때 RMSE가 180을 초과하게 나온다. 180을 초과하게 하는 코드는 다음과 같다.

  

```python
train_model(
    learning_rate=0.00002,
    steps=500,
    batch_size=5
)
```

![image](https://user-images.githubusercontent.com/46865281/76698555-bf3ac600-66e7-11ea-9876-6b7fbbf2190c.png)



### 모델 조정에 대한 표준 휴리스틱이 있는가?

* 분명한 규칙은 없지만 참고할 만한 몇 가지 경험칙이 있음
  * 학습 오차는 점차 감소함. 처음에 급격히 감소하다가 학습이 수렴됨에 따라 한계에 이름
  * 학습이 수렴되지 않았다면 더 오래 실행해는 것이 좋음
  * 학습 오차가 너무 천천히 감소하는 경우 학습률을 높이면 빨리 감소함
    * 학습률이 너무 높다면, 반대 현상이 나타나기도 함
  * 학습 오차가 크게 요동한다면 학습률을 낮춰 보셈
    * 학습률을 낮추면서 단계 수 혹은 배치 크기를 늘리면 좋은 결과가 나타나는 경우가 많음
  * 배치 크기가 너무 작아도 불안정성이 나타날 수 있음. 처음에는 100, 1000 등 큰 값을 사용한 후 성능이 악화되지 않는 선까지 낮춤
* 효과는 어디까지 데이터에 따라 달라지므로 이러한 경험칙을 무조건 따라가면 안 되며, 실험과 검증을 반복해야 함.

