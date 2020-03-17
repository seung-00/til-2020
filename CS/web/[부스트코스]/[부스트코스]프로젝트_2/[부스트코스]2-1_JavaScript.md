# JavaScript - FE

[toc]

## 변수, 연산자, 타입

### 자바스크립트의 버전

* 자바스크립트 버전은 ECMAScript(줄여서ES)의 버전에 따라서 결정되고, 이를 자바스크립트 실행 엔진이 반영함.
* ES5, ES6(ES2015).. 이런 식으로 버전을 일컫습니다.
* 2018년을 중심으로 ES6를 지원하는 브라우저가 많아서 몇 년간 ES6 문법이 표준으로 쓰이고 있습니다.
* ES6는 ES5문법을 포함하고 있어 하위호환성 문제가 없음, 다만 feature(ECMAScript)별로 지원하지 않는 브라우저가 있을 수 있어 조심해야 합니다.



### 변수

* 변수는 var, let, const 로 선언할 수 있음
* 어떤 것을 사용하는가에 의해서 scope, 즉 변수의 유효범위가 달라짐
* ES6이전까지는 var를 사용해서 변수를 선언할 수 있음

```javascript
var a = 2;
var a = "aaa";
var a = 'aaa';
var a = true;
var a = [];
var a = {};
var a = undefined;
```



### 연산자

```javascript
// or 연산자
const name = "crong";
const result = name || "defaultName";
console.log(result);
// 출력: crong

var name = "";
var result = name || "defaultName";
console.log(result);
// 출력: defaultName

// 삼항연산자
const data = 11;
const result = (data > 10) ? "ok" : "fail";
console.log(result);

// 비교연산자
// 비교는 == 보다 === 을 사용함. ==로 인한 아래와 같은 오류가 있음
0 == false;	// true
"" == false; // true
null == false;	// false, null은 객체라서
0 == "0";	//true
null==undefined;	// true
```

* **const** 는 재할당 불가
* or 연산으로 디폴트 값 할당 가능
* 자바스크립트에서 타입까지 비교하려면  `===` 을 써야함. 주로 `===` 가 쓰임



### Type

* js에서 타입은 런타임에 결정됨
* 타입을 체크할 방법이 뚜렷이 없음. `toString.call` 을 이용해서 그 결과를 매칭하곤 함. 문자, 숫자와 같은 기본 타입은 `typeof` 키워드를 사용 가능
* 배열 같은 경우 타입을 체크하는 `isArry` 함수가 표준으로 있음



## 비교문

### 조건문

```javascript
if(true){
 //... 
}
else{}

// 혹은 한 줄로

if(true) console.log(true)
else console.log(false)
```



### 반복문

```javascript
function howMany(selectObject){
  var numberSelected = 0;
  for (var i =0; i<selected.options.length; i++){
    if (selectObject.options[i].selected){
      numberSelected++;
    }
  }
  return numberSelected;
}
```

```javascript
var arr = [1,2,3];
for (var i = 0; len = arr.length; i<len; i++){
  console.log(i)
}
```



### 문자열 처리

```javascript
typeof "abc";	// string
typeof "a";	// string
typeof 'a';	// string
```

```javascript
"ab:cd".split(":");	// ["ab","cd"]
"ab:cd".replace(":", "$");	//"ab$cd"
" abcde  ".trim();	//"abcde"
```

* 문자열과 문자는 js 에서 같은 타입
* 문자열에 다양한 메서드가 있음





## 함수

### 인자

* 파라미터의 개수와 인자의 개수가 일치하지 않아도 오류가 나지 않음. 파라미터 1개일 때 인자 수가 0이면 파라미터는 undefined 라는 값을 갖게 됨.

* 또한 디폴트 리턴 값도 undefined임

```javascript
function printName(firstname){
  var myname = "jisu";
  return myname + " " + firstname;
}

console.log(printName())	// jisu is undefined
```



### 함수 표현식과 선언문

```javascript
function printName(){
  var inner = function() {
    return "inner value"
  }
  
  var result = inner();
  console.log("name is" + result)
}

printName()	// name is inner value
```

* 위 처럼 변수 정의와 동시에 함수를 만드는 것을 **함수 표현식(function expression)** 이라고 함.
* 다음과 같은 오류가 있을 수 있음

```javascript
// Function Expression
function printName(){    
  var result = inner();
  console.log("name is" + result)

  var inner = function() {
    return "inner value"
  }
}

printName()	// TypeError: inner is not a function


// Function Declarations
function printName(){    
  var result = inner();
  console.log("name is" + result)

  function inner = function() {
    return "inner value"
  }
}

printName()	// name is inner value

```

*  함수 표현식 실행 전에 호출할 경우, 함수 할당이 안 됨. inner가 있음은 알아도 함수로 인식이 안 되는 것 
* 만약 그 다음 코드처럼 함수 선언식을 쓰면 함수 타입인 것을 해당 스택에서 알게됨.



### 호이스팅

* js는 기본적으로 순서대로 스테이트를 실행하지만, js 파서가 먼저 한 번 함수를 훑어서 선언되있는 것들을 위로 끌어 올림. 이때 변수는 선언만, 함수는 정의까지 끌어 올림.

  ```javascript
  function printName(){    
    print(a)
    var a =1;
  }
  
  function printName(){    
    print(a)
    function inner(){}
  }
  
  
  // 위 코드는 호이스팅 결과 애러처럼 바뀐다.
  
  function printName(){    
    var a;
    print(a)
    a =1;
  }
  
  function printName(){    
    function inner(){}
    print(a)
  }
  
  // 따라서 함수 표현식은 변수만 미리 선언하는 모양이 되는 것!
  ```

  

### arguemtns 속성

```javascript
function a(){
  console.log(arguments);
}

function b(){
  for(var i=0; i<arguments.length; i++){
    console.log(arguments[i]);
  }
}

a(1,2,3);	// {'0':1, '1':2, '2':3 }
b(1,2,3);	// 1 2 3	(각각 new line)
```

* 배열과 유사한(배열은 아니므로 배열용 메서드 이용 불가) arguments가 디폴트로 정의된다. 
* length, [] 은 가능(오브젝트면 다 가능)



### arrow function

```javascript
fucntion getName(name){
  return "Kim " + name;
}

// 위 함수는 아래 arrow 함수와 같다.
var getname = (name) => "Kim " + name; 
```

* ES2015 추가된 문법, 점점 많이 사용되고 있는 syntax





## 함수 호출 스택

![img](https://miro.medium.com/max/1200/1*E3zTWtEOiDWw7d0n7Vp-mA.gif)

출처[^1]

[^1]:https://medium.com/@gaurav.pandvia/understanding-javascript-function-executions-tasks-event-loop-call-stack-more-part-1-5683dea1f5ec

