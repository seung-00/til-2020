## Day 3.1
[소수 찾기](https://programmers.co.kr/learn/courses/30/lessons/42839?language=javascript)

### 내 코드 (틀림)



### 다시 풀면 이렇게

```javascript
function solution(numbers) {
    let answer = 0;
    let subsets = new Set();
    mergeNumbers(subsets , '' , numbers.split(''));
    return subsets.size;
}

function primeChk(num) {
    if( num < 2) return false;
    for (let i =2; i <= num / 2 ; i++) {
        if( num % i === 0) return false;
    }
    return true;
}

function mergeNumbers(subsets , subset, nums) {
    if( nums.length === 0 ) return;
    
    for (let i = 0, max = nums.length; i<max; i++) {
        let n = nums.shift();
        let num = Number(subset+n);
        if (primeChk(num)) {
          console.log(num);
        subsets.add(num);
        }
        mergeNumbers(subsets, subset+n , nums);
        nums.push(n);
    }
}
```



### 리뷰

* 소수를 확인하는 건 쉬웠지만 부분집합 만드는게 생각보다 어려웠음.
