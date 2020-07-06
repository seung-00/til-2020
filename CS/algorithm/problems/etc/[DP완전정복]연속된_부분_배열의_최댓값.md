DP 완전정복[^1]



### ch4 예제: 연속된 부분 배열의 최댓값 구하기

> 정수로 이루어진 배열에서 연속된 부분 배열의 합의 최댓값을 리턴하는 함수를 구현하라

* 입력: [-2, -3, 4, -1, -2, 1, 5, -3]	출력: 7	연속된 부분 배열: [4, -1, -2, 1, 5]

* 풀이

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200313002053481.png" alt="image-20200313002053481" style="zoom:66%;" />

  

* 생각: 위 문제 역시 점화식을 만들 수 있다. `M(n) = max(M(n-1) + arr[n], arr[n])` 이런 식으로 쓰면 될 것이다. 그러나 트리 구조로 가지가 나눠지지 않고 n-1에 대해서만 재귀 호출 한다. 따라서 DP 최적화 대상인 반복 계산이 존재하지 않는다.

[^1]: https://github.com/crapas/dp

