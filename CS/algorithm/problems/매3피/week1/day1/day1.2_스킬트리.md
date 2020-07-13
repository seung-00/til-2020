## Day 1.2
[프로그래머스 스킬트리](https://programmers.co.kr/learn/courses/30/lessons/49993)

### 내 코드

```python
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        temp = list(skill)
        flag = True
        for s in skill_tree:
            if not temp:
                break
            elif s == temp[0]:
                temp.pop(0)
            elif s in temp[1:]:
                flag = False
                break
        if flag:
            answer += 1

    return answer
```



### 다시 풀면 이렇게

```python
from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = deque(skill)

        for s in skill_tree:
            if s in skill:
                if s != skill_list.popleft():
                    break
        else:
            answer += 1

    return answer
```



### 리뷰

* 큐는 deque로 구현
* for-else

