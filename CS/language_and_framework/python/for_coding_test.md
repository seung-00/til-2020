# 파이썬 코테 깨알 팁

파이썬으로 코딩테스트를 볼 때 유용하거나 주의해야할 깨알 문법들을 정리함



## 1. 입출력, 파라미터

* map을 활용해서 여러 변수들을 캐스팅하여 입력받기

  ```python
  i, j, k = map(int, input().split())
  ```

  ```
  tempList = list(map(int, input().split()))
  ```



* List comprehension 적절히 사용하기

  ```python
  #1 2 3
  #4 5 6
  #7 8 9 입력
  
  table1 = [input().split() for _ in range(3)]
  
  table2 = [list(map(int, input().split())) for _ in range(3)]
  
  #>>> table1
  #[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
  
  #>>> table2
  #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  
  #인접 행렬 만들기
  graph = [[0]*(V+1) for _ in range(V+1)]
  
  #>>> graph
  #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  ```
  
  

* 정답 출력 시 f-string, enumerate 활용하기

  ```python
  for testCase,result in enumerate(rstList):
      print(f"#{testCase+1} {result}")
  ```



* global, nonlocal 활용

  * global을 쓰면 지역변수가 전역변수에 영향을 줄 수 있다.

    ```python
    def DFS(start):
        global rst	# 지역변수 -> 전역변수
        #...
        rst = 1
    
    rst = 0
    DFS(0)
    print(rst)
    
    #1
    ```

  

  * nonlocal을 쓴 변수는 한단계 바깥쪽 함수의 변수와 바인딩 된다.

  * 전역변수에는 영향을 주지 않는다.

    ```python
    def Answer(start):
        rst = 0
        def DFS(start):
            nonlocal rst
            #...
            rst = 1
            print(rst)
        DFS(start)
        print(rst)
    
    rst = 0
    Answer(0)
    print(rst)
    
    #1
    #1
    #0
    ```

  

*  zip()

  ```python
  upperCase = ['A', 'B', 'C', 'D', 'E', 'F']
  lowerCase = ['a', 'b', 'c', 'd', 'e', 'f']
  for i, (upper, lower) in enumerate(zip(upperCase, lowerCase), 1):
      print(f'{i}: {upper} and {lower}.')
  # 1: A and a.
  # 2: B and b.
  # 3: C and c.
  # 4: D and d.
  # 5: E and e.
  # 6: F and f.
  
  출처: https://deepwelloper.tistory.com/143 [DEVLOG]
  ```



* 실행 시간 측정

  * time 모듈 활용

    ```python
    import time
    startTime = time.time()
    
    # code
    
    endTime = tiem.time()-startTime
    print(endTime)
    ```

  * 터미널에서 바로 확인

    ```
    $time python test.py
    ```

    

## 2. 이런 점은 주의하자

* 가변적인 변수(예컨대, 리스트)를 디폴트 파라미터로 주는 경우, 파이썬은 스태틱 변수처럼 사용한다.
  * 참고: https://onlywis.tistory.com/3

