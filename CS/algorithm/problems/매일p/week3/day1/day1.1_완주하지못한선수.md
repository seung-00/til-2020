## Day 1.1
[프로그래머스 완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576?language=javascript)

### 내 코드 (틀림)

```javascript
function solution(participant, completion) {
    for(var p of participant){
        var i = completion.indexOf(p);
        if(i==-1)
            return p;
        completion.splice(i, 1);
        }
}
```



### 다시 풀면 이렇게

```javascript
function solution(participant, completion) {
    participant.sort();
    completion.sort();
    for(var i = 0, j = participant.length; i<j; i++){
        if(participant[i] !== completion[i])
            return participant[i];
    }
}
```



### 리뷰

* 배열의 길이가 최대 100,000으로 2중 for문을 돌릴 경우 시간초과된다.
  * 그래서 indexOf를 써봤는데 역시 마찬가지로 시간초과
* 시간 복잡도를 고려할 때 먼저 생각해야 할 방법 중 하나는 배열을 정렬시키는 것
