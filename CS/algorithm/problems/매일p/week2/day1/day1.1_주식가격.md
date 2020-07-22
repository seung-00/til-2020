## Day 1.1
[프로그래머스 주식가격](https://programmers.co.kr/learn/courses/30/lessons/42584)

### 내 코드

```python
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        if len(prices)==1:
            answer.append(0)
            return answer
        price = prices.popleft()
        cnt = 0
        for p in prices:
            cnt +=1
            if p<price:
                answer.append(cnt)
                break
        else:
            answer.append(len(prices))
```





### 다시 풀면 이렇게

```python
# 인덱스 활용
def solution(prices):
    l= len(prices)
    answer = [0] * l
    for i in range(l):
        for j in range(i+1, l):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
```



### 리뷰

* week 1의 5.1와 비슷
* 난 큐에서 값을 하나씩 pop 하고 해당 값과 남은 값들을 비교해서 시간복잡도를 줄이려고 했다.
* 앞선 이터레이터의 위치를 기억해서 해당 위치 이후만 비교하는 경우 0 리스트를 만들고 인덱싱을 활용하는게 간결하다.

