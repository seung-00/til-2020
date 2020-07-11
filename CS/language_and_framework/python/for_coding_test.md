# 파이썬 코테 깨알 팁

파이썬으로 코딩테스트를 볼 때 유용하거나 주의해야할 깨알 문법들을 정리함



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

  

* or 연산 활용

  ```python
  False or print("test")
  # test
  
  # array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열
  return sorted([n for n in arr if n%divisor == 0]) or [-1]
  ```

  

* f-string, enumerate 활용하기

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

  

* 삼항연산자

  `val = test ? x : y` 

  이런 c 스타일의 삼항연산자를 파이썬에서 표현하면 

  `val = x if test else y` 가 된다.

  

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



* enumerate


* ```python
  # 리스트 max 값이 들어있는 인덱스+1 모두 저장
  for idx, s in enumerate(score):
    if s == max(score):
      result.append(idx+1)
  ```



* lambda

  * 정의

  ```python
  def foo(parameters):
    expression
    
  foo = lambda parameters: expression
  ```

  * 활용

  ```python
  f = lambda x: x**2
  print(f(8))
  #64
  
  #map은 iterable 각각의 요소를 function에 넣어줌
  a = [1, 2, 3, 4]
  b = [5, 6, 7, 8]
  list(map(lambda x, y: x+y, a,b))
  #[6, 8, 10, 12]
  
  #filter는 iterable 각각의 요소를 function에 넣은 뒤 True 인 경우만 남김
  l = [1,2,3,4,5,6]
  list(filter(lambda x: x % 3 == 0, foo) )
  
  # array 에서 commands[0]번째 줄부터 commands[1]줄까지 자른 뒤 정렬 후 k번째 값 선택
  list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
  ```

  

* sorted

  * key, reverse

  ```python
  # 리스트를 각 요소의 n번째 값을 기준으로 정렬하라
  sorted(lst, key=lambda x: x[n])
  
  student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)] 
  sorted(student_tuples, key=lambda x: x[2])   
  # sort by age
  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  # 출처: https://wayhome25.github.io/python/2017/03/07/key-function/
  
  # 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴
  return "".join(sorted(s, reverse=True))
  
  ```



* index

  ```python
  # 리스트에서 특정 값을 찾아서 인덱스를 리턴해라
  return l.index(key)
  ```



* list vs collections.deque

  * list.pop()은 O(1) 이지만, list.pop(0)은 O(n) 가 소요됨
  * 따라서 stack은 list, queue는 deque를 쓰는 것이 좋음. deque는 양 끝단 모두 O(1)임
    * deque.append(), deque.pop(), deque.appendleft(), deque.popleft()
  * 단 collections.deque은 슬라이싱이 안 되므로 주의

  ```python
  from collections import deque
  
  dq1 = deque()
  dq2 = deque([1,2,3])
  dq3 = deque([_ for _ in range(10)])
  
  dq1.append(1)
  dq1.append(2)
  dq1.append(3)
  dq1.popleft()
  # 1
  ```

  

* for-else

  * for- else는 예외처리를 간결하게 해줌. 아래 두 코드는 동일한 기능을 수행

  ```python
  data = [2, 4, 5, 11, 3]
  flag = False
  
  for i in data:
  	if i%2 ==0:
  		flag = True
  		break
  if(test == 0):
  	print('2의 배수 없음')
  ```

  ```python
  data = [2, 4, 5, 11, 3]
  for i in data:
    if i > 10:
      break
  else:
    print('2의 배수 없음')
  ```

* 딕셔너리

  ```python
  d = {"a":3, "b":100}
  del d["a"]
  print(d) # {'b': 100}
  ```

* any

  any(x), x 중 참이 있으면 return True, x가 모두 거짓일 때 return False. all(x)의 반대

  ```python
  any([1, 2, 3, 0])
  # True
  any([0, ""])
  # False
  ```

  



## 2. 이런 점은 주의하자

* 가변적인 변수(예컨대, 리스트)를 디폴트 파라미터로 주는 경우, 파이썬은 스태틱 변수처럼 사용한다.
  * 참고: https://onlywis.tistory.com/3

