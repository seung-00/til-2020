# 실습  - 합성 특성과 이상점

[구글 텐서플로우 첫 걸음 실습 정리 문서](https://colab.research.google.com/notebooks/mlcc/synthetic_features_and_outliers.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=syntheticfeatures-colab&hl=ko)

[TOC]

### 학습 목표

* 다른 두 특성의 비율로 합성 특성을 만든다
* 새 특성을 선형 회귀 모델의 입력으로 사용한다.
* 입력 데이터에서 이상점을 식별 및 삭제하여 모델의 효율성을 개선한다.



### 설정

```python
from __future__ import print_function

import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.metrics as metrics
%tensorflow_version 1.x
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0
california_housing_dataframe
```



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
    
    # Convert pandas data into a dict of np arrays.
    features = {key:np.array(value) for key,value in dict(features).items()}                                           
 
    # Construct a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features,targets)) # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)
    
    # Shuffle the data, if specified.
    if shuffle:
      ds = ds.shuffle(buffer_size=10000)
    
    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels
```

```python
def train_model(learning_rate, steps, batch_size, input_feature):
  """Trains a linear regression model.
  
  Args:
    learning_rate: A `float`, the learning rate.
    steps: A non-zero `int`, the total number of training steps. A training step
      consists of a forward and backward pass using a single batch.
    batch_size: A non-zero `int`, the batch size.
    input_feature: A `string` specifying a column from `california_housing_dataframe`
      to use as input feature.
      
  Returns:
    A Pandas `DataFrame` containing targets and the corresponding predictions done
    after training the model.
  """
  
  periods = 10
  steps_per_period = steps / periods

  my_feature = input_feature
  my_feature_data = california_housing_dataframe[[my_feature]].astype('float32')
  my_label = "median_house_value"
  targets = california_housing_dataframe[my_label].astype('float32')

  # Create input functions.
  training_input_fn = lambda: my_input_fn(my_feature_data, targets, batch_size=batch_size)
  predict_training_input_fn = lambda: my_input_fn(my_feature_data, targets, num_epochs=1, shuffle=False)
  
  # Create feature columns.
  feature_columns = [tf.feature_column.numeric_column(my_feature)]
    
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
        steps=steps_per_period,
    )
    # Take a break and compute predictions.
    predictions = linear_regressor.predict(input_fn=predict_training_input_fn)
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

  # Create a table with calibration data.
  calibration_data = pd.DataFrame()
  calibration_data["predictions"] = pd.Series(predictions)
  calibration_data["targets"] = pd.Series(targets)
  display.display(calibration_data.describe())

  print("Final RMSE (on training data): %0.2f" % root_mean_squared_error)
  
  return calibration_data
```

* 입력함수, 모델 학습용 함수를 정의함.



### 작업 1: 합성 특성 사용해보기

* `total_rooms` 특성과 `population` 특성은 모두 특정 지역의 합계를 계수함. 만약 지역마다 인구밀도가 다르다면 어떻게 해야할까? 두 특성의 비율로 합성 특성을 만들면 지역의 인구밀도와 주택 가격 중앙값(라벨)의 관계를 살펴볼 수 있을 것이다.

  ```python
  california_housing_dataframe["rooms_per_person"] = (
      california_housing_dataframe["total_rooms"] / california_housing_dataframe["population"])
  
  calibration_data = train_model(
      learning_rate=0.05,
      steps=500,
      batch_size=5,
      input_feature="rooms_per_person")
  ```

  ![image](https://user-images.githubusercontent.com/46865281/76699263-48a1c680-66ef-11ea-9bf2-b61be1ebb146.png)



* `rooms_per_person` 이라는 특성을 만들어서 모델에 전달한 후 학습시켰음



### 작업 2: 이상점 식별

```python
plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
plt.scatter(calibration_data["predictions"], calibration_data["targets"])
```

<img src="https://user-images.githubusercontent.com/46865281/76699459-fb265900-66f0-11ea-86be-e7699ca23ca3.png" alt="image" style="zoom:50%;" />

* Pyplot의 `scatter()` 로 산포도를 작성함. 몇 개의 이상점을 확인할 수 있음. 히스토그램으로도 확인해보자.

```python
plt.subplot(1, 2, 2)
_ = california_housing_dataframe["rooms_per_person"].hist()
```

<img src="https://user-images.githubusercontent.com/46865281/76699519-75ef7400-66f1-11ea-982c-c9923ec87286.png" alt="image" style="zoom:60%;" />



### 작업 3: 이상점 삭제

```python
california_housing_dataframe["rooms_per_person"] = (
    california_housing_dataframe["rooms_per_person"]).apply(lambda x: min(x, 5))

_ = california_housing_dataframe["rooms_per_person"].hist()
```

<img src="https://user-images.githubusercontent.com/46865281/76699576-1776c580-66f2-11ea-96f4-232721fd8a0d.png" alt="image" style="zoom:33%;" />

* 작업 2 히스토그램을 보면 대부분 값이 5 미만임. 5 아래로 잘라줬음

  

```python
calibration_data = train_model(
    learning_rate=0.05,
    steps=500,
    batch_size=5,
    input_feature="rooms_per_person")
```

```python
_ = plt.scatter(calibration_data["predictions"], calibration_data["targets"])
```

<img src="https://user-images.githubusercontent.com/46865281/76699622-a683dd80-66f2-11ea-8933-ac82f6c55474.png" alt="image" style="zoom:33%;" />

<img src="https://user-images.githubusercontent.com/46865281/76699674-332e9b80-66f3-11ea-95b6-e6e5a419fc91.png" alt="image" style="zoom:33%;" />



* 보정한 데이터들로 학습을 시키고, 예측 데이터들을 히스토그램으로 그렸다.

