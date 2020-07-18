# Javascript 기초 개념

### 모듈

* 순수  js에는 모듈이라는 개념이 분명하게 존재하지 않음
* 그러나 호스트 환경(js가 구동되는 환경,  리액트, node ...)에 따라 모듈화 방법이 다름



### API와 UI

* User Interface
  * 사용자들을 대면하는 접점

* Application Programming Interface
  * 주로 개발자가 대면하는 접점



#### 객체

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



### this

* **`this`**는 메소드를 호출한 객체가 저장된 프로퍼티다.

  * 다른 언어의 경우 **`this`** 객체를 참조하는 주소를 의미하며 자바스크립트의 **`this`** 조금 다르다. 어떤 문맥에서 **`this`**가 쓰였냐가 핵심이다. 

* 전역 스코프에서 쓰였다면 **`this`**는 전역 객체인 window다. 즉 this가 window(전역 객체)를 문맥 객체로 갖는 것

  * 일반 함수들은 전역 객체의 메소드처럼 동작한다.

  ```javascript
  var a = 1;
  console.log(this.a);
  // 1
  
  function foo() {
    this.b = "10";
    console.log(this);
  }
  
  foo();
  // Window
  console.log(this.b);
  // 10
  
  this.foo();
  // Window
  ```

  

* 객체 메소드에서 **`this`** 사용하는 경우(예컨대 생성자), this는 해당 객체를 의미하며 다른 객체지향 언어들의 **`this`**와 차이가 없다.

  ```javascript
  function Student(name, id) {
    this.name = name;
    this.id = id;
  }
  
  var seungyoung = new Person('오승영', 00001);
  ```

  ```javascript
  a = 100
  function foo() {
    console.log(this.a);
  }
  
  var obj = {
    a: 10,
    func1: foo,
    func2: function() {
      console.log(this.a);
    }
  };
  
  obj.func1(); // 10
  obj.func2(); // 10
  
  // func3의 문맥 객체는 Window다.
  var func3 = obj.func1;
  func3(); // 100
  ```

  

### 배열

* 배열은 특수한 객체로, key가 필요없는 순차적인 자료구조다.

```javascript
members = ['egoing', 'k8805', 'sorialgi'];
for(i = 0; i < members.length; i++){
    document.write(members[i].toUpperCase());   
    document.write('<br />');
}
// EGOING
// K8805
// SORIALGI

for(key in members) {
    document.write("key : "+key+" value : "+members[key]+"<br />");
}
// key : 0 value : egoing
// key : 1 value : k8805
// key : 2 value : sorialgi
```



