# Javascript 템플릿 리터럴

* 템플릿 리터럴(Template literals)은 ES6에 새로 도입된 문자열 표기법이다.
* 기존 문자열 표기법 작은 따옴표 `'` 와 큰 따옴표 과 `"` 대신 백틱(backtick) (``)을 사용한다.
  * 파이썬3의 *f-string*과 비슷하다.

### Multi-line strings

* newline character `\n`  를 템플릿 리터럴의 일부로 포함할 수 있다.

  ```javascript
  // 기존
  console.log("string text line 1\n"+
  "string text line 2");
  // "string text line 1
  // string text line 2"
  
  // Template literals
  console.log(`string text line 1
  string text line 2`);
  // "string text line 1
  // string text line 2"
  ```



### Expression interpolation

* 표현식을 템플릿 리터럴의 일부로 포함할 수 있다.

  ```javascript
  // 기존
  var a = 5;
  var b = 10;
  console.log("Fifteen is " + (a + b) + " and\nnot " + (2 * a + b) + ".");
  // "Fifteen is 15 and
  // not 20."
  
  
  // Template literals
  var a = 5;
  var b = 10;
  console.log(`Fifteen is ${a + b} and
  not ${2 * a + b}.`);
  // "Fifteen is 15 and
  // not 20."
  ```

  

### REFERENCES

* [MDN](https://developer.mozilla.org/ko/)