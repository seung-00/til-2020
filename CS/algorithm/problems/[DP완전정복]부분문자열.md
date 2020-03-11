DP 완전정복[^1]



### ch3 예제: 부분 문자열 다루기

> 숫자로 이루어진 문자열에서 부분 문자열 중 앞 부분 절반 숫자의 합과 뒷부분 절반 숫자의 합이 같은 부분 문자열 가운데 가장 긴 부분 문자열의 길이

* **입력 문자열**: 1412124

  * **출력**: 6

* **입력 문자열**: 9430723

  * **출력**:4

    

* 코드

  ```python
  def maxSubSpring(inputStr):
      n = len(inputStr)
      maxLen = 0
      sum = [[0]*n for _ in range(n)]
      
      for i in range(n):
          sum[i][i] = int(inputStr[i])    #subLen = 1 인 경우
      
      for subLen in range(2, n+1):
          for s in range(0, n-subLen+1):
              e = s+subLen-1
              p = subLen//2
              sum[s][e] = sum[s][e-p] + sum[e-p+1][e]
              if subLen%2 == 0 and sum[s][e-p] == sum[e-p+1][e] and subLen>maxLen:
                  maxLen = subLen
      
      return maxLen
  
  print(maxSubSpring("943072"))
  ```

  

* 생각

  <img src="https://user-images.githubusercontent.com/46865281/76407141-37df1100-63ce-11ea-84fc-3ebd97b67e04.png" alt="image" style="zoom:50%;" />

  

  * 위 그림과 같은 순환식을 가진다.

    내가 헷갈렸던 점은, 2차원 행렬에 값을 넣을때 단순히 행을 이동하는 것이 아니라, S[i, i] 라는 base case에 근접한 곳에서 먼 곳으로 이동해야 했다는 점이다. 따라서 반복문을 부분문자열 기준으로 돌도록 했다.



[^1]: https://github.com/crapas/dp

