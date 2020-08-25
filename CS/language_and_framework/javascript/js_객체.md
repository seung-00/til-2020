# Javascript 객체

[생활코딩](https://opentutorials.org/course/743) 강좌를 수강 후 추가적인 정보들을 보충해 정리한 문서입니다.



## 객체

### 객체

* 자바스크립트의 객체는 key 와 value로 이루어진 자료구조다.
  * key는 문자열만 가능하다.
* **`for-in loop`** 을 써준다.

```javascript
var grades = {'egoing': 10, 'k8805': 6, 'sorialgi': 80};

for(key in grades) {
    document.write("key : "+key+" value : "+grades[key]+"<br />");
}

var grades = {
    'list' : {'egoing': 10, 'k8805': 6, 'sorialgi': 80},
  	'show' : function(){	// 메소드
      for (var name in this.list){
        console.log(name, this.list[name]);
      }
    }
}
document.write(grades['list']['egoing'])
// 10
grades['show']();
```



### 프로퍼티

* 프로퍼티(property)는 객체 내부의 데이터를 의미한다.
  * 프로퍼티에는 몇몇 속성이 존재한다. **`enumerable, eritable, configurable`** 등이 그것이다.
  * 만약 해당 프로퍼티가 enumerable 하다면 **`for-in`** loop로 순차적으로 접근할 수 있다.
