# Javascript 함수 선언 방식

## 함수 선언 방식

* 함수  선언과 함수 표현식의 차이는 **선언한 함수를 변수에 할당하냐 여부에 달렸음**

  * 할당을 하지 않은 경우, 전체가 호이스팅의 대상이 됨
  * 할당을 한 경우 변수만 호이스팅이 됨

* 호이스팅 동작 차이 때문에 함수 표현식이 선언문보다 선호됨

  * 다음과 같은 문제가 발생할 수 있음

    * 두 `sum()` 선언이 호이스팅 되고 캐스캐이딩 원칙 (나중에 나오는 코드가 우선순위 높음)에 의거해 첫 번째 `sum()`이 덮어쓰였다.

    ```javascript
    function sum(x, y){
    	return x + ' + ' + y + ' = ' + (x+y);
    }
    console.log(sum(1,2));	
    
    // expected: 1 + 2 = 3
    // actual: 3
    
    // ...
    
    function sum(x, y){
      return x + y;
    }
    
    console.log(sum(1,2));	// 3 
    ```

    

### 함수 선언문

```javascript
function func() {
  return 'a';
}
```



### 기명 함수 표현식

```javascript
const f = function func() {
  return 'a';
}
```



### 익명 함수 표현식

```javascript
const f = function() {
  return 'a';
}
```

* 최근 브라우저는 익명 함수 표현식을 쓴 경우 자동으로 변수명을 네임 프로퍼티에 할당함
  * 디버깅 시에 불편하지 않음



## 화살표 함수

* 화살표 함수 표현식(arrow function expression)은  **ES6** 에 추가된 익명 함수 표현 방법이다.

  * 구문

    ```javascript
    // 일반 익명 함수 표현식
    const foo = function(param1, param2, ..., paramN) { statements };
    
    // 화살표 함수 표현식
    const bar = (param1, param2, ..., paramN) => { statements };
    ```

* 간결하다.

  * 특히 콜백을 간결하게 표현할 수 있다.

    ```javascript
    let arr = [1, 2, 3, 4];
    let odds = arr.filter(function(param) {return param%2 !==0;})	// 일반 익명 함수
    
    let odds2 = arr.filter(param => (param%2) !== 0);	// 화살표 함수
    
    console.log(odds);	// [1, 3]
    console.log(odds2);	// [1, 3]
    ```

* **`this`**

  * 기존의 *function* 키워드 함수는 함수가 호출될 때 호출한 방법에 따라 `this`에 객체를 동적으로 바인딩한다.

    * 생성자 함수, 객체의 메소드를 제외한 모든 함수의 `this`가 전역 객체(*window*)

    ```javascript
    function foo() {
        console.log(this);
    }
    
    foo();	// Window
    
    let obj = {
      val: 1,
      bar: function() {
            console.log(this);
            console.log(this.val);
        }
    }
    
    obj.bar();
    // {val: 1, bar: ƒ}
    // 1
    ```

    * *function* 키워드에서 `this`의 값은 함수가 호출한 방법이 결정한다.  아래의 예시에서 동일한 `obj.func1` 이지만 `func1()`과 `func3`의 결과가 다르다. 전자는 객체  `obj` 에서 후자는 전역 객체에서 호출했기 때문이다.

    ```javascript
    let a = 100
    function foo() {
      console.log(this.a);
    }
    
    let obj = {
      a: 10,
      func1: foo,
      func2: function() {
        console.log(this.a);
      }
    };
    
    obj.func1(); // 10
    obj.func2(); // 10
    
    // func3의 문맥 객체는 Window다.
    let func3 = obj.func1;
    func3(); // 100
    ```

    

  * 화살표 함수는 `this` 값이 정적으로 결정된다. 화살표 함수의 상위 스코프를  `this`로 참조한다. 

    * 함수가 호출된 방법에 관계 없이 `this`가 고정된다.

      ```javascript
      let a = 100;
      
      let obj = {
        a: 10,
        func: () => {console.log(this.a);}
      }
      
      obj.func(); // 10
      
      // func3의 문맥 객체는 Window다.
      let func3 = obj.func;
      func3(); // 100
      ```

      

    * 메소드로 함수가 사용된다면  *function* 키워드 방식이 적합하다. *MDN* 문서에서도 화살표 함수를 메소드로 사용하지 않는 것을 권한다.

      ```javascript
      let obj1 = {
        val: "a",
        func: function() {console.log(this.val);}	// this 는 obj1
      }
      
      let obj2 = {
        val: "b",
        func: () => {console.log(this.val);}	// this는 Window
      }
      
      obj1.func()	// a
      obj2.func()	// undefined
      ```

      

    * 콜백에서 화살표 함수의  `this`는 유용하다.

      * 생성자 함수 `Persont()` 은 아래와 같다. `SetTimeout` 함수의 콜백 함수는 `this`를 전역 객체로 바인딩한다. 결과적으로 의도와 다르게 동작한다.

      ```javascript
      function Person() {
        this.age =0;
        
        setTimeout(function() {
          console.log(this);
          this.age++;	// NaN
        }, 1000);
      }
      
      let p = new Person();	// Window
      console.log(p.age);	// 0
      ```

      * 화살표 함수로 콜백을 사용할 경우 `this`는 호출 방법과 관계없이, 함수 바깥의 함수 혹은 클래스의  `this` 값이 쓰인다.

      ```javascript
      function Person() {
        this.age =0;
        
        setTimeout(() => {
          console.log(this);
          this.age++;
        }, 1000);
      }
      
      let p = new Person();	// Person {age: 0}
      console.log(p.age);	// 1
      ```

      

### REFERENCES

* [Javascript 핵심 개념 알아보기 - JS Flow]([https://www.inflearn.com/course/%ED%95%B5%EC%8B%AC%EA%B0%9C%EB%85%90-javascript-flow](https://www.inflearn.com/course/핵심개념-javascript-flow))
* [MDN](https://developer.mozilla.org/ko/)