## Day 3.1
[124 나라의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12899#)

### 내 코드

```python
# 틀렸음
def solution(n):
    num = ['1','2','4']
    answer = ""

    while True:
        m, r = divmod(n-1, 3)
        answer = answer + num[r]
        if m != 0:
            n = m
            continue
        return answer
```



### 다시 풀면 이렇게

```python
# 내 코드에서 잘못된 부분 수정 + 정리
def solution(n):
    num = ['1','2','4']
    answer = ""

    while n!=0:
        n, r = divmod(n-1, 3)
        answer= num[r] + answer
    return answer
```



```python
# 재귀로 구현
def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return solution(q) + '124'[r]
```





### 리뷰

* 3진법 문제임을 알았지만, n-1을 생각하지 못해서 조금 헤맸다.
  * 테스트 케이스를 대입해보면서 귀납적으로 생각했다면 좀 더 쉽게 알 수 있었을 것이다.
* 주어진 테스트 케이스는 통과했지만 틀렸다. 생각했던 로직에서 잘못된 부분이 존재했고 히든 테케에서 걸렸다.
  * 디테일을 좀 더 신경 쓰자

