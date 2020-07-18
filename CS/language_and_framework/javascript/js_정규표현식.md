# javascript 정규표현식

### 정규표현식 리터럴

```javascript
var pattern = /a/;
var pattern = new RegExp('a');
// 위 둘은 같은 기능
```

### 정규표현식 메소드 실행

* RegExp.exec()
  * 필요한 정보를 추출
* RegExp.test()
  * 정보가 있는지 확인

```javascript 
var pattern = /a/;
console.log(pattern.exec('abcdef'));	// ["a"]

var pattern = /a./;	// .은 임의의 문자
console.log(pattern.exec('abcdef'));	// ["ab"]

console.log(pattern.exec('bcdef'));	// null

console.log(pattern.test('abcdef'));	// true
console.log(pattern.test('bcdef'));	// false
```



### 문자열 메소드 실행

* String.match()
* str.replace(pattern, 'A');

```javascript
var pattern = /a/;
var str = 'abcdef';
str.match(pattern);	// ["a"]

var str = 'bcdef';
str.match(pattern);	// null

var str = 'abcdef';
str.replace(pattern, 'A');	// "Abcdef" 
```



### 옵션

* i
  * 대소문자를 구분하지 않음
* g
  * global

```javascript
var xi = /a/;
"Abcde".match(xi);	// null

var oi = /a/i;
"Abcde".match(oi);	// ["A"]

var xg = /a/;
"abcdea".match(xg);	// ["a"]

var og = /a/g;
"abcdea".match(og);	// ["a", "a"]

var ig = /a/ig;
"AabcdAa".match(ig);	//	["A", "a", "A", "a"]
```



###  캡처

* 그룹을 지정하고 해당 그룹을 사용하는 기능

* 괄호: 그룹
* \w: 문자(A~Z, a~z, 0~9)
* ''+'' : 수량자 
* \s: 공백
* $: 그룹(괄호)을 선택

```javascript
var pattern = /(\w+)\s(\w+)/;
var str = "coding everybody";
var result = str.replace(pattern, "$2, $1");
console.log(result);	// everybody, coding
```



### 치환

```javascript
var urlPattern = /\b(?:https?):\/\/[a-z0-9-+&@#\/%?=~_|!:,.;]*/gim;
var content = '생활코딩 : http://opentutorials.org/course/1 입니다. 네이버 : http://naver.com 입니다. ';
var result = content.replace(urlPattern, function(url){
    return '<a href="'+url+'">'+url+'</a>';
});
console.log(result);
```





[정규표현식 빌더](https://regexr.com/)

[정규표현식 시각화](https://regexper.com/)