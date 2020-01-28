# 파이썬으로 코딩 테스트

## 0. 개요

파이썬으로 코딩테스트를 볼 때 유용하거나 주의해야할 부분들을 정리함



## 1. 이런 점은 유용하다

* map을 활용해서 여러 변수들을 캐스팅하여 입력받기

  ```python
  i, j, k = map(int, input().split())
  ```

  ```
  tempList = list(map(int, input().split()))
  ```



* List comprehension 적절히 사용하기

  ```python
  maze = [list(map(int, input().split())) for _ in range(3)]
  
  #1 2 3
  #4 5 6
  #7 8 9 입력
  >>> maze
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  ```



* format, enumerate 활용하기

  ```python
  for testCase,result in enumerate(rstList):
      print("#{} {}".format(testCase+1,result))
  ```



- [ ] set 활용하기





## 2. 이런 점은 주의하자

- [ ] 