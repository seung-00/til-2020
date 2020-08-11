#  javascript 클로저

## 개요

> A **closure** is the combination of a function bundled together (enclosed) with references to its surrounding state (the **lexical environment**). In other words, a closure gives you access to an outer function’s scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time.
>
> 클로저는 함수와 함수가 선언된 어휘적 환경(lexical enviroment)의 조합이다. 클로저를 이해하려면 자바스크립트가 어떻게 변수의 유효범위를 지정하는지(Lexical scoping)를 먼저 이해해야 한다.
>
> MDN

* 클로저란, 함수 내부에서 생성한 데이터와 그 스코프로 인해 발생하는 특수한 상태를 의미
  * 함수가 정의될 시점, 닫혀있는(closed) 스코프에서 내부 정보를 유지함
  * js에는 class가 없고 따라서 private 변수도 없다. 이와 유사한 효과를 보기 위해 내부 함수가 외부 함수의 지역변수에 접근하도록 하는 패턴이 자주 사용됨 (아래 case 4).
    * **생명 주기가 끝난 외부 함수의 변수를 참조한다** 라고 많이 표현함.



### 왜 쓰는가?

* 접근 권한 제어

* 지역변수 보호

* 데이터 보존 및 활용

  * 예제 코드로 확인해보자.

  

### 예제

* case 1

  * 함수 a()의 스코프 내부에 b()를 선언함. a() 에서 선언한 x는 a()와 b() 내부에서만 실행 가능함

    * 접근 권한 제어, 지역변수 보호

    ```javascript
    function a() {
      var x = 1;
      function b() {
        console.log(x);
      }
      b();
    }
    a();	// 접근 가능
    console.log(x); // 접근 불가
    ```

* case 2

  * a()에서 b()를 리턴함으로써 외부에서  a()의 x의 값을 출력할 수 있음. 그러나 마찬가지로 외부에서 임의로 x의 값을 변경할수는 없음

    * 데이터 보존 및 활용

    ```javascript
    function a {
      var x = 1;
      return funciton b() {
        console.log(x);
      }
    }
    var c = a();
    c();
    ```

* case 3

  * 내부에서 함수를 리턴함으로써 외부에서 내부 프로퍼티를 접근하도록 권한을 주었다. getter와  setter의 설정에 따라 지역변수에 영향을 줄지 여부를 결정할 수 있다.

    * 접근 권한 제어, 지역변수 보호, 데이터 보존 및 활용

    ```javascript
    function a() {
      var _x = 1;
      return {
        get x() { return _x; }
        set x(v) { _x = v; }
      }
    	var c = a();
    	c.x = 10;
    }
    ```

* case 4

  * private 변수를 클로저로 만들어보자.

    ```javascript
    var obj = {
        _x: 2,
        x: 10,
        func: function() {
            console.log(`x: ${this.x}, _x: ${this._x}`);
        }
    }
    
    obj.func(); // x: 10, _x: 20
    ```

  * 위 코드에서 객체의  _x를 외부에서 접근할 수 없도록 바꿔보자.

    * 함수 내부에서 함수를 리턴하는 경우, 그 함수는 정의될 때 정보를 유지함.

    ```javascript
    var createObj = () => {
        var _x = 2;
        return {
            x: 10,
            func: function() {
                console.log(`x: ${this.x}, _x: ${_x}`);	// _x는 객체 바깥에 있으므로 this 빼줌
            }
        }
    }
    
    obj = createObj();
    // obj._x = 20;
    obj.func();	// x: 10, _x: 2
    ```

    

### REFERENCES

* [MDN](https://developer.mozilla.org/ko/)
* [Javascript 핵심 개념 알아보기 - JS Flow]([https://www.inflearn.com/course/%ED%95%B5%EC%8B%AC%EA%B0%9C%EB%85%90-javascript-flow](https://www.inflearn.com/course/핵심개념-javascript-flow))