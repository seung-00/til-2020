

## comprehension

**comprehension**(함축)이란, iterable한 오브젝트를 쉽게 정의하기 위한 파이썬의 문법이다. list, set, dict 등의 자료형에서 comprehension을 지원하고 있다. 



### list comprehension



**생성**

만약 1부터 10까지 정수를 리스트에 저장해야 한다고 가정하자.

```python
nums = []
for i in range(1, 10+1):
  nums.append(i)
```

이를 comprehension 사용으로 간단하게 만들 수 있다.

```python
nums = [i for i in range(1, 10+1)]
```



comprehension에서 선행하는 i 는 위의 코드의 append 인자인 i와 쓰임이 같다. i 뒤의 for 문 또한 쓰임이 같다. 

```python
evens = [i*2 for i in range(1, 10+1)]
```





**조건문**

```python
evens = [i for i in range(1,10+1)if i%2 == 0]
```

위와 같이 if 문을 지원한다.





**중첩**

```python
nums = [i+j for i in ['a','b','c','d','e'] for j in ['1','2','3','4','5']]
print(nums)
#['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e4', 'e5']
```

for 문은 중첩이 가능하다. 이때 앞의 for 문이 우선해서 시행된다. comprehension이 미적용된 상태로 생각하면 다음과 같다.

```python
nums = []
for i in ['a','b','c','d','e']:
  for j in ['1','2','3','4','5']:
    nums.append(i+j)
print(nums)
```

