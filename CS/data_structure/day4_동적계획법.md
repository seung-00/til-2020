## 메모이제이션

* 한 번 계산한 결과를 메모리에 저장해두고 꺼내 씀으로써 중복 계산을 피하는 방법이다. DP에 쓰임

* 중복 계산 예시: 피보나치 수열

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200114214639737.png" alt="image-20200114214639737" style="zoom:30%;" />

  예컨대 f(4) = f(1)+f(0)+f(1)+f(1)+f(0)으로 같은 값이 계속 중복된다.

* 메모이제이션을 적용한 피보나치 수열

  ```python
  def fibo(n):
    global memo
    if n>=2 and len(memo)<=n:
      memo.append(fibo(n-1) + fibo(n-2))
     return memo[n]
  	memo = [0, 1]
  ```

  

## 동적 계획법(DP)

* 크기가 작은 문제들은 모두 해결하고 그 해들을 이용해 보다 큰 크기의 문제들을 해결

  * 문제를 부분들로 나누고, 부분들의 해를 테이블에 저장한 후 이를 이용한다.

* 피보나치 수에 DP 적용

  ```python
  def fibo(n):
    f = [0, 1]
    for i in range(2, n+1):
      a.append(f[i-1]+f[i-2])
    return fibo[n]
  ```

