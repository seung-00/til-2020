# Javascript 반복문

## for-loop

* js는 다양한 for-loop 문법을 지원한다.

  * [for-loop의 성능을 비교한 글]([https://velog.io/@cada/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-for-loop-%EC%86%8D%EB%8F%84-%EB%B9%84%EA%B5%90](https://velog.io/@cada/자바스크립트-for-loop-속도-비교))을 참고했을 때 for in은 되도록 지양하고 길이를 캐시한 기본 for loop와  for of, for Each 를 사용하는 것이 좋겠다.

  * 최대 길이를 캐시한 for loop > for of > forEach 순으로 성능이 좋다. forEach는 직관적이고 간결하지만 반복을 중간에 멈춰야 하는 경우 불편할 수 있다.

    

* 기본 for

  * max length를 캐시시켜 성능을 향상시킨다

  ```javascript
  var arr = [1,2,3,4];
  
  for(var i=0; i<arr.length; i++)
  {...}	// 일반적인 for loop
  
  for(var i=0, max =arr.length; i<max; i++)
  {...}	// max lenght를 캐시시킨 for loop
  ```




* for of


  * iterable한 객체(`Arrray`, `Map`, `Set` 등)에 사용 가능한 반복문

  ```javascript
  var arr = [1,2,3,4];
  
  for(var value of members) {
      console.log(value);
  }
  // 1234
  ```

  

* forEach

  * 주어진 callback을 각 요소에 대해 오름차순으로 한 번씩 실행하는  메서드

    * `Array`, `Map`, `Set`에 사용 가능 

  * 구문

    * `index`,  `array`, `thisArg`는 생략 가능

    ```javascript
    arr.forEach(callback(currentvalue[, index[, array]])[, thisArg])
    ```

  ```javascript
  const arr = [1,2,3,4];
  
  arr.forEach(function(element){
      console.log(element);
  });
  
  // 혹은
  arr.forEach(element => console.log(element));
  
  // 1
  // 2
  // 3
  // 4
  
  arr.forEach(element => {if(element%2==0) console.log(element)});
  // 2
  // 4
  ```



* for in

  * **객체**의 모든 enumerable 프로퍼티를 반복함.

    * ES6에 추가된 문법 
    * 객체를 편리하게 순회할 수 있다.

  * 구문

    ```javascript
    for (variable in object) { ... }
    ```

    

### REFERENCES

* [MDN](https://developer.mozilla.org/ko/)