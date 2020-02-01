# 190117



## 스택의 활용: 계산기

* 중위표기식 -> 후위표기식

  1. 토큰 읽음

  2. 피연산자면 push

  3. if 토큰이 연산자일 경우:

     * if 우선 순위가 높음: stack.push(토큰)

     * elif 우선 순위가 낮음: 

       ​	while 연산자의 우선 순위가 토큰보다 작을 때까지:

       ​		-> stack.pop

        	stack.push(토큰)

     * elif top에 연산자가 없음:

       ​	stack.push(토큰)

       

  4. if 토큰 == ')':

     ​	while:

     ​		if stack.peek() == '(':

     ​			stack.pop()

     ​			break

     ​		else:		

     ​			print(stack.pop())

     

  5. 더 읽을게 없을 때까지 반복

     

  6. while stack:

     ​	print(stack.pop())



* 후위 표기법 계산

  1. if 토큰이 피연산자:

     ​	stack.push(토큰)

     

  2. elif 토큰이 연산자:

     ​	x = stack.pop()

     ​	y = stack.pop()	# 토큰(피연산자)을 두 번 꺼냄

     ​	rst = eval()	# 연산 수행

     ​	stack.push(rst)	#결과 push

     

  3. while stack:

     ​	print(stack.pop())



## 백트래킹

* 정의: 해를 찾는 도중, 해가 아닐 경우 되돌아가서 다시 해를 찾는 기법
  * 최적화, 결정 문제에 쓰임 => 문제의 조건을 만족하는 해가 존재하는지 여부를 T/F로 답하는 문제
  * ex) 미로찾기, n-Queue, map coloring, subset sum
* DFS와 비교:
  * 특정 경로가 해를 구해주지 못할 것 같으면 그 경로를 멈추고 되돌아감으로써 시도의 횟수를 줄임
  * 이를 **가지치기** 라 함. 해의 가능성이 있는지 판단하는 과정을 **유망**성을 점검한다고 함



## 분할 정복

* 정의

  1. 분할: 문제를 부분으로 나눔
  2. 정복: 각각 해결
  3. 통합: (필요하다면) 해답을 모음

* 예시: 재곱

  ```python
  def Power(base, exp):
    if exp == 0 or base == 0:
      return 1
    if exp % 2 == 0:
      newBase = Power(base, exp/2)
      return newBase*newBase
    else:
      newBase = Power(base, (exp-1)/2)
      return (newBase*newBase)*base
  ```

  * 일반적으로 값을 n번 곱하는 방식의 시간 복잡도: O(n)

    분할 정복 기반 방식의 시간 복잡도: O(log n)

    ![image-20200117140011299](/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200117140011299.png)



* **퀵 정렬**

  * 핵심은 파티션을 기준으로 양 옆을 나누는 것(파티션의 자리를 찾아주는 것)

  * ```python
    def QuickSort(a, begin, end):
      if begin < end:
        p = Partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
    ```

  * ```python
    def Partition(a, begin, end):
      pivot = (begin + end)//2
      left = begin
      right = end
      while left<right:
        while(a[left]<a[pivot] and left<right): left +=1
        while(a[right]>=a[pivot] and left<right): right -= 1
          #피봇 기준으로 정렬 중
        if left<right: # 아직 피봇 기준 정렬 전 섞어줘야 함
          if left == pivot: pivot = right
          a[left], a[right] = a[right], a[left] # 피봇 기준으로 정렬이 되게 바꿔줌
        a[pivot], a[right] = a[right], a[pivot]
        return right
    ```

  * ![image-20200117141515654](/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200117141515654.png)

  * ![image-20200117141554532](/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200117141554532.png)

  * ![image-20200117141645980](/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200117141645980.png)

* **합병 정렬**

  