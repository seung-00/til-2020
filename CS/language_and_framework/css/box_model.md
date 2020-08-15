# css 박스 모델

<img src="https://poiemaweb.com/img/box-model.png" width="500" height="300">

* 박스 모델은 웹 페이지 레이아웃에 사용되는 컨테이너임. HTML 태그들은 모두 박스 모델을 가지고 있음
  * margin, border, padding, content을 포함함

* content
  * 실제 내용(html 태그)이 차지하는 공간
  * width, height에 의해 크기 결정됨
* padding
  * border 안쪽에 위치하는 내부 여백
  * `padding: x;` 로 패딩 영역 두께를 지정 가능
  * 배경의 컬러, 이미지는 패딩 영역까지 적용됨
* border
  * 테두리 영역
  * `border: x;` 로 테두리의 두께 지정 가능
* margin
  * 테두리 바깥에 위치하는 외부 여백
  * `margin: x;` 로 마진 영역 두께 지정 가능
  * 배경색 지정 불가

### REFERENCES

* [poiemaweb](https://poiemaweb.com/css3-box-model)