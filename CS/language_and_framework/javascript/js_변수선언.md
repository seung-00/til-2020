# Javascript 변수 선언 방식

## 변수 선언 방식

* js 변수 선언 방식에는  `var` , `let` , `const`가 있다.
  
  * ES5까지 `var` 키워드로만 변수를 선언할 수 있었다.  `var`은 몇가지 문제점들이 존재했고 이를 보완하기 위해 ES6부터  `let` , `const`가 도입됐다.
  
  * `let`은 변수를 선언할 때, `const`는 상수를 선언할 때 사용하는 키워드다. 다른 언어와 마찬가지로 `const`는 값을 재할당할 수 없도록 한다.
  
  * `const`는 선언과 동시에 값을 할당해줘야 한다.
  
    ```javascript
    const foo = 1;
    foo = 2; // TypeError: Assignment to constant variable.
    ```
  
    
  
* `var` vs `let`, `const` 주요 차이점

  1. 유효범위(function level scope)

  2. 중복 선언 허용 여부

  3. 키워드 생략 허용 여부

  4. 변수 호이스팅

     

### 1. 유효범위

   * function level scope: 함수 내에서 선언한 변수만 지역변수이며 외부에서 선언한 변수는 모두 전역 변수

     * python이 funciton scope 언어 중 하나다

     ```python
     for i in range(100):
       pass
     print(i)
     # 99
     ```

   * block level scope: 모든 코드 블록(함수, 조건문, 반복문 등) 내에서 선언된 변수는 지역 변수

     * c 계열, java가 block scope 언어다

     ```c++
     if (true) {
         int x = 1;
     }
     std::cout << x << std::endl;
     // error: 'x' was not declared
     ```

     

   * `var`은 function level scope

     ```javascript
     var foo = 1;
     
     if(true)
     {
       var foo = 2;
     }
     
     console.log(foo); // 2
     ```

   * `let`, `const`은 function level scope

     ```javascript
     let foo = 1;
     
     if(true)
     {
       let foo = 2;
     }
     
     console.log(foo);	// 1
     ```



### 2. 중복 선언 허용 여부

* `var`은 동일한 이름의 변수를 중복 선언할 수 있었다. 많은 이들이 이 부분에 불만을 가졌고 이후 `let`, `const`는 변수 재선언을 허용하지 않았다.

  

### 3. 키워드 생략 허용 여부

* `var`은 키워드를 생략하고 선언할 수 있다. 바꿔말하면 키워드를 명시해야 `let`, `const`를 쓸 수 있다.



### 4. 호이스팅(Hoisting)

[참고한 글](https://evan-moon.github.io/2019/06/18/javascript-let-const/)

* 호이스팅이란 js 파서가 함수가 실행되기 전에 내부에 존재하는 변수/함수 선언들을 **최상단으로 끌어올려(hoist)** 선언하는 것을 의미함
  * 변수가 함수내에서 정의되었을 경우 선언이 함수의 최상위로, 함수 바깥에서 정의되었을 경우는 전역 컨텍스트의 최상위로 변경됨
  * 이 부분 역시 사이드 이펙트 발생시킬 수 있기 때문에 불만의 대상이었음

* 예시

  * 아래 예시에서 처음 출력은 변수가 선언되기 전이므로 `error`가 발생해야 하지만 뒤의 선언을 호이스팅해서 `undefined`가 출력됐다.

  ```javascript
  const hoisting = () => {
    console.log(foo);
    var foo = 1;
    console.log(foo);
  }
  
  hoisting();
  // undefined
  // 1
  ```

  * 다음과 같은 상황도 발생할 수 있다.

  ```javascript
  var foo = 'outer scope value';
  
  const hoisting = () => {
    console.log(foo);
    var foo = "inner scope value";
    console.log(foo);
  }
  
  hoisting();
  // undefined
  // inner scope value
  // 바깥 스코프의 값을 참조하지 못했다. 
  ```



* `let` 과 `const`는 어떻게 다를까?

  * `let`, `const` 역시 호이스팅을 수행하지만 **TDZ**(Temporal Dead Zone)가 개입하면서 변수에 접근을 막고 에러를 발생시킨다.

    ```javascript
    let foo = 'outer scope value';
    
    const hoisting = () => {
      console.log(foo);
      let foo = "inner scope value";
      console.log(foo);
    }
    
    hoisting();
    // Uncaught ReferenceError: Cannot access 'foo' before initialization
    // 전역 변수에 접근하지 못했고(호이스팅을 수행했기에) 정의되지 않은 변수에 접근하지도 못했다.
    ```

  * 변수는 **선언(Declaration) -> 초기화(Initalization) -> 할당(Assignment)** 의 단계를 거친다. 선언에서 스코프가 변수 객체를 참조하고, 초기화에서 해당 객체에 메모리를 할당한다(js에서는 `undefined`로). 마지막으로 할당 단계에서 해당 메모리 공간에 값을 할당한다.

  * `var` 키워드로 객체를 선언한 경우 선언과 동시에 `undefined`로 초기화가 이루어진다. 그러나 `let`, `const`로 생성한 객체는 다르다. 

    * 변수 선언 이후  `let`, `const`는 초기화가 필요한 상태로 따로 분류된다. 아래 V8 엔진 코드로 확인할 수 있다. 자세한 설명은 상단의 참고 링크를 보자.

      ```c++
      static InitializationFlag DefaultInitializationFlag(VariableMode mode) {
        DCHECK(IsDeclaredVariableMode(mode));
        return mode == VariableMode::kVar ? kCreatedInitialized
        : kNeedsInitialization;
      }
      // https://github.com/frida/v8/blob/master/src/ast/variables.h
      ```

    * 여기서 말하는 초기화가 필요한 상태가 **TDZ** 인 것이다. 즉 `let`, `const`는 **선언** 이후 **TDZ** 구간을 거쳐 **초기화** -> **할당**이 이루어지며 **TDZ** 상태에 접근을 시도하는 경우 에러가 발생한다.