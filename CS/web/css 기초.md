# CSS 기초

### style 속성

* style 속성 속에는 css가 온다

  ```html
  <h1 style = "background-color: powderblue; color: white">Central Limit Theorem</h1>
  
  ```

  

* div, span 태그

  * css로 특정 문구를 제어하기 위한 태그, 이때  div는 줄바꿈이 생긴다.

    ```html
    <p>확률론과 통계학에서, <span style="font-weight: bold;">중심 극한 정리(中心 極限 定理, 영어: central limit theorem, 약자 CLT)</span>는
    ```

* 선택자

  * 선택을 해주는 요소, 특정 요소들을 선택하여 스타일을 적용하게 해줌

    <img src="http://www.nextree.co.kr/content/images/2016/09/yrkim-140327-selector-04.png" alt="img" style="zoom:40%;" />

  * 참고 및 그림 출처: http://www.nextree.co.kr/p8468/

  ```html
          .js
          {
              color: green
          }
          #first
          {
              font-weight: bold;
            	color: red
          }    
  
  <p><span id="first">확률론</span>과 <span class = "js">통계학</span>에서, <span style class = "js">중심 극한 정리(中心 極限 定理, 영어: central limit theorem, 약자 CLT)</span>는 동일한 확률분포를 가진 독립 확률 변수 n개의 평균의 분포는 n이 적당히 크다면 정규분포에 가까워진다는 정리이다.
  ```

  * id 는 중복되지 않은 고유의 값, class는 좀 더 포괄적인 분류를 위한 값으로 쓰임. 따라서 두 선택자가 겹칠 시 id를 우선적으로 인식함.

    이처럼 선택자 간에 우선순위가 있음.



<span style = "color:blue">오호라</span>

