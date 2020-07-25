## Day 2.1
[기능개발](https://programmers.co.kr/learn/courses/30/lessons/42586#)

### 내 코드 (틀림)

```javascript
function solution(p, s) {
    let ans = [];
    let tmp = [];
    while(p.length){
        let flag = false;
        for(let i=0, max =p.length; i<max; i++)
            {
                p[i]+=s[i];
                if(p[i]>=100)
                    {
                        tmp.push(i);
                        if(i==0){
                            flag = true;
                            break;
                        }
                        p[i] = 0;
                        s[i] = 0;
                    }
            }
        if(flag){
           tmp.sort();
            let cnt = 1;
            for(let j=1, max =tmp.length; j<max; j++){
                if(tmp[j]!==j){
                    break;
                }
                cnt++;
            }
            ans.push(cnt);
            p.splice(0, cnt);
            s.splice(0, cnt);
            tmp=[];
        }
    }
   return ans;
}
```



### 다시 풀면 이렇게

```javascript
function solution(p, s) 
{
    let ans = [];

    while(p.length) 
    {
        for(let i=0, max = p.length; i<max; i++)	// day ++
        {
            if(p[i] < 100) 
            {
                p[i] += s[i];
            }
        }
        let cnt = 0;
        while(p[0] >= 100)
        {
            p.shift();
            s.shift();
            cnt++;
        }
        if(cnt)
        {
            ans.push(cnt);
        }
    }
    return ans;
}
```



### 리뷰

* queue를 씀으로써 인덱스를 저장할 필요가 없어짐.
