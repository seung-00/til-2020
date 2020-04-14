### 반복과 재귀

* 반복과 재귀는 유사한 작업을 수행함
  * 재귀는 하나의 큰 문제를 더 작은 문제로 쪼개는 작업에 사용됨
* 선택 정렬(반복 활용)

```python
def sort(lst):
	for i in range(len(lst)-1):
		min = i
		for j in range(i+1, len(lst)):
			if lst[j]<lst[min]:
				min = j
		lst[i], lst[min] = lst[min], lst[i]
```

* 재귀 알고리즘
  * base case(종료)
  * inductive part(호출)
  * 작성 절차: 
    * 더 작은 문제로 표현할 수 있는가
    * 직접 해결할 수 있는 경우 base case 확인
    * N이 줄어서 base case 를 만나는가
  * 재귀의 비효율성: 함수 호출은 스택이 쓰임. 재귀는 반복적으로 스택이 쌓이므로 오버헤드 발생
* 반복 or 재귀 ? => 문제에 따라 더 자연스러운 방법을 사용!



## 