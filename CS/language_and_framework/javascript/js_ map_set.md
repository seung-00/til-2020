# Javascript Map, Set

## 개요

* Map과 Set은 ES6에 추가된 컬랙션이다.
* 특정 상황에서 Map과 Set은 기존의 Object 와 Array 보다 좋은 선택지가 된다.
  * 기존 컨테이너와 유사한 역할을 하지만 장단이 있다. 따라서 적재적소에 사용하는 것이 중요



##  Map

> ECMAScript 2015 introduces a new data structure to map values to values. A `Map` object is a simple key/value map and can iterate its elements in insertion order.

* Map은 key와 value를 매핑하기 위한 자료구조다.

* 다음과 같은 기능, 문법을 가지고 있다.

  ```javascript
  var sayings = new Map();
  sayings.set("dog", "woof");
  sayings.set("cat", "meow");
  sayings.set("elephant", "toot");
  sayings.size; // 3
  sayings.get("fox"); // undefined
  sayings.has("bird"); // false
  sayings.delete("dog");
  
  for (var [key, value] of sayings) {
    console.log(key + " goes " + value);
  }
  // "cat goes meow"
  // "elephant goes toot"
  ```

### Map과 Object 비교

* 자바스크립트의 Object 역시 key-value로 이루어진 자료구조로 해시맵으로 많이 사용되고 있다.
  * 그렇다면 Map과 Object의 차이는 무엇인가?

1. key 의 유형

   * Object는 String과 Symbol만을 키로 가질 수 있다.

   * Map은 어떤 타입의 값도 키로 줄 수 있다.

     ```javascript
     const map = new Map();
     map.set(1, "test");
     console.log(map.get(1));
     // test
     ```

2. size

   * Object는 프로퍼티의 개수를 확인하기 불편하다(`size()`, `lenght() ` 같은 메서드가 없다.)

   * Map은 `size` 프로퍼티를 제공한다.

     ```javascript
     const map = new Map();
     map.set("k1", 1);
     map.set("k2", 2);
     map.set("k3", 3);
     map.size;
     // 3
     ```

3. 순회

   * Map은 iterable 객체로 반복문을 수행하기에 편하다.

   *  [key, value]로 반환해주는 `for-of` 문법을 사용할 수 있다.

     * `forEach()` 도 사용 가능하다.

     ```javascript
     const map = new Map();
     map.set("k1", 1);
     map.set("k2", 2);
     map.set("k3", 3);
     
     for (let [key, value] of map) {
       console.log(`${key} : ${value}`);
     }
     k1 : 1
     k2 : 2
     k3 : 3
     ```

4. 프로토타입 체인 

   * Object는  프로토타입 체인으로 의도하지 않은 키에 접근할 위험이 있다
   * Map은 명시적으로 제공한 키 이외에는 어떤 키도 가지지 않는다.

5. 성능

   * Map은 잦은 key-vlaue의 추가, 제거, 조회에 더 좋은 성능을 보인다.

     



### REFERENCES

* [MDN](https://developer.mozilla.org/ko/)
* 

