# 전처리 -> 분할표 -> 독립성 검정 (python)



```python
from scipy import stats
import pandas as pd
data = pd.read_csv("국민건강영양조사(2018).csv")
target = pd.DataFrame()
target['HE_obe'], target['sex'], target['age'], target['incm'], target['BD1_11'], target['BP1'] = data['HE_obe'], data['sex'], data['age'], data['incm'], data['BD1_11'], data['BP1']
# df.column_name형식으로 쓰면 안 된다. 이런 방식은 기존에 존재하는 열을 불러올 땐 가능하지만 처음에 열을 생성하려면 무조건 df['column_name']으로 해야 한다. 

data = data['HE_obe'], data['sex']
data = data.dropna() #nan 제외
data.HE_obe = data.HE_obe.apply(lambda l: 1 if l >=3 else 0)	# 버켓팅
crosst = pd.crosstab(data.HE_obe,data.sex)
print(stats.chi2_contingency(crosst))

# 검정 통계량, p-value

```

* 이미 분할표가 있는 경우

```python
import padnas as pd

import numpy as np

from scipy import stats

#성

table =pd.DataFrame(np.array([[2250,469],[2906,545]]))

print(stats.chi2_contingency(table))

#연령

table =pd.DataFrame(np.array([[1266, 384],[1910, 417], [1980, 213] ]))

print(stats.chi2_contingency(table))

#경제상태

table =pd.DataFrame(np.array([[1266,270],[2553,527], [1318, 215] ]))

print(stats.chi2_contingency(table))

#음주빈도

table =pd.DataFrame(np.array([[2301,424],[1132,254], [1114, 268] ]))

print(stats.chi2_contingency(table))

#스트레스

table =pd.DataFrame(np.array([[1257,324],[2858,534], [992, 156]]))

print(stats.chi2_contingency(table))
```
