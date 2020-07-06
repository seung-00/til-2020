## Day 1.1
[프로그래머스 쇠막대기](https://programmers.co.kr/learn/courses/30/lessons/42585)

### 내 코드

```python
def solution(arrangement):
    stack = []
    answer = 0
    flag = False
    l = len(arrangement)
    for i in range(l):
        if flag:
            flag = False
            continue

        if arrangement[i] == '(':
            if arrangement[i+1] == ')': # razer
                answer += len(stack)
                flag = True
                
            else: # stick
                stack.append(True)
                answer += 1
            
        else: # arrangement[i] == ')'
            stack.pop(0)

    return answer
```

```
테스트 1 〉	통과 (54.59ms, 11MB)
테스트 2 〉	통과 (0.07ms, 10.7MB)
테스트 3 〉	통과 (13.59ms, 10.8MB)
테스트 4 〉	통과 (0.58ms, 10.7MB)
테스트 5 〉	통과 (0.82ms, 10.7MB)
테스트 6 〉	통과 (0.82ms, 10.7MB)
테스트 7 〉	통과 (7.83ms, 10.9MB)
테스트 8 〉	통과 (7.80ms, 10.7MB)
테스트 9 〉	통과 (9.25ms, 10.8MB)
테스트 10 〉	통과 (8.59ms, 10.8MB)
테스트 11 〉	통과 (6.57ms, 10.7MB)
테스트 12 〉	통과 (6.82ms, 10.7MB)
테스트 13 〉	통과 (7.28ms, 10.7MB)
테스트 14 〉	통과 (10.58ms, 10.9MB)
테스트 15 〉	통과 (11.17ms, 10.9MB)
테스트 16 〉	통과 (10.94ms, 10.8MB)
테스트 17 〉	통과 (12.72ms, 10.8MB)
테스트 18 〉	통과 (12.98ms, 10.9MB)
테스트 19 〉	통과 (12.76ms, 10.9MB)
테스트 20 〉	통과 (13.63ms, 10.8MB)
```



### 다시 풀면 이렇게

```python
def solution(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')

    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer
```

```
테스트 1 〉	통과 (5.84ms, 10.9MB)
테스트 2 〉	통과 (0.05ms, 10.7MB)
테스트 3 〉	통과 (6.88ms, 11MB)
테스트 4 〉	통과 (0.29ms, 10.7MB)
테스트 5 〉	통과 (0.42ms, 10.7MB)
테스트 6 〉	통과 (0.42ms, 10.8MB)
테스트 7 〉	통과 (3.83ms, 10.8MB)
테스트 8 〉	통과 (3.80ms, 10.7MB)
테스트 9 〉	통과 (4.47ms, 10.8MB)
테스트 10 〉	통과 (4.02ms, 10.8MB)
테스트 11 〉	통과 (3.17ms, 10.8MB)
테스트 12 〉	통과 (3.30ms, 10.8MB)
테스트 13 〉	통과 (3.33ms, 10.7MB)
테스트 14 〉	통과 (5.08ms, 10.9MB)
테스트 15 〉	통과 (5.47ms, 11MB)
테스트 16 〉	통과 (5.32ms, 10.8MB)
테스트 17 〉	통과 (5.77ms, 10.9MB)
테스트 18 〉	통과 (6.22ms, 10.9MB)
테스트 19 〉	통과 (6.13ms, 10.9MB)
테스트 20 〉	통과 (6.24ms, 11MB)
```



### 리뷰

* 굳이 스택 안 쓰고 합 연산만으로 가능