# List 2

### 2차원 List

* 2차원 리스트 입력

  ```python
  n, m = map(int, input().split())
  myList = [0 for i in range(10)]
  for i in range(n):
  	myList[i] = list(map(int, input().split()))
  ```

  ```python
  n, m = map(int, input().split())
  myList = [list(map(int,input().split())) for i in range(10)]
  ```



* 2차원 리스트에서 원하는 데이터의 위치 찾기

  ```python
  n, m = map(int, input().split())
  myList = [list(map(int,input().split())) for i in range(10)]
  newList = [(i, j) for i in range(n) for j in range(m) if myList[i][j] == 1]
  ```

  

* 델타를 이용한 2차 리스트 탐색

  1. 2차 리스트의 한 좌표에서 네 방향의 인접 리스트 요소를 탐색할 때 사용하는 방법

  2. 델타 값은 한 좌표에서 네 방향의 좌표와 x, y의 차이를 저장한 리스트로 구현

  3. 델타 값을 이용하여 특정 원소의 상하좌우에 위치한 원소에 접근

  4. 이차원 리스트의 가장자리 원소들은 상하좌우 네 방향에 원소가 존재하지 않을 수도 있으므로, 인덱스를 체크하거나 범위를 제한해야 함

     ```python
     #arr[0...n-1][0...n-1]
     dx = [0,0,-1, 1] # 상하좌우
     dy = [-1,1,0,0]
     
     for x in range(len(arr)):
       if(x==0 or x== len(arr)-1):
         continue
       for y in range(len(arr[x])):
         if(y==0 or y== len(arr)-1):
           continue
         for i in range(4):
           testX = x + dx[i]
           testY = y + dy[i]
           print(arr[testX][testY])
     ```

     

* 전치 행렬 구하기

  ```python
  #i 행의 좌표
  #j 열의 좌표
  arr = [[1,2,3],[4,5,6],[7,8,9]]
  
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if i<j:
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
  ```



* zip(iterable*)

  * 리스트 둘을 튜플로 묶어줄 수 있음

  ```python
  alpha = ['a', 'b', 'c']
  index = [1, 2, 3]
  alph_index = list(zip(alpha, index))
  print(alph_index)
  >>>[('a',1), ('b',2), ('c',3)]
  #인덱스 기준으로 일대일 대응 묶음
  ```

  * *을 이용해서 다차원 리스트를 행 별로 분리한 다음 인자로 묶을 수도 있음 => 전치 행렬 변환과 같은 결과
    * arr(i)(j) <=> arr(j)(i)가 되므로

  ```python
  arr = [[1,2,3],[4,5,6],[7,8,9]]
  print(list(zip(*arr)))
  >>[(1,4,7),(2,5,8),(3,6,9)]
  ```

  

  