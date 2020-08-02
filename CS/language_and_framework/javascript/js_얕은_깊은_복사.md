# 얕은 복사, 깊은 복사

* 얕은 복사, 깊은 복사는 다른 언어들에서도 중요한 내용이다. *JS* 는 다른 언어들보다 비교적 방법이 다양한듯 하다.

## 얕은 복사(shallow copy)

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



### `Array.prototype.slice()`

* 배열의 안에 값을 꺼내 복사할 때 많이 쓰이는 방식이다. 중첩된 배열까지 복사하지는 못하므로 얕은 복사에 속한다.

  * 내부에서 *for-loop*가 돌아가면서 값을 복사한다.
  
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
  // fail!
  ```



### `Object.assign()`

* `Object.assign()`은 두 객체를 병합하는 메소드다. 마찬가지로  중첩된 객체는 깊은 복사하지 못한다.
  * 구문: `Object.assign(target, ...sources)`
    
    * `target`: 대상 객체, `srouces`: 하나 이상의 출처 객체
    
  * 일치하는  *key*가 있을 때 해당  *value* 를 대체하는 방식이다.
  
    

### `Spread Operator()`

* `Spread`는 *ES6*에 추가된 연산자다. 

  * 구문: `myFunction(...iterableObj);`

* 배열, 문자열 등의 **이터러블**을 개별 요소로 분리한다. 마찬가지로 중첩된 객체는 깊은 복사하지 못한다.

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
  // fail!
  ```

* `spread`는 다양하게 활용된다. [링크](https://seongbeom.github.io/2017/02/08/uses-of-spread-operator.html)에 예시들이 잘 정리되어 있다.
  * 깊이 1 복사
    * `let copied = [... arr];`
  * 배열, 객체 결합
    * `let sumObj = {...obj1, ...obj2};`
  * `Set()`, `Map()`과 사용
    * `let mySet = [... new Set(arr)];`



## 깊은 복사(deep copy)

* 깊은 복사

  * 객체의 주소를 복사하는 것이 아니라 값을 복사한다. 중첩 구조까지 모두 값을 복사한다.


### `JSON.parse(), JSON.stringify()`

* `JSON.parse()` 는 JSON 문자열의 구문을 분석하고, 그 결과에서 값이나 객체를 생성한다.

  ```javascript
  console.log(JSON.stringify({ a: 1, b: 2 }));
  // {"a":1,"b":2}
  ```

* `JSON.stringify()` 메소드는 값이나 객체를 JSON 문자열로 변환한다.

* `JSON.parse()` 와 `JSON.stringfy()`를 함께 사용하면 깊은 복사를 쉽게 해결할 수 있다.

  ```javascript
  let arr = [1, 2, 3, 4, [5, 6]];
  let copied = JSON.parse(JSON.stringify(arr));
  copied[4].push(7);
  
  console.log(copied);	// [1, 2, 3, 4, [5, 6, 7]]
  console.log(arr);	// [1, 2, 3, 4, [5, 6]]
  // succses!
  ```

* 이것이 가능한 이유는 `JSON.stringify()` 로 객체를  문자열로 변환한 뒤 넘기기 때문이다. 즉  참조형 타입인 객체가 아니라 원시형 타입인 문자열로 값을 넘기기 때문에 깊은 복사가 가능하다.

* `JSON.parse()` 을 이용한 깊은 복사는 권장하는 방식은 아닌데, 몇 가지 이유가 있다. 

  * *JOSN*으로 표현될 수 있는 값은 한정되어 있다. (*ECMA-404* 라는 명세로 이들을 따로 분류하고 있다)

    * *object, array, number, string, true, false, null*

  * 다른 방법들에 비해 속도가 느리다.

    * 깊은 복사는 값을 복사하므로 기본적으로 얕은 복사보다 속도가 느릴 수 밖에 없다. 특히 객체의 크기가 클수록 오버헤드가 증가할 것이다. 그런데 `JSON.parse()`는 깊은 복사 방법 중에서도 성능이 안 좋다.

      

### `Lodash| _.cloneDeep()`

* `Lodash` 라이브러리는 얕은 복사를 위한 `_clone()`과 깊은 복사를 위한  `_cloneDeep()`을 제공한다.

  * 구문: `_.cloneDeep( value )`
  * value 의 타입을 체크하면서 필요한 경우 재귀적으로 중첩된 객체를 복사하는 방식이다.

  ```javascript
  const _ = require('lodash');
  let arr = [1, 2, 3, 4, [5, 6]];
  let copied = _.cloneDeep(arr);
  
  copied[4].push(7);
  
  console.log(copied);	// [1, 2, 3, 4, [5, 6, 7]]
  console.log(arr);	// [1, 2, 3, 4, [5, 6]]
  // succses!
  ```

  

### REFERENCES

[MDN](https://developer.mozilla.org/ko/)

[GeeksforGeeks](https://www.geeksforgeeks.org/)

[깊은 복사와 얕은 복사에 대한 심도있는 이야기]([https://medium.com/watcha/%EA%B9%8A%EC%9D%80-%EB%B3%B5%EC%82%AC%EC%99%80-%EC%96%95%EC%9D%80-%EB%B3%B5%EC%82%AC%EC%97%90-%EB%8C%80%ED%95%9C-%EC%8B%AC%EB%8F%84%EC%9E%88%EB%8A%94-%EC%9D%B4%EC%95%BC%EA%B8%B0-2f7d797e008a](https://medium.com/watcha/깊은-복사와-얕은-복사에-대한-심도있는-이야기-2f7d797e008a))