# 실습 - 표현

[구글 텐서플로우 첫 걸음 실습 정리 문서](https://developers.google.com/machine-learning/crash-course/representation/programming-exercise)

[toc]

### 학습 목표

* 지난 실습에서는 모델에 모든 특성을 넣었음
* 그러나 모델에 포함된 특성이 적을수록 리소스 사용이 감소하며 유지보수도 쉬워짐
* 주택 관련 특성을 최소한으로 사용하며, 데이터 세트의 모든 특성을 사용하는 모델과 동등한 성능을 발휘하는 모델을 만들자.



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

california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
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

```python
# Choose the first 12000 (out of 17000) examples for training.
training_examples = preprocess_features(california_housing_dataframe.head(12000))
training_targets = preprocess_targets(california_housing_dataframe.head(12000))

# Choose the last 5000 (out of 17000) examples for validation.
validation_examples = preprocess_features(california_housing_dataframe.tail(5000))
validation_targets = preprocess_targets(california_housing_dataframe.tail(5000))

# Double-check that we've done the right thing.
print("Training examples summary:")
display.display(training_examples.describe())
print("Validation examples summary:")
display.display(validation_examples.describe())

print("Training targets summary:")
display.display(training_targets.describe())
print("Validation targets summary:")
display.display(validation_targets.describe())
```



### 작업1: 효율적인 특성 세트 개발

* **상관행렬**은 각 특성을 타겟과 비교한 결과 및 각 특성을 서로 비교한 결과에 따라 상관성을 보여줌.
* 여기서 상관성을 피어슨 상관계수(자주 쓰이는 상관계수)로 정의함
* 피어슨 상관계수 같은 경우, -1이면 완벽한 음의 상관성, +1이면 완벽한 양의 상관성, 0이면 상관성이 없음을 나타냄

```python
correlation_dataframe = training_examples.copy()
correlation_dataframe["target"] = training_targets["median_house_value"]

correlation_dataframe.corr()
```

<img src="https://user-images.githubusercontent.com/46865281/76971662-cfb1a180-6970-11ea-846c-4ac94d6723ae.png" alt="image" style="zoom:50%;" />

* 타겟과 상관성이 높은 특성을 찾아야 함.
* 또한 각 특성이 서로 독립적인 정보를 추가하돌고 서로간의 상관성이 높지 않은 특성을 찾는 것이 좋음

* `median_income` 과 `room_per_person`이 해당하는 값이므로 이를 가지고 학습을 해보자.

```python
minimal_features = [
  "median_income",
  "latitude",
]

minimal_training_examples = training_examples[minimal_features]
minimal_validation_examples = validation_examples[minimal_features]

_ = train_model(
    learning_rate=0.01,
    steps=500,
    batch_size=5,
    training_examples=minimal_training_examples,
    training_targets=training_targets,
    validation_examples=minimal_validation_examples,
    validation_targets=validation_targets)
```

<img src="https://user-images.githubusercontent.com/46865281/76972414-e86e8700-6971-11ea-94a6-a716339fbfbf.png" alt="image" style="zoom:50%;" />



### 작업2: 위도 활용 고도화

```python
plt.scatter(training_examples["latitude"], training_targets["median_house_value"])
```

<img src="https://user-images.githubusercontent.com/46865281/76972652-3d120200-6972-11ea-978e-5cf3c21125e4.png" alt="image" style="zoom:50%;" />

* `latitude`와 타겟은 선형관계가 없어 보이지만, 그래프를 그려보면 특정 부근에 기둥이 나타남을 알 수 있다. 이는 실제로 로스앤젤레스 및 샌프란시스코에 해당하는 위치 부근을 의미함

```python
# 1. 빈을 만들기 위한 튜플들
LATITUDE_RANGES = zip(range(32, 44), range(33, 45))

# 2. 위도를 빈으로 변환 후 피쳐로 추가한 데이터셋을 반환하는 함수
def select_and_transform_features(source_df):
  selected_examples = pd.DataFrame()
  selected_examples["median_income"] = source_df["median_income"]
  for r in LATITUDE_RANGES:
    selected_examples["latitude_%d_to_%d" % r] = source_df["latitude"].apply(
      lambda l: 1.0 if l >= r[0] and l < r[1] else 0.0)
  return selected_examples

selected_training_examples = select_and_transform_features(training_examples)
selected_validation_examples = select_and_transform_features(validation_examples)
print(selected_training_examples)
```

<img src="https://user-images.githubusercontent.com/46865281/76974199-41d7b580-6974-11ea-8ea1-95a69289d21e.png" alt="image" style="zoom:50%;" />

1. 위도를 버킷화하기 위해 튜플 만듬 (32, 33), (34, 35) ...
2. 데이터 셋에서 위도 데이터를 빈으로 나눈 뒤 각각을 새로운 데이터셋 피쳐로 넣어줬다.

```python
_ = train_model(
    learning_rate=0.01,
    steps=500,
    batch_size=5,
    training_examples=selected_training_examples,
    training_targets=training_targets,
    validation_examples=selected_validation_examples,
    validation_targets=validation_targets)
```



<img src="https://user-images.githubusercontent.com/46865281/76976751-bfe98b80-6977-11ea-8c04-9a6f12c352aa.png" alt="image" style="zoom:50%;" />

