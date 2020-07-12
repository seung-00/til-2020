## Day 4.1
[프린터](https://programmers.co.kr/learn/courses/30/lessons/42587)

### 내 코드

```python
from collections import deque

def solution(priorities, location):
    l = len(priorities)
    items = [_ for _ in range(l)]
    temp = list(zip(items, priorities))
    r = sorted(temp, key=lambda x: x[1], reverse=True)
    h = {_[0]: _[1] for _ in r}
    items = deque(items)
    cnt = 0

    while items:
        item = items.popleft()
        if h[item] == list(h.values())[0]:
            del h[item]
            cnt += 1
            
            if item == location: return cnt
            continue
        items.append(item)
```



### 다시 풀면 이렇게

```python
def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans

```



```python
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any([cur[1] < q[1] for q in queue]):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
```





### 리뷰

* 스택과 큐만으로 풀어야하는 문제인데, 나는 해시를 사용했다.
  * 각 아이템들을 키로 특정하는 방법 밖에 생각이 안 났다.
* 아래 두 풀이는 해시를 쓰지 않고 문제를 풀었다
  * 첫 번째 풀이는 day 2.1의 다리를 지나는 트럭 문제와 해결 방식이 비슷하다. 목표 위치를 이동함으로써 아이템을 특정해주는 것이다.
  * 두 번째 풀이는 내 풀이와 비슷한데, 좀 깔끔한 면이 있어서 참조해봤다.

