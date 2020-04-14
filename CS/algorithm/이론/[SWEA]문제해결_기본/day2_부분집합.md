# 부분 집합

* 부분 집합의 합 문제

  ex) {-7, -3, -2, 5, 8}에서 합이 0인 부분 집합인 경우 {-3,-2,5}

  * 완전 검색 기법으로, 집합의 모든 부분 집합을 생성한 후 각각의 합을 확인

* 부분 집합의 수

  * 2^n (n은 원소의 수) => 각 원소를 부분 집합에 포함시키거나, 포함시키지 않는 두 경우를 모든 원소에 적용한 경우의 수

  * bit list(트리 구조)

    ```python
    bit = [0,0,0,0]
    for i in range(2):
        bit[0] = i
        for j in range(2):
            bit[1] = j
            for k in range(2):
                bit[2] = k
                for l in range(2):
                bit[3] = l
                print(bit)
    ```

    <img src="https://user-images.githubusercontent.com/46865281/72202688-c6eeac00-34a5-11ea-90db-bfc2ac339f41.png" alt="image" style="zoom:25%;" /><img src="https://user-images.githubusercontent.com/46865281/72202752-74fa5600-34a6-11ea-9fca-0f41cda78666.png" alt="image" style="zoom:25%;" />

    

  * 비트 연산자

    1. **&**: and 연산

    2. **|**: or 연산

    3. **<<** : 피연산자의 비트 열을 왼쪽으로 이동

    4. **>>** : 피연산자의 비트 열을 오른쪽으로 이동

       ```python
       1<<n			#2^n 부분 집합
       i&(1<<j)	#i에서 j번째 비트가 1인지 확인
       ```

  * 비트 연산자 활용해서 간결하게 부분 집합 생성

    ```python
    arr = [3,6, 7, 1, 5, 4]
    n = len(arr)					#n: 원소의 개수
    
    for i in range(1<<n):	#1<<n: 부분 집합의 개수만큼 루프
      for j in range(n):	#원소의 수만큼 비트를 비교함
        if i&(1<<j):			#i의 j번째 비트가 1이면 j번째 원소 출력
          print(arr[j], end=',')
         print()
    ```

    