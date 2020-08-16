# css position

* position 속성은 html 태그 요소들을 문서에 배치하는 방법을 결정한다.
  * position의 값으로 위치 지정 요소 **static(default), relative, absolute, fixed, sticky**가 있다.
    * 좌표 프로퍼티 **top, right, bottom, left** 가 최종 위치를 결정한다.

<img src="https://poiemaweb.com/img/position.png" width="500" height="300">

### static

* position의 디폴트 값
* 위에서 아래로, 왼쪽에서 오른쪽으로 배치됨
* 부모 요소가 있을 때 부모 요소의 위치를 기준으로 배치됨
* 좌표 프로피터를 사용할 수 없음



### relative

* 좌표 프로퍼티를 사용하여 최종 위치 결정
  * 동일 position의 태그가 겹칠 때 나중에 나온 태그가 더 위에 배치됨
    * z-index 속성으로 조절 가능
  * 이상은 static을 제외한 태그들(relative, absolute, fixed)에서 동일하게 적용됨 
* 이외에는 static과 동일



### absolute

* static 을 제외한 프로퍼티(relative, absolute, fixed)를 가지고 있는 부모 요소를 기준으로 위치가 결정된다.

* 만약 조상 중에 위에 해당되는 태그가 없다면 documnet body가 기준이 된다.

* 예제

  * html

    ```html
    <div>
      <div id="absolute">absolute</div>
    </div>
    <div id="parent">
      <div id="child">children</div>
    </div>
    ```

  * css

    ```css
    #absolute {
      background: yellow;
      position: absolute;
      right: 0;
    }
    
    #parent {
      position: relative;
      width: 1000px;
      height: 100px;
      background: skyblue;
    }
    
    #child {
      position: absolute;
      right: 100px;
    }
    ```

  * 결과

    * #absolute는 documnet body를 기준으로 right에 의해 위치가 정해짐
    * #child는 #parent를 기준으로 right에 의해 위치가 정해짐
    * width는 content에 맞게 변화되므로 적절한 값을 지정해야 한다.

    <img src="https://user-images.githubusercontent.com/46865281/90326786-891bae00-dfc7-11ea-88a9-d6a81321fbdb.png" width="550" height="100">

### fixed

* 브라우저의 vidwport를 기준으로 배치시킨다. 최종 위치는 좌표 프로피터로 결정된다.
* 스크롤과 상관없이 항상 같은 곳에 위치한다. 
  * 광고 등에 사용됨
* width는 content에 맞게 변화되므로 적절한 값을 지정해야 한다.



### REFERENCE

* [poiemaweb](https://poiemaweb.com/css3-box-model)
* [MDN](https://developer.mozilla.org/ko/docs/Web/CSS/position)