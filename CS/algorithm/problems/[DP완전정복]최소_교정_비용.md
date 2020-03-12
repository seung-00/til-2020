DP 완전정복[^1]



### 예제 5-1. 최소 교정 비용

> 두 단어 str1, str2가 있다. str1에서 str2가 되는데 필요한 최소 교정 비용을 구하라. 단, str1에서 수행할 수 있는 연산은 삽입, 삭제, 치환이다. 두 단어 간 교정 비용이란, 한 단어에서 다른 단어로 바꾸는데 필요한 연산 횟수를 의미한다.

* 입력: "sunday", "saturday"	출력: 3	(삽입 2, 치환 1)

* 풀이

  <img src="https://user-images.githubusercontent.com/46865281/76537135-ad2b0e80-64c0-11ea-9fc0-dc12e09b6a22.png" alt="image" style="zoom:67%;" />

  <img src="https://user-images.githubusercontent.com/46865281/76537309-ef545000-64c0-11ea-921c-c1167186c9d5.png" alt="image" style="zoom:67%;" />

  

* 생각: 우선 나는 이 문제를 못 풀고 해설을 봤다. 순환식을 생각하는 것이 어려웠다. 즉, 삽입. 삭제, 치환 과정에서 하위 구조가 반복되는 것을 생각하기 어려웠다. 

[^1]: https://github.com/crapas/dp

