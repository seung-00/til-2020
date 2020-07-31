# Javascript 배열

## 배열 

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
  ```

  

### 배열 요소 조작

[참고]([https://zetawiki.com/wiki/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8_push()](https://zetawiki.com/wiki/자바스크립트_push())

* n번째 삽입, 삭제

  ```javascript
  let fruits = ["Apple", "Banana", "Orange", "Mango"];
  let new_fruit = "Melon";
  fruits.splice(2, 0, new_fruit);
  console.log( fruits );
  // ["Apple", "Banana", "Melon", "Orange", "Mango"]
  
  let fruits = ["Apple", "Banana", "Orange", "Mango"];
  // [2]번째부터 1개 삭제
  fruits.splice(2, 1);
  console.log( fruits );
  // ["Apple", "Banana", "Mango"]
  ```



* push, pop

  * 배열의 뒤에서 삽입, 삭제

  ```javascript
  let fruits = ["Apple", "Banana", "Orange"];
  fruits.push( "Lemon" ); // 여러개 넣을 수도 있음
  console.log( fruits );
  // ["Apple", "Banana", "Orange", "Lemon"]
  
  
  let fruits = ["Apple", "Banana", "Orange"];
  let element = fruits.pop();
  console.log( element );
  // Orange
  console.log( fruits );
  // ["Apple", "Banana"]
  ```

  

* unshift, shift

  * 배열의 앞에서 삽입, 삭제

  ```javascript
  let fruits = ["Apple", "Banana", "Orange"];
  fruits.unshift( "Lemon" );
  console.log( fruits );
  // ["Lemon", "Apple", "Banana", "Orange"]
  
  
  let fruits = ["Apple", "Banana", "Orange"];
  let element = fruits.shift();
  console.log( element );
  // Apple
  console.log( fruits );
  // ["Banana", "Orange"]
  ```

  

* indexOf

  * 찾은 값의 첫 번째 원소 위치를 리턴한다. 배열에 없을 경우 -1을 리턴한다.

  ```javascript
  let fruits = ["Apple", "Banana", "Orange"];
  fruits.indexOf("Apple");
  // 0
  fruits.indexOf("milk");
  // -1
  ```

  


