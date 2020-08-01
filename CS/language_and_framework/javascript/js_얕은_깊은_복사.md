# 얕은 복사, 깊은 복사

[레퍼런스 1](https://developer.mozilla.org/ko/)

[레퍼런스 2]([https://medium.com/watcha/%EA%B9%8A%EC%9D%80-%EB%B3%B5%EC%82%AC%EC%99%80-%EC%96%95%EC%9D%80-%EB%B3%B5%EC%82%AC%EC%97%90-%EB%8C%80%ED%95%9C-%EC%8B%AC%EB%8F%84%EC%9E%88%EB%8A%94-%EC%9D%B4%EC%95%BC%EA%B8%B0-2f7d797e008a](https://medium.com/watcha/깊은-복사와-얕은-복사에-대한-심도있는-이야기-2f7d797e008a))



* 얕은 복사, 깊은 복사는 다른 언어들에서도 중요한 내용이다. *JS* 는 다른 언어들보다 비교적 방법이 다양한듯 하다.

### 얕은 복사(shallow copy)

* 얕은 복사란
  * 값을 복사하는 것이 아니라 주소를 복사한다.

  * 아래 예제에서 객체 `copied`는 `origin`이 참조하는 *Heap* 영역 객체 데이터의 메모리 주소만을 참조한다. 따라서 `copied.x`를 수정하면 `origin.x` 도 함께 바뀐다.

    ```javascript
    let oirgin = {
      x: 1,
      y: 2
    };
    
    let copied = origin;
    // copied와 origin은 동일한 주소값을 값으로 갖는다.
    
    copied.x = 10;
    
    consol.log(copied.x);	// 10
    consol.log(oirgin.x);	// 10
    ```

  * 객체가 중첩된 경우, **객체 속에 중첩된 객체까지 복사할 수 있느냐 여부**로 깊은 복사, 얕은 복사가 갈린다. 즉 객체의 깊이에 상관없이 복사가 가능해야 깊은 복사다.

* **`Array.prototype.slice`**

  * 배열의 안에 값을 꺼내 복사할 때 많이 쓰이는 방식이다. 중첩된 배열까지 복사하지는 못하므로 얕은 복사에 속한다.

    * 내부에서 *for-loop*가 돌아감녀서 값을 복사
    
    ```javascript
    let arr = [1, 2, 3, 4];
    let copied = arr.slice();
    copied.push(5);
    
    console.log(copied);	// [1, 2, 3, 4, 5]
  console.log(arr);	// [1, 2, 3, 4]
    ```
    
    ```javascript
    let arr = [1, 2, 3, 4, [5, 6]];
    let copied = arr.slice();
    copied[4].push(7);
    
    console.log(copied);	// [1, 2, 3, 4, [5, 6, 7]]
    console.log(arr);	// [1, 2, 3, 4, [5, 6, 7]]
    ```

* **`Spread Operator`**

  * `Spread`는 *ES6*에 추가된 연산자다. 

    * 구문: `myFunction(...iterableObj);`

  * 배열, 문자열 등의 **이터러블**을 개별 요소로 분리한다. 마찬가지로 중첩된 객체는 복사하지 못한다.

    * `Array.prototype.slice`와 마찬가지로 내부에서 *for-loop*가 돌아가면서 값을 복사하는 방식이므로 이터러블 객체만 가능

    ```javascript
    let arr = [1, 2, 3, 4];
    let copied = [...arr];
    copied.push(5);
    
    console.log(copied);	// [1, 2, 3, 4, 5]
    console.log(arr);	// [1, 2, 3, 4]
    ```

    ```javascript
    let arr = [1, 2, 3, 4, [5, 6]];
    let copied = [...arr];
    copied[4].push(7);
    
    console.log(copied);	// [1, 2, 3, 4, [5, 6, 7]]
    console.log(arr);	// [1, 2, 3, 4, [5, 6, 7]]
    ```

  * spread는 다양하게 활용된다. [링크](https://seongbeom.github.io/2017/02/08/uses-of-spread-operator.html)에 예시들이 잘 정리되어 있다.

  ```javascript
  // Set(), Map() 과 함께 많이 쓰인다.
  let arr = [1, 1, 2, 2, 3, 3];
  let mySet = [...new Set(arr)];
  
  console.log(mySet);	// [1, 2, 3]
  
  // 객체들을 결합시킬 때도 쓰인다.
  ```

  

  

* **`Object.assign`**

  

### 깊은 복사(deep copy)

* 깊은 복사

  * 주소를 복사하는 것이 아니라 값을 복사한다. 배열, 문자열 등의 **이터러블**을 개별 요소로 분리한다.
    * 해당 객체가 `Symbol.iterator`를 프로퍼티로 가지고 있다면 해당 객체가 어터러블 하다는 의미이므로 가능

* **`JSON.parse`**

  

