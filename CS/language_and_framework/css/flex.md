# flex

### 개요

* flex는 css 레이아웃을 보다 쉽게 잡아주기 위한 도구

* 기본적으로 다음과 같은 구조를 가짐

  ```html
  <container>
  	<item></item>
  	<item></item>
  </container>
  ```

* 각각의 속성들은 태그에 따라 구분되어 있음. 상위 태그인 Container와 item

  * Container
    * `display`
    * `flex-direction`
    * `flex-wrap`
    * `flex-flow`
    * `justify-content`
    * etc
  * item
    * `order`
    * `flex-grow`
    * `flex-shrink`
    * `flex-basis`
    * `flex`
    * etc



### flex 기본

* flex를 적용하지 않은 경우

  * 각각  item 태그들은 block-level element로 화면 전체를 사용함

  ```css
  .container{
      background-color: powderblue;
      /* display:flex; */
  }
  
  .item{
      background-color: tomato;
      color: white;
      border: 1px solid white;
  }
  ```

  <img src="https://user-images.githubusercontent.com/46865281/89726085-8235ee00-da51-11ea-928f-c315f279580e.png" width="500" height="150">

* flex를 적용한 경우

  * container에 flex를 줬음

  ```css
  .container{
      background-color: powderblue;
      display:flex;
  }
  
  .item{
      background-color: tomato;
      color: white;
      border: 1px solid white;
  }
  ```

  <img src="https://user-images.githubusercontent.com/46865281/89726095-937efa80-da51-11ea-8860-1fdb5351ac35.png" width="550" height="80">

* flex-direction: row 이용

  * 옵션을 주지 않아도 디폴트로 `flex-direction: row` 상태임.

  ```css
  .container{
      background-color: powderblue;
      display:flex;
      flex-direction: row-reverse;
  }
  
  .item{
      background-color: tomato;
      color: white;
      border: 1px solid white;
  }
  ```

  <img src="https://user-images.githubusercontent.com/46865281/89726209-db525180-da52-11ea-92e3-a8149bfebb2d.png" width="560" height="90">

* flex-direction: row 이용

### REFERENCES

* [생활코딩](https://opentutorials.org/course/2418/13526)