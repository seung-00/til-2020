### [leetcode] 1290. Convert Binary Number in a Linked List to Integer



> Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
>
> Return the *decimal value* of the number in the linked list.
>
>  
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2019/12/05/graph-1.png)
>
> ```
> Input: head = [1,0,1]
> Output: 5
> Explanation: (101) in base 2 = (5) in base 10
> ```



* 나의 접근

  헤드에 해당하는 값은 이진수 -> 십진수로 표현했을 때 **2^n** (n은 리스트 사이즈) 다. 나머지 값들도 해당 자리수 만큼 2를 곱한 값이다. 따라서 하나의 변수를 두고 리스트에서 값을 꺼낼 때마다 2씩 곱해서 2^n을 만들었다. 다른 사람들 코드를 보니 괜히 재귀로 풀었다는 생각이 든다. 

  ```python
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None
  
  class Solution:
      def __init__(self):
          self.val = 0
      
      def getDecimalValue(self, head):
          if head == None:
              print(self.val)
              return self.val
          self.val = self.val*2 + head.val
          return self.getDecimalValue(head.next)
  ```

  아래는 내 코드보다 빠르면서도 깔끔한 코드들이다.



* 다른 풀이1

  재귀를 안 씀

  ```python
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None
  
  class Solution:
      def getDecimalValue(self, head: ListNode) -> int:
          answer = 0
          while head:
              answer = 2*answer + head.val
              head = head.next
          return answer
  ```

  

* 다른 풀이2

  문자열을 이용해서 깔끔하게 푼 풀이

  ```python
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None
  
  class Solution:
      def getDecimalValue(self, head):
          ans = ''
          while head:
              ans += str(head.val)
              head = head.next
              
          dec = int(ans, 2)
          return dec
  ```

  

* 다른 풀이3

  제일 빠른 코드다. 리스트로 모든 값을 받고, 해당 값이 0인 경우 결과값 업데이트를 패스했다.

  ```python
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None
  
  class Solution:
      def getDecimalValue(self, head: ListNode) -> int:
          binary = [head.val]
          while head.next != None:
              head = head.next
              binary.append(head.val)
  
          res = 0
          base = 1
          for i in binary[::-1]:
              if i == 1:
                  res += base
              base *= 2
          
          return res
  ```

  