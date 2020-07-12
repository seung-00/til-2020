## Day 5.1
[탑](https://programmers.co.kr/learn/courses/30/lessons/42588)

### 내 코드

```python
def solution(heights):
    answer = []
    heights.reverse()
    l = len(heights)
    for i, ph in enumerate(heights):
        for j,th in enumerate(heights[i+1:]):
            if th>ph:
                answer.append(l-i-j-1)
                break
        else:
            answer.append(0)
    answer.reverse()
    return answer
```



### 다시 풀면 이렇게

```python
# 인덱스로 접근해서 더 간결하게
def solution(heights):
    l = len(heights)
    answer = [0]*l
    for i in range(l-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i]<heights[j]:
                answer[i] = j+1
                break
    return answer
```





### 리뷰

* reverse가 O(n) 이니까 지양하자
