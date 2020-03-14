DP 완전정복[^1]



### 예제 5-3. 문자열 인터리빙

> 두 문자열 A, B 내의 상대적 위치가 유지된 채 섞여 새 문자열 C가 만들어지면 C를 A, B의 인터리빙이라 함. A, B, C가 주어졌을 때 C가 A, B의 인터리빙인지 검사하는 함수를 구현하라.

* 풀이

  <img src="https://user-images.githubusercontent.com/46865281/76607184-e1e9a500-6556-11ea-8a26-d8773888e449.png" alt="image" style="zoom:33%;" />
  <img src="https://user-images.githubusercontent.com/46865281/76607227-f3cb4800-6556-11ea-943e-8f0113566d8b.png" alt="image" style="zoom:33%;" />
  <img src="https://user-images.githubusercontent.com/46865281/76607263-09407200-6557-11ea-9674-7e392a6de4dd.png" alt="image" style="zoom:33%;" />

  

  

* 생각

  * 순환식(재귀)을 정의할 때 각각의 분기가 나눠지도록 OR 연산이 필요하다는 점
  * 상향식으로 DP를 구현할 때 네 가지 경우를 나눠서 값을 정하는 부분
  * 위 두 부분이 어려웠던 문제

[^1]: https://github.com/crapas/dp

