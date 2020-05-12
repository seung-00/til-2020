[김성법 교수님의 영상](https://www.youtube.com/watch?v=l_8XEj2_9rk&list=PLz2mnAqrQ4J7KIXHRFylz3MUomid4sG0z&index=5&t=886s)을 참고했습니다.



# 심플한 로지스틱 회귀분석

## 선형 회귀 vs 로지스틱 회귀

* 회귀분석이란, 독립 변수들과 종속 변수의 관계를 통해 모형을 그리는 분석 방법이다.
* 선형 회귀와 다르게 로지스틱 회귀 모델은 **분류**를 위한 모델이다.



## 분류를 위한 로지스틱 회귀

* 분류를 하기 위함이라 함은, 연속형이 아니라 범주형 종속 변수를 갖는다는 말이다.

*  예를 들어, 한 달간 야식을 먹은 횟수로 대상이 비만 위험군인지 아닌지를 예측한다고 해보자. 이 분석은 분류에 속한다.

  <img src="https://user-images.githubusercontent.com/46865281/80453642-a4ed3c80-8963-11ea-8651-b5ce82031f9a.png" alt="image" style="zoom:30%;" />

  * 분석의 목표는 위 그림처럼 어떤 함수에 x(야식 먹은 횟수)를 넣어 yes or no를 얻는 것이다.

    <img src="https://user-images.githubusercontent.com/46865281/80453756-dcf47f80-8963-11ea-9743-878372fa50f7.png" alt="image" style="zoom:33%;" />

  * 위 그림처럼, 이를 위해서 특정 데이터의 분포를 넣어서 예측 모델을 만들어야 할 것이다.

    <img src="https://user-images.githubusercontent.com/46865281/80455319-7cb30d00-8966-11ea-8554-69720541c6bf.png" alt="image" style="zoom:20%;" />

  * Linear Regression은 이런 분류가 어렵다. 

    위 그림처럼, 0과 1 사이의 범위를 가지지도 않고 예측 선이 분포를 잘 설명해주지도 않는다.

    애초에 범주형 종속변수는 정규분포(평균 0)를 따르지 않으므로 회귀분석의 가정에 위배됨

    <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200428154120904.png" alt="image-20200428154120904" style="zoom:25%;" />

  * Logistic Regression은 그림처럼 0과 1사이의 곡선으로 예측을 해서 그런 문제들을 해결한다.

  

* 회귀분석식은 결국 `y= ax + b` 와 같은 식일 뿐인데 어떻게 이것이 가능할까?

  * 이를 설명하기 위해서 sigmoid 함수와 odd ratio에 대한 이해가 필요하다.



## 로지스틱 회귀 모델 이해

* X값이 주어졌을 때 Y가 1을 가질 확률
  $$
  \begin{align}
  &Y_i=\beta_0+\beta_1X_i+\epsilon_i,\ 이때\ Y_i=1\ or\ 0\\
  &P(Y_i=1)=\pi_i,\ P(Y_i=0)=1-\pi_i \ (*베르누이\ 확률변수)\\
  \end{align}
  $$
  
  $$
  따라서\  X값이\ 주어졌을\ 때\ Y가\ 1을\ 가질\ 확률은 \\
  \begin{align}
  E(Y_i)& = \beta_0+\beta_1X_i\\
  &= 1*\pi_i+0*(1-\pi_i)\\ 
  &=\pi_i
  \end{align}
  $$
  

### 시그모이드 함수(로지스틱 함수)

  * 시그모이드
    $$
    sigmoid(x)=\frac{1}{1+e^{-x}}
    $$

    * x를 0과 1 사이의 확률 값으로 압축해서 출력시켜 줌

      

  * 로지스틱 회귀에서 사용

    <img src="https://user-images.githubusercontent.com/46865281/80458924-8e97ae80-896c-11ea-8738-f4c8a19d9c27.png" alt="image" style="zoom:15%;" />

    * 선형 회귀식을 넣음

  

  * 시그모이드는 미분 결과가 간결하다는 특징이 있음
    $$
    \begin{align}
    \frac{d}{dz}sigmoid(z) & = \frac{d}{dz}{(1+e^{-z})^{-1}} \\ 
    & ...\\
    & = sigmoid(z)(1-sigmoid(z))
    \end{align}
    $$
    

    * ​	초기 뉴럴넷 gradient descent 에서 시그모이드가 많이 쓰인 이유 중 하나임

      

* 단순 로지스틱 회귀 모델
  $$
  관측치\ x가\ 범주1에\ 속할\ 확률  \\
  \begin{align}
  E(Y_i)& = \pi(X=x) \\
  &= \frac{1}{1+e^{-(\beta_0+\beta_1x)}}
  \end{align}
  $$
  * beta의 해석이 직관적이지 못함 -> odd를 활용



### Odds(승산)

* Odds는 로지스틱 회귀모델의 파라미터 추정을 직관적으로 하기 위해 쓰인다. 

* 성공 확률을 p라 하자, 그때의 Odds(승산)는 실패 대비 성공 확률의 비율이다.
  $$
  Odds = \frac{p}{1-p}
  $$
  * 만약 p =1 이라면, odds는 발산하고 p=0이라면 0이 된다.

* 로지스틱 회귀에서의 Odds

  * 범주 0에 속할 확률 대비 범주 1에 속할 확률

  $$
  Odds = \frac{\pi(X=x)}{1-\pi(X=x)}
  $$

  * Logit Transform(로짓 변환)
    $$
    \begin{align}
    log(Odds)& = log(\frac{\pi(X=x)}{1-\pi(X=x)})\\
    & ...\\
    & =\beta_0+\beta_1x
    \end{align}
    $$

    * beta에 대한 해석이 직관적으로 변했음
      * 예컨대, x가 증가하면 log(Odds)가 선형으로 증가 

