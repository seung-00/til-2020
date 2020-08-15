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



## flex 기본

* 다음과 같은  html 코드를 가지고  css 예제를 적용해본다.

  ```css
  <!doctype>
  <html>
  <head>
      <meta charset = "utf-8" />
      <link rel="stylesheet"
      href="./style.css"/>
  </head>
  <body>
      <div class="container">
          <div class="item">1</div>
          <div class="item">2</div>
          <div class="item">3</div>
          <div class="item">4</div>
          <div class="item">5</div>
      </div>
  </body>
  </html>
  ```

  

### Container

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
  * `row-reverse` 는 아래와 같이 우측부터 정렬됨

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

* flex-direction: column

  * `flex-direction: row`는 수평으로 item을 쌓았다면 `flex-direction: column`은 수직으로 쌓음

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

  

  <img src="https://user-images.githubusercontent.com/46865281/89734853-a87f7c00-da99-11ea-91b2-9fba0711dde5.png" width="450" height="250">

  * 위 결과를 보고 block-level element (flex를 적용하지 않은 경우)와 차이가 없다고 생각할 수 있음. 실제로 `flex-direction: column` 역시 화면 전체를  *width*로 사용함.
  * 그러나 *height* 값을 주는 경우 차이를 확인할 수 있는데, flex는 item들이 container의 *height*, *width* 를 기준으로 정렬됨.
  * 아래 코드와 사진은 `direction: column-reverse` 를 적용한 결과임

  ```css
  .container{
      background-color: powderblue;
      display:flex;
      height: 200px;
      flex-direction: column-reverse;
  }
  
  .item{
      background-color: tomato;
      color: white;
      border: 1px solid white;
  }
  ```

  <img src="https://user-images.githubusercontent.com/46865281/89734873-c0570000-da99-11ea-8189-5ada248a5467.png" width="500" height="300">

### item

* flex-basis

  * flex 방향에 따르는  item 크기를 결정
  * nth-child(n)으로 n 번째 아이템 지정

  ```css
  .container{
      background-color: powderblue;
      display:flex;
      height: 200px;
      flex-direction: row;
  }
  
  .item{
      background-color: tomato;
      color: white;
      border: 1px solid white;   
  }
  
  .item:nth-child(2){
      flex-basis: 200px;
  }
  ```

  <img src="https://user-images.githubusercontent.com/46865281/89780956-5c8e0f00-db4d-11ea-9ef6-260c2f95b79c.png" width="600" height="170">

  * flex-direction: column일 경우는 다음과 같음

    <img src="https://user-images.githubusercontent.com/46865281/89781778-ed191f00-db4e-11ea-9362-a713add52eca.png" width="600" height="170">

  

* **flex-grow**

  * 전체 컨테이너(여백을 포함)을 채우는 것, flex에서 중요한 기능임.
  * `flex-grow:1`을 하는 경우, 전체를 item으로 균등하게 채운다. 즉 item이 6개니까 컨테이이 너비의 1/6 만큼 아이템 너비가 결정된다.

  ```css
  .container{
      background-color: powderblue;
      display:flex;
      height: 200px;
      flex-direction: row;
  }
  
  .item{
      background-color: tomato;
      color: white;
      border: 1px solid white;
      flex-grow:1;   
  }
  ```

  <img src="https://user-images.githubusercontent.com/46865281/89782631-a62c2900-db50-11ea-80e4-129a11dd2438.png" width="600" height="170">

   * 만약, 아래의 코드 처럼 두 번째 아이템에 `flex-grow:2` 를 준다면 캐스캐이딩으로 두 번째 아이템 크기가 `flex-grow:2` 로 결정된다.
   * 이 경우 두 번째 아이템은 **2/6** 만큼의 너비를 가지게 된다.
  
  ```css
  .container{
      background-color: powderblue;
      display:flex;
      height: 200px;
      flex-direction: row;
  }
  
  .item{
      background-color: tomato;
      color: white;
      border: 1px solid white;
      flex-grow:1;   
  }
  
  .item:nth-child(2){
      flex-grow:2;   
  }
  ```
  
  <img src="https://user-images.githubusercontent.com/46865281/89782233-d7f0c000-db4f-11ea-8b60-8a083a888039.png" width="600" height="170">

* **flex-shrink**

  * shrink는 grow와 반대로  크기가 줄어드는 규칙을 결정한다. (`flex-basis` 로 크기가 정해져 있을 때)

  * 디폴트로 브라우저 화면을 줄일 때 여백이 없다면 item의 크기를 줄인다.

    ```css
    .container{
        background-color: powderblue;
        height:200px;
        display:flex;
        flex-direction:row;
    }
    .item{
        background-color: tomato;
        color:white;
        border:1px solid white;         
    }
    
    .item:nth-child(2){
        flex-basis: 1700px;
    }
    ```

  * shrink 속성을 0으로 준다면 해당 아이템의 크기는 처음 설정한 그대로 줄어들지 않는다. 1이면 디폴트 그대로임!

    ```css
    .container{
        background-color: powderblue;
        height:200px;
        display:flex;
        flex-direction:row;
    }
    .item{
        background-color: tomato;
        color:white;
        border:1px solid white;         
    }
    
    .item:nth-child(2){
        flex-basis: 1700px;
        flex-shrink: 0;
    }
    ```

  * 아래와 같이 두 아이템에  shrink 값을 다르게 준다면 어떻게 될까?? grow에서처럼 값에 따라서 그만큼 줄어드는 비율이 결정된다. 

    ```css
    .container{
        background-color: powderblue;
        height:200px;
        display:flex;
        flex-direction:row;
    }
    .item{
        background-color: tomato;
        color:white;
        border:1px solid white;         
    }
    .item:nth-child(1){
        flex-basis: 150px;
        flex-shrink: 1;
    }
    .item:nth-child(2){
        flex-basis: 150px;
        flex-shrink: 2;
    }
    ```

### Holy Grail Layout

* 아래와 같은 레이아웃을 Holy Grail(성배) Layout이라 한다. 성배를 찾기 위해 노력하듯 많은 사람들이 도전했던 레이아웃이라는 의미다. flex는 아래와 같은 레이아웃을 세련되고 간결한 방법으로 구성할 수 있다.

  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/HolyGrail.svg/440px-HolyGrail.svg.png" width="400" height="300">

 *  html

     * 아래와 같은  html로 레이아웃을 구성해보자.

    ```html
    <!doctype>
    <html>
    <head>
        <meta charset = "utf-8" />
        <link rel="stylesheet"
        href="./style.css"/>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>읽거나 적거나</h1>
            </header>
            <section class = "content">
                <nav>
                    <!-- navigation -->
                    <ul>
                        <li>html</li>
                        <li>css</li>
                        <li>js</li>
                    </ul>
                </nav>
                <main>
                    읽고 공부한 것들을 적습니다
                </main>
                <aside> 
                    <!-- aside는 부가적인 내용 -->
                    AD
                </aside>    
            </section>
            <footer>
                <a href="https://seung00.tistory.com/">블로그</a>
            </footer>
        </div>
    </body>
    </html>
    ```

    

* container에 그냥 `disply:flex` 만 준 경우 아래 그림과 같이 수평으로 구성될 것이다.

  <img src="https://user-images.githubusercontent.com/46865281/89787578-a8928100-db58-11ea-9fc0-a544dbf4bf7d.png" width="700" height="200">

* 디폴트로 `flex-direction: row` 상태이므로 그렇다.  `flex-direction: column` 으로 수직으로 쌓이게 바꿔준다.

* `header`와 `footer`에 `border-top`, `border-botoom` 속성을 줘서 구분선을 만든다.

* 이제 `nav`, `main`, `aside` 가 수평으로 쌓이도록 `content` 태그에 `display:flex`를 준다.

  * 수평으로 쌓인 아이템들에 `border`로 구분선을 만든다.

* 메인 양쪽의 네비게이션, AD 의 크기를 고정시킨다.

  * `flex-basis`, `flex-shrink` 속성을 준다.

  <img src="https://user-images.githubusercontent.com/46865281/89790659-35d7d480-db5d-11ea-9871-253c52ec704e.png" width="550" height="230">

### REFERENCES

* [생활코딩](https://opentutorials.org/course/2418/13526)