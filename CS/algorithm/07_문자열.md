## 해싱

* 특정 항목을 검색하고자 할 때 탐색키를 이용하여 키가 있는 위치를 계산해 바로 찾아가는 방법

* 해시 함수: 탐색할 data를 해시 값으로 변환하는 함수

* 해시 테이블: 해시 함수에 의해 반환된 주소의 위치에 항목을 저장한 자료구조

* 해시 검색 과정

  <img src="https://user-images.githubusercontent.com/46865281/74242932-23055400-4d22-11ea-865c-2077332dba07.png" alt="image" style="zoom:33%;" />

  

* **충돌**: 서로 다른 탐색키를 해시 함수에 적용했는데, 반환된 해시 주소가 동일한 경우
  
  * 해시 테이블에 저장되는 자료의 수가 증가함에 따라 충돌은 불가피 함
  * 충돌 해결 방법
    1. 체이닝: 링크드리스트 등을 활용해 하나의 버킷에 여러 키 값을 저장하도록 함
    2. 개방 주소법: 빈 공간이 있을 때까지 그 다음 공간을 탐색한 후 항목을 저장



## 문자열

### JAVA의 경우

[참고](https://aljjabaegi.tistory.com/465)

```java
public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence {
    /** The value is used for character storage. */
    private final char value[];

    /** Cache the hash code for the string */
    private int hash; // Default to 0
    
    ...
    }
}
```

* 유니코드로 저장됨

* java의 object는 해시 값을 가짐. object의 hashCode() 메소드는 객체 고유의 해시 코드를 만들어 리턴 시킴. 두 객체가 동일한 지 체크할 때(equals()) 이 해시코드 값이 쓰임.

* `String str = "test";`

  "test"는 힙 메모리에 저장되고 그 주소를 저장한 str은 스택에 저장됨

* 내부 value가 final로 선언 되어 있어서 스트링 객체는 Immutable 함

  * 만약 `str += "code"` 처럼 값을 변경할 경우, 기존 변수 값을 변경하는 것이 아닌 새로운 string 객체가 생성되는 것이다. 참조를 잃어버린 기존 객체 str은 GC에 의해 처리됨

    * 문자열의 Immutable 특성은 성능은 좋지 않지만 thread-safe하다는 장점이 존재함 (즉, 여러 스레드에서 특정 string 객체를 참조하더라도 안전함, 새로운 문자열을 할당하더라도, 힙 영역의 값은 변하지 않음)

      

### C/C++ 의 경우

* 아스키 코드로 저장됨

* 문자열은 문자(char)의 배열 형태로 구현됨

* 마지막에 끝을 표시하는 '\0' 이 들어감

  ```c++
  void MyStrcpy(char *des, char *src)
  {
    while(*src != '\0')	// 문자열의 끝
    {
      *des = *src;
      src++;
      des++;
    }
    *des = '\0';
  }
  ```

  

## 패턴 매칭

1. brute force

   * O(MN)

   ```
   p[] : 페턴,	t[]: 전체 텍스트
   M: 페턴의 길이, N: 전체 텍스트의 길이
   
   BruteForce(p[], t[])
   	i <- 0, j <- 0
   	while j < M and i <N
   		IF t[i] != p[j]
   			i <- i-j
   			j <- -1
   		j <- i+1
   		j <- j+1
   	IF j == M:	return i-M
   	ELSE:	return i
   ```



2. 카프 - 라빈 알고리즘
   * 해시를 활용, 해턴의 해시 값과 본문 안의 해시 값만을 비교
   * 최악의 경우, O(MN)이지만 ,평균적으로 빠름
   * 한 글자씩 이동하면서, 이전의 해시 값에서 한 글자를 버리고, 다음 한 글자를 추가하는 식으로 해시 값을 업데이트 함



3. KMP 알고리즘

   * 불일치가 발생 했을 때,  그 전 부분들을 다시 비교하지 않고 불일치가 일어난 부분부터 매칭 수행

   * 매칭이 실패했을 때 돌아가기 위해서 next 배열을 만들어 둬야 함

   * 시간 복잡도: O(M+N)

     ```c++
     void kmp(char *pat)
     {
       int n = strlen(pat);
       int i = -1, j =0;
       next[j] = i;
       while(j<n)
       {
         if (i == -1||(i>=0&&pat[i]==pat[j]))
         {
           i++;
           j++;
           next[j] = i;	// 일치했을 경우 
         }
         else i = next[i];
       }
     }
     ```



## 트라이

* 트라이: 문자열의 집합을 표현하는 트리

  {"aeef", "ad", "bbfe", "bbfg", "c"}

<img src="https://user-images.githubusercontent.com/46865281/74304066-3d314780-4d9f-11ea-8593-981f18623547.png" alt="image" style="zoom:30%;" />



* 부분 문자열 검사, 최장 공통 접두어 찾기, 사전적 순서로 정렬된 k번째 접미사 찾기 등에 활용됨

https://meylady.tistory.com/23