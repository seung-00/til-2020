## Day 1.3
[프로그래머스 멀쩡한 사각형](https://programmers.co.kr/learn/courses/30/lessons/62048)

### 내 코드

못 품



### 다시 풀면 이렇게

```python
import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

출처: https://leedakyeong.tistory.com/135#comment16270807 [슈퍼짱짱]
```



### 리뷰

* 일정한 패턴이 두 수의 최대 공약수 만큼 반복된다
  * 대각선이 지나간 사각형 = 가로 길이 + 세로 길이 - 가로, 세로 길이 최대 공약수
