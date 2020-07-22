## Day 2.1
[프로그래머스 다리를 지나는 트럭](https://programmers.co.kr/learn/courses/30/lessons/42583)

### 내 코드

못 품



### 다시 풀면 이렇게

```python
from collections import deque 

def solution(bridge_length, weight, truck_weights):
    truck_weights.reverse()
    q=deque([False]*bridge_length)
    sec, w =0, 0
    
    while q:
        sec+=1
        out = q.popleft()
        if out:
            w-=out
        if truck_weights:
            if w+truck_weights[-1]<=weight:
                new_truck = truck_weights.pop()
                w+=new_truck
                q.append(new_truck)
            else:
                q.append(False)
    return sec
```



### 리뷰

* day 4.1과 비슷