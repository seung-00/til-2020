# feature(variable) selection

## 개요

* 많은 특성이 모델의 설명력을 보장해주지 않는다.
* 특성이 추가될 수록 모델은 복잡해지고, 과적합의 위험은 높아진다.
* 가장 좋은 모델은 가장 적은 수의 독립 변수로 종속 변수를 설명할 수 있는 모델이다.
* 따라서 많은 feature가 주어졌을 때, 최적의 성능을 낼 수 있는 feature 조합을 골라야 한다.



##  방법론

0. 기본적으로 모든 조합을 따져볼 시 2^n 만큼의 비교를 해야한다. 이를 방지하기 방법론들이 존재한다.
1. Filter Method
   * 통계적 기법으로 학습 알고리즘에 상관 없이 전처리 과정에서 feature selection 진행, 
2. Wrapper Method
   * 평가 모델에 넣었다 뺐다하면서 부분 집합을 찾는 방법, 위 아래 방법들보다 비용이 많이 들겠지?

3. Embeded Method
   * 학습되는 모델 자체적으로 feature selection을 진행



## 1. Filter Method

* 다음과 같은 방법론들이 존재한다.
  * Pearson Correlation
  * chi-square test
  * fisher score
  * variance threshold
  * information gain

* 예컨대, chi-square test로 타겟과 feature 간의 독립성을 검정한 뒤 p-val 값으로 연관이 있는지(유의한 feature인지) 판단하는 식



## 2. Wrapper Methods

* 다음과 같은 방법론들이 존재한다.

  * Foward selection
  * Backward selection
  * Stepwise selection
  * genetic algorithm

* 가장 간단한 Foward selection의 경우 feature를 하나도 선택하지 않은 모델에서(절편만 있는 모델, 영모델) feature들을 하나씩 추가하면서 AIC 같은 기준으로 성능을 측정해 최적의 부분집합을 찾는 방식이다.

  

## 3. Embeded Method

* 회귀 모델에서의 Ridge, Lasso, Elastic net 의사결정나무에서의 Random Forest와 같은 방법론들이 존재함.
* [L1, L2 Norm]([https://github.com/young-o/TIL/blob/master/ML/machine_learning_basic/%EC%9D%B4%EB%A1%A0/%5BML_basic%5DL1_L2_regularization.md](https://github.com/young-o/TIL/blob/master/ML/machine_learning_basic/이론/[ML_basic]L1_L2_regularization.md)) 방식이 적용된 회귀 모델인 Ridge와 Lasso가 대표적