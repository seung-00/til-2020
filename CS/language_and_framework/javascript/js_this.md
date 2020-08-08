# Javascript this

### this

* **`this`**는 메소드를 호출한 객체가 저장된 프로퍼티다.

  * 다른 언어의 경우 **`this`** 객체를 참조하는 주소를 의미하며 자바스크립트의 **`this`** 조금 다르다. 

    

* 전역 스코프에서 쓰였다면 **`this`**는 전역 객체인 *Window다*. 즉 this가 *Window*(전역 객체)를 문맥 객체로 갖는 것

  * 일반 함수들은 전역 객체의 메소드처럼 동작한다. (`Window.func()`)
  * 생성자 함수, 객체의 메소드를 제외한 모든 함수의 `this`가 전역 객체(*Window*)

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

  

* 객체 메소드에서 **`this`** 사용하는 경우, this는 해당 객체를 의미하며 다른 객체지향 언어들의 **`this`**와 차이가 없다.

  ```javascript
  function Student(name, id) {
    this.name = name;
    this.id = id;
  }
  
  var seungyoung = new Person('오승영', 00001);
  ```

  * 객체 속의 함수(`!==`메소드)는 `this` 가 객체를 가르키지 않는다.

    ```javascript
    var a = 10;
    var obj = {
      a: 20,
      b: function() {
        console.log(this.a);
        
        function c() {
          console.log(this.a);
        }
        c();
      }
    }
    obj.b();
    
    // 20
    // 10
    ```

    * 이 문제를 스코프 체인을 이용해 우회해서 해결할 수 있다. 혹은 화살표 함수(*arrow function*)를 사용해도 된다.

      ```javascript
      var a = 10;
      var obj = {
        a: 20,
        b: function() {
          var self = this;
          console.log(this.a);
          
          function c() {
            console.log(self.a);	// 현재 스코프에 self가 없으므로 위로 올라감
          }
          c();
        }
      }
      obj.b();
      
      // 20
      // 20
      ```

      

* 메소드에서  `this`의 값은 메소드를 호출한 방법이 결정한다.  아래의 예시에서 동일한 `obj.func1` 이지만 `func1()`과 `func3`의 결과가 다르다. 전자는 객체  `obj` 에서 후자는 전역 객체에서 호출했기 때문이다.

  ```javascript
  var a = 100
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

