[TOC]

## HTML - FE

### HTML tags

* 태그는 의미에 맞춰서 사용해야 함
  * 링크
  * 이미지
  * 목록
  * 제목
* 편리한 단축키(tag + tab, tag*4)

  * 응용

    `div>ul>li*2` + tab

### Layout 태그

- header
- section
- nav
- footer
- aside

<img src="https://cphinf.pstatic.net/mooc/20171231_41/15146999078486r8Pv_JPEG/5086.HTML5PageLayout_2.jpg" alt="img" style="zoom:67%;" />



## CSS - FE

* [[생활코딩]css 기초]([https://github.com/SeungYoungOh/TIL/blob/master/CS/web/%5B%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9%5D%20css%20%EA%B8%B0%EC%B4%88.md](https://github.com/SeungYoungOh/TIL/blob/master/CS/web/[생활코딩] css 기초.md)) 참고


### CSS 선언 방법

* style을 html 페이지에 적용하는 3가지 방법

  1. inline

     ```html
     <!DOCTYPE html>
     <html>
       <meta charset = "utf-8" />
       <titel>World !</titel>
       <body>
         <span style="color:red"> Hello world!</span>
       </body>
     </html>
     ```

     * html 태그 안에다가 넣는 방법

     * 다른 방법들보다 우선 순위가 빠름

     * 구조를 표현하는 html 속에 스타일이 섞이기 때문에 권장되는 방법은 아님

       

  2. internal

     ```html
     <!DOCTYPE html>
     <html>
       <head>
         <meta charset="utf-8" />
         <title>World !</title>
         <style>
           p{
             font-size: 2em;
             color:red;
           }
         </style>
       </head>
     </html>
     ```

     * 헤드에 스타일 태그를 지정해서 선언

     * 별도의 css 파일을 관리하지 않아도 됨

     * 서버에 css 파일을 부르기 위해 별도의 브라우저가 요청을 보낼 필요가 없음

     * 그러나 마찬가지로 구조와 스타일이 섞이게 되므로 유지보수가 어려움

       

  3. external

     ```html
     <!DOCTYPE html>
     <html>
       <head>
         <meta charset="utf-8"/>
         <title>World !</title>
         <link rel="stylesheet" href="sytle.css"/>
       </head>
         
     </html>
     ```

     * 보통 제일 많이 쓰이는 방법



### CSS 상속

```html
<html>
    <head>
        <style>
            div{
                color:green;
                border:2px solid slategray;
                padding:5px;
            }

            div>ul>li>div>p{
                color:red;
            }
        </style>
    </head>
    <body>
      <div>
          <span>my test is upper!</span>
          <ul>
              <li>
                  <span>my text is dummy</span>
                  <div>
                      <p>
                          What makes me bearable makes me unbearable.
                      </p>
                      <p>
                          But man is not made for defeat
                      </p>

                  </div>
              </li>
              <li></li>
          </ul>
      </div>        
    </body>
</html>
```

* border, padding과 같은 레이아웃과 관련된 속성들[^2] 은 하위 엘리먼트로 상속을 받지 않음.

[^2]:box-model이라고 불리는 속성들(width, height, margin, padding, border)



* **cascading**

  CSS는 **경쟁**에 의해서 적절한 스타일이 반영됨

  1. 선언 방식에 의한 차이

     inline>internal=external

  2. 동일하면 나중에 것

  3. 더 구체적으로 표현한 것

     `body>span{...}`이 그냥 `span{...}` 보다 우선순위 높음

  4. id > class > element



### CSS selector

* element에 style을 지정하기 위해 tag, id, class 선택지가 존재

  * tag로 지정

    ```html
    <style>
         span {
           color : red;
         }
     </style>
    
    <body>
         <span> HELLO World! </span>
    </body>
    ```

    

  * id로 지정

    ```html
    <style>
         #spantag {
           color : red;
         }
    </style>
    
    <body>
         <span id="spantag"> HELLO World! </span>
    </body>
    ```

    

  * class로 지정

    ```html
    <style>
         .spanClass {
         color : red
         }
    </style>
    
    <body>
         <span class="spanClass"> HELLO World! </span>
    </body>
    ```

    

* 활용

  * 그룹 지정

    ```html
    <style>
      span, #test{
        color:green;
        border:2px solid slategray;
        padding:5px;
      }
    </style>
    
    <body>
      <div>
        <span>my test is upper!</span>
        <h id = "test">my text is dummy</span>
      </div>
    </body>
    ```

    

  * 자식 선택

    ```html
    <style>
    #jisu > span { color : red }
    </style>
    
    <div id="jisu">
      <div>
        <span> span tag </span>
      </div>
      <span> span tag 2 </span>
    </div>
    
    ```

    



### CSS 기본 Style 변경

* 색상 변경

  * 색상은 rgb, 16진수를 기본으로 표현한다

    `color: rgb(255,0,0)` == `color:#ff0000` 후자 방식은 #ff00까지만 표현해도 됨

  * em은 폰트 사이즈의 배수

  ```html
  <html>
    <head>
  		<style>
        body > div{
          font-size: 16px;
          background-color: #ff0;
          font-family:monospace;
          
        }
        
        .myspan{
          color: #f00;
          font-size:2em;
        }
      </style>
    </head>
    <body>
      <div>
        <span class = "myspan">my text is upper!</span>
      </div>
    </body>
  </html>
  ```



### Element가 배치되는 방법(CSS layout)

* 엘리먼트를 화면에 배치하는 것을 layout 작업 혹은 Rendering 과정이라고 함

* 엘리먼트는 위에서 아래로 순서대로 블럭을 이루며 배치되는 것이 기본

* 하지만 다양한 표현을 위해 css는 추가적인 속성을 제공함

  * **display(block, inline, inline-block)**

    1. 블록으로 쌓이는 엘리먼트(display:block)

       ```html
       <html>
           <head>
               <style>
                   div,p{
                       width:100px;
                       height:100px;
                       border:1px solid gray;
                   }
               </style>
           </head>
           <body>
               <div>block1</div>
               <p>block2</p>
               <div>block3</div>
           </body>
       </html>
       ```

       display 속성이 block이거나 inline-block인 경우 화면에서 위에서 아래로 쌓이듯이 채워짐. 높이 값을 주면 더 높은 크기로 엘리먼트가 쌓임.

       대부분 block 속성이므로 inline 속성인 태그를 외울 것

       

    2. 옆으로 흐르는 엘리먼트(display: inline)

       ```html
       <html>
           <head>
               <style>
                   span,a,strong{
                       border: 1px solid gray;
                   }
               </style>
           </head>
           <body>
               <span>좌우로 배치</span>
               <a>링크는 ?</a>
               <strong>링크도 강조도 모두 좌우로 배치</strong>
           </body>
       </html>
       ```

       높이와 넓이 지정은 반영이 안 됨

       명시적으로 `display:block` `display:inline`을 줄 수도 있다.

       

  * **position(static, absolute, relative, fixed)**

    ```html
    <html>
        <head>
            <style>
                .wrap{
                    position:relative;
                }
    
                .wrap>div{
                    width:150px;
                    height:100px;
                    border:1px solid gray;
                    font-size: 0.7em;
                    text-align: center;
                    line-height: 100px;
                }
    
                .relative{
                    position:relative;
                    left:10px;
                    top:10px;
                }
    
                .absolute{
                    position:absolute;
                    left:130px;
                    top:30px;
                }
                .fixed{
                    position:fixed;
                    top:250px;
                }
                
            </style>
        </head>
        <body>
            <div class="wrap">
                <div class="static">static(default)</div>
                <div class="relative">relative(left:10px)</div>
                <div class="absolute">absolute(left:130px top:30px)</div>
                <div class="fixed">fixed(top:250px)</div>
            </div>
        </body>
    </html>
    ```

    

    1. 디폴트는 static 으로 그냥 순서대로 배치

       

    2. absolute는 기준점에 따라서 특별한 위치에 배치
       top / left / bottom으로 설정

       기준점을 상위 엘리먼트에서 단계적으로 찾는데, static이 아닌 position이 기준이 됨

       위 코드에서 보면, absolute의 상위에 wrap이 있고 static이 아님

       따라서 wrap이 기준점이 됨

       

    3. relative는 원래 자신이 위치해야 할 곳을 기준으로 이동

       top / left / right / bottom

       

    4. fixed는 viewpoint(전체화면)좌측, 맨위를 기준으로 동작

       (예: 광고)

       

  * **margin**

    간격을 다르게 해서 배치함

    ```html
    <html>
        <head>
            <style>
                *{
                    border:1px solid gray;
                }
    
                .bottom{
                    margin-top:10px;
                    margin-left:100px;
                }
            </style>
        </head>
        <body>
            <div>left</div>
            <div class="bottom">bottom</div>
        </body>
    </html>
    ```

    

  * **기본 배치에서 벗어나서 떠있기(float: left)**

    ```html
    <html>
        <head>
            <style>            
            div{
                width:100px; height:100px;
                border:1px solid gray;
                font-size:0.7em;
            }
            .blue{
                background-color:blue;
            }
            .green{
                float:left;
                background-color:green;
            }
            .red{
                background-color:red;
                /*숨겨진 녹색을 드러내기 위해 relative로 옮김*/
                position:relative;
                left:10px
            }
            </style>
        </head>
        <body>
            <div class="wrap">
                <div class="blue"></div>
                <div class="green"></div>
                <div class="red"></div>
            </div>
        </body>
    </html>
    ```

    레이아웃을 쌓이지 않게 배치시킬 때 이용됨

    

  * **하나의 블록 엘리먼트는 box 형태임 (box-model)**

    ![image](https://user-images.githubusercontent.com/46865281/75608293-a526b280-5b41-11ea-88fd-8aa168db034b.png)

    ```html
    <html>
        <head>
            <style>            
            div{
                background-color: lightgrey;
                width: 300px;
                border: 25px solid green;
                padding: 25px;
                margin: 25px;
            }
            </style>
        </head>
        <body>
            <div>
                okay, let me see.. what am I supposeed to say?
                this is my text that tests css syntax.
            </div>
        </body>
    </html>
    ```

    

    * 패딩 값을 늘리는 경우, 박스가 깨질 수가 있음

      box-sizing 값을 넣어줘서 이를 방지할 수 있음.

      예를 들어 아래의 코드에서 padding을 키워도 border-box는 원래 크기를 유지하려고 함(box-size가 border-box이므로)

      ```html
      <html>
          <head>
              <style>            
              div{
                  width:100px;
                  height:100px;
                  border:1px solid red;
                  padding:10px;
                  font-size:0.8em;
              }
      
              .box-content{
                  box-sizing:content-box;
              }
              
              .box-border{
                  box-sizing:border-box;
              }
              </style>
          </head>
          <body>
              <div class="box-content">
                  box-content<br>(100px보다 커짐)
              </div>
              <div class="box-border">
                  box-border<br>(100px 유지)
              </div>
          </body>
      </html>
      ```

      

* layout 구현 방법은?

  1. 전체 레이아웃은 float을 잘 사용해서 2단, 3단 컬럼 배치를 구현

  최근 css-grid, flex 속성 등을 쓰기도 함

  2. 특별한 위치를 배치하기 위해 position absolute를 사용함(기준점 relative)

  3. 네비게이션과 같은 엘리먼트는 inline-block을 써서 가로로 배치하기도 함
  4. 엘리먼트 안의 텍스트 간격과 다른 엘리먼트 간의 간격은 padding과 margin 속성을 잘 활용해서 위치시킴