# flex 레이아웃

* [flexbox로 만들 수 있는 10가지 레이아웃](https://d2.naver.com/helloworld/8540176) 을 보고 정리한 내용입니다.

  * 문서의 그림들 역시 해당 포스팅에서 가져왔습니다.

    

### 부모 요소와 자식 요소에 정의하는 속성 구분

* 부모 속성(flex container)과 자식 속성(flex item)을 구분해야 함.

  - flex container 속성: `flex-direction`, `flex-wrap`, `justify-content`, `align-items`, `align-content`
  - flex item 속성: `flex`, `flex-grow`, `flex-shrink`, `flex-basis`, `order`

  <img src="https://d2.naver.com/content/images/2018/12/helloworld-201811-flex_02.png" width="600" height="300">

### container의 flex-direction

* flexbox 레이아웃에서 디폴트 주축은 수평 방향(왼쪽에서 오른쪽)
* `flex-direction: column`으로 주축의 방향을 수직으로 바꿀 수 있음



### item의 flex-grow

* 아이템의 확장을 관리한다. 0과 양의 정수를 속성값에 사용한다.
* 값이 0인 경우 컨테이너 크기와 상관없이 설정된 크기를 유지한다.
* 값이 1 이상인 경우 아이템이 컨테이너를 채우도록 유지되며 컨테이너의 크기에 따라 아이템의 크기도 달라진다.
* 1 이상의 값들은 아이템들의 flex-basis를 제외한 여백 부분을 특정 비율로 나눠가지게 한다.



### item의 flex-shrink

* 아이템의 축소를 관리한다. 0과 양의 정수를 속성값에 사용한다. 디폴트값은 1
* 값이 0인 경우 컨테이너 크기와 상관없이 설정된 크기를 유지한다.
* 값이 1 이상인 경우 컨테이너의 크기에 따라 아이템의 크기도 달라진다.



### item의 flex-basis

* 아이템의 기본 크기를 결정한다. 디폴트값은 auto
* width 속성에 사용되는 모든 단위(px, %, em,등)를 속성값에 사용할 수 있다.
* 값이 0인 경우 아이템은 absolute flex item이 되어 컨테이너를 기준으로 크기가 결정된다.
  * flex-basis 속성값을 0으로 선언할 때에는 `flex-basis: 0px `과 같이 단위도 같이 설정해야 함.
* 값이 auto인 경우 아이템은  relative flex item이 되어 콘텐츠의 크기에 따라 크기가 결정됨



### item의 flex: 1

* `flex: 1`은 `flex: 1 1 0`을 축약한 것이고, `flex: 1 1 0` 은 `flex-glow: 1; flex-shrink: 1; flex-basis: 0;`을 축약한 것이다.

  ````css
  .flex-item {
    flex:1;
    
    /* 아래와 동일
    flex: 1 1 0;
  
    flex-grow: 1;
    flex-shrink : 1;
    flex-basis: 0; 
    */
  }
  ````

* n이 임의의 양의 정수일 때 `flex: n`은 `flex: n 1 0 `을 의미한다. 즉 n은 flex-grow 속성값을 결정하고 flex-shrink:1, flex-basis:0은 고정된다.

  

### item의 flex: none 속성으로 크기 고정

* flex 속성의 디폴트 값은 `flex: 0 1 auto` 임

* item 크기를 고정하려면 `flex: none`  속성을 적용해야 함

  * `flex: none`은 `flex-grow: 0; flex-shrink: 0; flex-basis: auto;`을 축약한 것임




### item의 flex 속성 키워드

* flex 속성 키워드에 따라 축약되는 설정값들이 존재함

  * initial(기본값)
    * 컨테이너의 크기가 작아지면 아이템의 크기도 작아진다. 하지만 컨테이너의 크기가 커져도 아이템의 크기는 커지지 않는다. (flex-grow: 0, flex-shrink: 1)
  * none
    * 컨테이너 크기에 아이템이 영향을 받지 않는다.
  * auto
    * 컨테이너 크기에 맞추어 아이템의 크기가 커지거나 작아진다.
  * 양의 정수 n
    * 아이템들이 컨테이너 공간을 특정 비율로 나눠 가지면서(basis: 0) 컨테이너 크기에 따라 크기가 커지거나 작아진다.

  | flex            | flex-grow | flex-shrink | flex-basis |
  | --------------- | --------- | ----------- | ---------- |
  | initial(기본값) | 0         | 1           | auto       |
  | none            | 0         | 0           | auto       |
  | auto            | 1         | 1           | auto       |
  | 양의 정수 n     | n         | 1           | 0          |

  ​	<img src="https://d2.naver.com/content/images/2018/12/helloworld-201811-flex_13.png" width="600" height="300"> 

  

### margin: auto 속성으로 자식 요소 배치

* 요소의 바깥 여백(margin)을 설정하는 속성에 auto를 적용하면 flexbox에서 아이템을 쉽게 배치 가능

  * 예컨대, margin: auto 속성을 적용하면 아이템의 바깥 여백이 자동으로 확장되어 컨테이너의 가운데에 위치하게 됨 

* 아이템을 수평으로 배치할 때

  * `margin-right: auto` 바깥 여백이 오른쪽의 모든 공간을 차지하기 위해 아이템을 왼쪽으로 밈
  * `margin: 0 auto` 아이템을 수평 중앙에 위치시킴
  * `margin-left: auto` 아이템을 오른쪽으로 밈

  <img src="https://d2.naver.com/content/images/2018/12/helloworld-201811-flex_14.png" width="350" height="100">

* 아이템을 수직으로 배치할 때

  * `margin-bottom: auto` 아이템을 아래에서 위로 밈

  * `margin: auto 0` 아이템을 수직 중앙에 위치시킴

  * `margin-top: auto` 아이템을 위쪽에서 아래로 밈

    * 푸터를 만들 때 사용 가능 (레이아웃 3)

      

### container의 justify-content

* `justify-content` 는 주축을 기준으로 아이템을 수평으로 정렬한다. 

  * `justify-content: flex-start`(기본값): 주축의 시작 부분을 기준으로 flex item을 정렬한다.
  * `justify-content: center`: 주축의 중앙을 기준으로 flex item을 정렬한다.
  * `justify-content: flex-end`: 주축의 끝부분을 기준으로 flex item을 정렬한다.
  * `justify-content: space-around`: 주축을 기준으로 flex item을 일정한 간격으로 정렬한다.
  * `justify-content: space-between`: 첫 번째와 마지막 flex item은 주축의 시작 부분과 끝부분에 정렬하고 나머지 flex item을 일정한 간격으로 정렬한다.
    * 상단 메뉴를 만들 때 사용 가능 (레이아웃 4)

  <img src="https://d2.naver.com/content/images/2018/12/helloworld-201811-flex_19.png" width="600" height="100">

### REFERENCE

