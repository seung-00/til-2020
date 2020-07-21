# javascript 함수지향

## 유효범위

### 변수의 수명

  * 우선적으로  local, 이후 global
  * 전역변수는 지양하자.

  ```javascript
  function a (){
      var i = 0;
  }
  for(var i = 0; i < 5; i++){
      a();
      document.write(i);
  }
  // 01234
  ```

  ```javascript
  function a (){
      i = 0;
  }
  for(i = 0; i < 5; i++){
      a();
      document.write(i);
  }
  // 무한반복
  ```



### 전역 변수를 사용해야 한다면,

  1. 객체 활용

     ```javascript
     MYAPP = {}
     MYAPP.calculator = {
         'left' : null,
         'right' : null
     }
     MYAPP.coordinate = {
         'left' : null,
         'right' : null
     }
      
     MYAPP.calculator.left = 10;
     MYAPP.calculator.right = 20;
     function sum(){
         return MYAPP.calculator.left + MYAPP.calculator.right;
     }
     document.write(sum());
     ```

  2. 익명함수

     * 여러 js 모듈에서 이 방법이 쓰임

     ```javascript
     (function(){
         var MYAPP = {}
         MYAPP.calculator = {
             'left' : null,
             'right' : null
         }
         MYAPP.coordinate = {
             'left' : null,
             'right' : null
         }
         MYAPP.calculator.left = 10;
         MYAPP.calculator.right = 20;
         function sum(){
             return MYAPP.calculator.left + MYAPP.calculator.right;
         }
         document.write(sum());
     }())
     ```



## 값으로서의 함수

### 1급 객체란?

  * 1급 객체 혹은 1급 시민(first class citizen)은 꽤 재밌는 비유다. 거주, 투표, 출입국 등의 자유가 있는 과거의 1급 시민처럼, 연산과 전달이 자유로운 객체를 1급 객체라 말한다.

  * 일반적으로 다음과 같은 조건들을 충족한다.

    * 변수나 데이터에 할당 가능

    * 객체의 파라미터로 넘길 수 있음

    * 객체의 리턴값으로 리턴 할수 있음

    * 동적으로 프로퍼티 할당이 가능

    * 할당에 사용된 이름과 관계없이 구별이 가능

      ```javascript
      var foo = function goo(){
      ...
      }
      
      foo();
      ```

### js의 함수는 객체, 즉 값으로 취급되며 1급객체다.

  ```javascript
  function a(){}
  ```

  * 객체의 메소드로도 사용됨

  ```javascript
  a = {
      b:function(){
      }
  };
  ```

  * 다른 함수의 인자로 전달 될수도 있음

  ```javascript
  function cal(func, num){
      return func(num)
  }
  function increase(num){
      return num+1
  }
  function decrease(num){
      return num-1
  }
  alert(cal(increase, 1));
  alert(cal(decrease, 1));
  ```

  * 리턴 값으로도 사용될 수 있음

  ```javascript
  function cal(mode){
      var funcs = {
          'plus' : function(left, right){return left + right},
          'minus' : function(left, right){return left - right}
      }
      return funcs[mode];
  }
  alert(cal('plus')(2,1));
  alert(cal('minus')(2,1));
  ```

  * 배열의 값으로도 사용할 수 있음

  ```javascript
  var process = [
      function(input){ return input + 10;},
      function(input){ return input * input;},
      function(input){ return input / 2;}
  ];
  var input = 1;
  for(var i = 0; i < process.length; i++){
      input = process[i](input);
  }
  alert(input);	// 60.5
  ```



## 콜백

### 처리의 위임

```javascript
function sortNumber(a,b){
    // 위의 예제와 비교해서 a와 b의 순서를 바꾸면 정렬순서가 반대가 된다.
    return b-a;
}
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
alert(numbers.sort(sortNumber)); // array, [20,10,9,8,7,6,5,4,3,2,1]
```



