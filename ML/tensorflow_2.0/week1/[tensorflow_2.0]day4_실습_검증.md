# 실습 - 검증

[구글 텐서플로우 첫 걸음 실습 정리 문서](https://developers.google.com/machine-learning/crash-course/validation/another-partition)

[TOC]

### 학습 목표

* 단일 특성이 아닌 여러 특성을 사용하여 모델의 효과를 더욱 높임
* 모델 입력 데이터의 문제를 디버깅함
* 테스트 데이터 세트를 사용하여 모델이 검증 데이터에 과적합 되었는지 확인함



### 설정

```python
from __future__ import print_function

import math

from IPython import display
from matplotlib import cm
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

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

# california_housing_dataframe = california_housing_dataframe.reindex(
#     np.random.permutation(california_housing_dataframe.index))
```

```python
def preprocess_features(california_housing_dataframe):
  """Prepares input features from California housing data set.

  Args:
    california_housing_dataframe: A Pandas DataFrame expected to contain data
      from the California housing data set.
  Returns:
    A DataFrame that contains the features to be used for the model, including
    synthetic features.
  """
  selected_features = california_housing_dataframe[
    ["latitude",
     "longitude",
     "housing_median_age",
     "total_rooms",
     "total_bedrooms",
     "population",
     "households",
     "median_income"]]
  processed_features = selected_features.copy()
  # Create a synthetic feature.
  processed_features["rooms_per_person"] = (
    california_housing_dataframe["total_rooms"] /
    california_housing_dataframe["population"])
  return processed_features

def preprocess_targets(california_housing_dataframe):
  """Prepares target features (i.e., labels) from California housing data set.

  Args:
    california_housing_dataframe: A Pandas DataFrame expected to contain data
      from the California housing data set.
  Returns:
    A DataFrame that contains the target feature.
  """
  output_targets = pd.DataFrame()
  # Scale the target to be in units of thousands of dollars.
  output_targets["median_house_value"] = (
    california_housing_dataframe["median_house_value"] / 1000.0)
  return output_targets
```

* 특성을 전처리하는 로직을 모듈화했다. `rooms_per_person` 피쳐를 추가했음.



```python
training_examples = preprocess_features(california_housing_dataframe.head(12000))
training_examples.describe()
```

<img src="https://user-images.githubusercontent.com/46865281/76846849-8126d900-6884-11ea-8ad2-c234c34f3228.png" alt="image" style="zoom:50%;" />

```python
training_targets = preprocess_targets(california_housing_dataframe.head(12000))
training_targets.describe()
```

<img src="https://user-images.githubusercontent.com/46865281/76846937-a582b580-6884-11ea-81a5-fb513285ab09.png" alt="image" style="zoom:50%;" />

* **학습 세트**로 17,000개 예 중에서 처음 12,000개를 선택함



```python
validation_examples = preprocess_features(california_housing_dataframe.tail(5000))
validation_examples.describe()
```

<img src="https://user-images.githubusercontent.com/46865281/76847060-d2cf6380-6884-11ea-8ab9-2c10900d3f16.png" alt="image" style="zoom:50%;" />

```python
validation_targets = preprocess_targets(california_housing_dataframe.tail(5000))
validation_targets.describe()
```

<img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200317192426364.png" alt="image-20200317192426364" style="zoom:50%;" />

* **검증 세트**로 17,000개 예 중 마지막 5,000개를 선택함



### 작업 1: 데이터 조사

* 위 데이터들로부터 다음과 같은 의문점을 발견할 수 있다.
  1. `median_income`의 척도가 약 3~15 사이인데 그 의미가 불분명함. 일종의 로그 척도로 보이나 별도 설명된 곳이 없음.
  2. `median_house_value` 의 최댓값은 500,001로 인위적인 한도로 보임
  3. `rooms_per_person` 특성의 척도는 상식에 부합한다. 하지만 75번 째 백분위 수 값이 2인데 비해 18이나 55 같은 매우 큰 값이 보인다. 이는 데이터 손상의 증거일 수 있음



### 작업 2: 위도/경도와 주택 가격 중앙값을 비교하여 도식화

```python
plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
ax.set_title("Validation Data")

ax.set_autoscaley_on(False)
ax.set_ylim([32, 43])
ax.set_autoscalex_on(False)
ax.set_xlim([-126, -112])
plt.scatter(validation_examples["longitude"],
            validation_examples["latitude"],
            cmap="coolwarm",
            c=validation_targets["median_house_value"] / validation_targets["median_house_value"].max())

ax = plt.subplot(1,2,2)
ax.set_title("Training Data")

ax.set_autoscaley_on(False)
ax.set_ylim([32, 43])
ax.set_autoscalex_on(False)
ax.set_xlim([-126, -112])
plt.scatter(training_examples["longitude"],
            training_examples["latitude"],
            cmap="coolwarm",
            c=training_targets["median_house_value"] / training_targets["median_house_value"].max())
_ = plt.plot()
```

<img src="https://user-images.githubusercontent.com/46865281/76849429-bdf4cf00-6888-11ea-84f3-bc9dff5c88d4.png" alt="image" style="zoom:50%;" />

* `latitude`와 `longitude` 라는 두 특성을 도식화하고 `median_house_value` 를 색상으로 표현했다.
* 정상적으로 기대되는 결과는 캘리포니아주 지도가 그려지면서 샌프란시스코, 로스앤젤레스 같이 주택 가격이 높은 지역이 붉게 표현되는 것이다. 실제 지도와 비교해봤을 때, 학습 세트는 어느 정도 기대에 부합하지만 검증 세트는 그렇지 않음

* 중요한 점은 특성 혹은 열의 종류에 관계없이 **학습 세트와 검증 세트에서 값의 분포가 대략적으로 같아야 한다는 점**이다. 값의 분포가 다르다면 이는 심각한 문제임. 학습 세트와 검증 세트를 만드는 방법을 다시 살펴봐야 함



### 작업 3: 데이터 가져오기 및 전처리 코드로 돌아가서 버그가 있는지 확인

* 데이터를 읽을  무작위로 섞는 부분. 학습 세트와 검증 세트를 만들 때 적절히 섞여있지 않으면, 즉 데이터가 어떤 규칙으로 정렬되어 있으면 안 됨. 이 부분에서 문제가 발생한 것으로 보임

* **ML의 디버깅은 코드 디버깅이 아닌 데이터 디버깅인 경우가 많음**

  

### 작업 4: 모델 학습 및 평가

```python
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """Trains a linear regression model of multiple features.
  
    Args:
      features: pandas DataFrame of features
      targets: pandas DataFrame of targets
      batch_size: Size of batches to be passed to the model
      shuffle: True or False. Whether to shuffle the data.
      num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
    Returns:
      Tuple of (features, labels) for next data batch
    """
    
    # Convert pandas data into a dict of np arrays.
    features = {key:np.array(value) for key,value in dict(features).items()}                                           
 
    # Construct a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features,targets)) # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)
    
    # Shuffle the data, if specified.
    if shuffle:
      ds = ds.shuffle(10000)
    
    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels
```

```python
def construct_feature_columns(input_features):
  """Construct the TensorFlow Feature Columns.

  Args:
    input_features: The names of the numerical input features to use.
  Returns:
    A set of feature columns
  """ 
  return set([tf.feature_column.numeric_column(my_feature)
              for my_feature in input_features])
```

* 이전 실습에서 쓰였던 입력 함수를 정의하고, 여러 특성 열을 구성하는 코드를 모듈화해서 정의했다.



```python
def train_model(
    learning_rate,
    steps,
    batch_size,
    training_examples,
    training_targets,
    validation_examples,
    validation_targets):
  """Trains a linear regression model of multiple features.
  
  In addition to training, this function also prints training progress information,
  as well as a plot of the training and validation loss over time.
  
  Args:
    learning_rate: A `float`, the learning rate.
    steps: A non-zero `int`, the total number of training steps. A training step
      consists of a forward and backward pass using a single batch.
    batch_size: A non-zero `int`, the batch size.
    training_examples: A `DataFrame` containing one or more columns from
      `california_housing_dataframe` to use as input features for training.
    training_targets: A `DataFrame` containing exactly one column from
      `california_housing_dataframe` to use as target for training.
    validation_examples: A `DataFrame` containing one or more columns from
      `california_housing_dataframe` to use as input features for validation.
    validation_targets: A `DataFrame` containing exactly one column from
      `california_housing_dataframe` to use as target for validation.
      
  Returns:
    A `LinearRegressor` object trained on the training data.
  """

  periods = 10
  steps_per_period = steps / periods
  
  # Create a linear regressor object.
  my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
  my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
  linear_regressor = tf.estimator.LinearRegressor(
      feature_columns=construct_feature_columns(training_examples),
      optimizer=my_optimizer
  )
  
  # 1. Create input functions.
  training_input_fn = lambda: my_input_fn(
      training_examples, 
      training_targets["median_house_value"], 
      batch_size=batch_size)
  predict_training_input_fn = lambda: my_input_fn(
      training_examples, 
      training_targets["median_house_value"], 
      num_epochs=1, 
      shuffle=False)
  predict_validation_input_fn = lambda: my_input_fn(
      validation_examples, validation_targets["median_house_value"], 
      num_epochs=1, 
      shuffle=False)

  # Train the model, but do so inside a loop so that we can periodically assess
  # loss metrics.
  print("Training model...")
  print("RMSE (on training data):")
  training_rmse = []
  validation_rmse = []
  
  for period in range (0, periods):
    
    # 2-1. 학습 데이터로 모델 학습 시킴
    linear_regressor.train(
        input_fn=training_input_fn,
        steps=steps_per_period,
    )
    # 2-2. 학습 데이터, 검증 데이터로 모델 평가함.
    training_predictions = linear_regressor.predict(input_fn=predict_training_input_fn)
    training_predictions = np.array([item['predictions'][0] for item in training_predictions])
    
    validation_predictions = linear_regressor.predict(input_fn=predict_validation_input_fn)
    validation_predictions = np.array([item['predictions'][0] for item in validation_predictions])
    
    # 3. 손실 계산
    training_root_mean_squared_error = math.sqrt(
        metrics.mean_squared_error(training_predictions, training_targets))
    validation_root_mean_squared_error = math.sqrt(
        metrics.mean_squared_error(validation_predictions, validation_targets))
    # Occasionally print the current loss.
    print("  period %02d : %0.2f" % (period, training_root_mean_squared_error))
    # Add the loss metrics from this period to our list.
    training_rmse.append(training_root_mean_squared_error)
    validation_rmse.append(validation_root_mean_squared_error)
    
    
  print("Model training finished.")

  # Output a graph of loss metrics over periods.
  plt.ylabel("RMSE")
  plt.xlabel("Periods")
  plt.title("Root Mean Squared Error vs. Periods")
  plt.tight_layout()
  plt.plot(training_rmse, label="training")
  plt.plot(validation_rmse, label="validation")
  plt.legend()

  return linear_regressor
```

<img src="https://user-images.githubusercontent.com/46865281/76857185-49299100-6898-11ea-993b-6e1ed7e6496f.png" alt="image" style="zoom:50%;" />

1. 입력 함수를 선언했다. 위에서 정의한 학습, 검증 데이터를 입력 함수에 넣어줬다.
2. 모델 학습시킴 그후 학습 데이터, 검증 데이터로 모델을 평가함

3. 각각 RMSE을 계산한 뒤 `training_rmse`, `validation_rmse` 에 추가한다.

* 학습 데이터와 검증 데이터  결과를 비교함
* 위에서 보이듯 검증 데이터에서도 RMSE가 180 수준으로 내려온 것을 볼 수 있음



### 작업 5: 테스트 데이터로 평가

```python
california_housing_test_data = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_test.csv", sep=",")

test_examples = preprocess_features(california_housing_test_data)
test_targets = preprocess_targets(california_housing_test_data)

predict_test_input_fn = lambda: my_input_fn(
      test_examples, 
      test_targets["median_house_value"], 
      num_epochs=1, 
      shuffle=False)

test_predictions = linear_regressor.predict(input_fn=predict_test_input_fn)
test_predictions = np.array([item['predictions'][0] for item in test_predictions])

root_mean_squared_error = math.sqrt(
    metrics.mean_squared_error(test_predictions, test_targets))

print("Final RMSE (on test data): %0.2f" % root_mean_squared_error)
```

``` python
# 출력 결과
Final RMSE (on test data): 160.72
```

* 테스트 세트 평가로 과적합이 발생하지 않았나 판단해야 함.
* 결과를 보면 모델의 일반화 성능이 우수함을 확인할 수 있음.