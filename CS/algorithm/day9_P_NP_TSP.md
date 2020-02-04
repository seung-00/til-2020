

## P, NP, NP-난해, NP-완전

참고 1. https://wkdtjsgur100.github.io/P-NP/

참고 2. https://zeddios.tistory.com/176

### 	P - NP 문제

* **P 문제(Polynomial problem)**: 결정론적 튜링머신으로 다항시간 내에 풀 수 있는 문제
* **NP 문제(Non-deterministic Polynomial problem)**: 비 결정론적 튜링머신으로 다항시간 내에 풀 수 있는 문제

* **다항 시간(Polynomial Time)**: 다항시간 내에 풀 수 있다는 의미는 시간 복잡도가 O(n^2)와 같이 표현될 수 있다는 의미

* **튜링 머신**

  * 정해진 명령표(예를 들어 헤드를 한 칸 움직여라 or 테이프의 값을 바꿔라 같은)에 따라 원하는 일을 수행하는 가상의 기계를 튜링 머신이라 함
  * **결정론적 튜링머신**: P 문제는 튜링 머신이 다항 시간내에 풀어낼 수 있는, 쉬운 문제를 의미한다. 예시로는 정렬 문제가 있음
  * **비결정론적 튜링머신**: 특정 입력 값이 주어진 문제의 해답인지를 검사하는 장치를 말함. 예컨대 외판원 문제(TSP)에서 비결정론적 튜링머신은 입력된 경로가 정답인지 아닌지 알 수 있음

* NP 문제는 비결정론적 튜링머신이 주어진 입력이 정답인지 아닌지 계산하는데 다항시간이 걸리는 문제임(결정론적 튜링머신으로는 다항 시간 내에 불가)

* NP 문제는 결정 문제들 중 적어도 검산은 쉽게할 수 있는 것을 모아 놓은 집합으로도 정의 가능함.

* 예컨대, 정수 n개로 이루어진 집합이 주어졌다고 할 때, '이 집합의 부분집합들 중에서 원소의 합이 0이 되는 집합이 존재하는가?'라는 문제는 아직까지 다항식 시간 알고리즘이 알려져 있지 않음. 만약 {6, 1, -7} 같은 입력이 주어진다면, 우리는 이것이 정답인지는 알 수 있으므로 이 문제는 적어도 NP 문제라는 것을 알 수 있음

* 다른 예로, TSP(optimization) 역시 NP 문제임. 경로가 추가될 때마다 경우의 수가 팩토리얼로 증가하므로.

  ### NP-난해, NP-완전 문제

* **NP-난해(NP-hard) 문제**는 적어도 NP문제 보다는 어려우며, “모든” NP 문제를 다항 시간 내에 어떤 문제 A로 환원(reduction)할 수 있다면, 그 A 문제를 NP-난해(NP-hard) 문제라 함.

  * 예컨대

    ```
    문제 A: 주어진 n개의 숫자를 크기 순서로 정렬하는 문제
    문제 B: 주어진 n개 숫자의 중간값을 계산하는 문제
    ```

    가 주어졌을 때, A를 풀 수 있다면 정렬된 가운데 값으로 B를 쉽게 풀 수 있을 것이다. 이 경우 B를 A 문제로 환원시킬 수 있다고 한다. 이때 B를 A보다 **어렵다**라고 정의할 수 있다. 더 쉬운 예시로 곱셈과 덧셈의 예시를 생각해볼 수 있다. 

  * NP-난해 문제들 중에서도 해결 가능한 문제(NP에 포함되는)와 해결 불가능한 문제가 존재함.

    

* **NP-완전(NP-complete) 문제**는 NP 난해 문제에도 포함되며, NP 문제에도 포함되는 문제다. 즉 NP 문제들 중 풀 수 있는 가장 어려운 문제인 것. 

  * 헤밀턴 사이클은 대표적인 np-complete 문제다.

  

![diagram](https://wkdtjsgur100.github.io/images/posts/p_np.png)

* 위 다이어그램으로 개념을 정리한다. 이때 다이어그램 두 개인이유는 아직 P=NP 인지 P!=NP인지 증명이 안 됐기 때문

  

### TSP

* TSP(travelling salesman problem) 는 Optimization, Decision 두 버전이 존재한다.

* TSP Optimization은 주어진 무향 완전 그래프에서 모든 도시를 한 번씩 방문해서 시작점으로 돌아오는 "최단 경로"를 구하는 문제다.
  * TSP Optimization 같은 경우 NP-hard 문제다. 입력 값이 주어졌을 때 그것이 최단 경로인지를 확인하기 위해서 그래프의 모든 경로를 확인해야 하기 때문이다. 즉 NP에 속하지 않는다. 

* TSP Decision은 주어진 완전 그래프에서 모든 도시를 한 번씩 방문하고 돌아오는데 그 가중치의 합이 k인 것이 존재하는지 구하는 문제다.

  (k가 주어져을 때 k보다 비용이 적게드는 회로가 있는지로도 물어볼 수 있음)

  * 이는 해밀턴 경로 문제와 유사하며, 해밀턴 경로 문제는 NP-Complete이다.

  * 해밀턴 경로 문제를 이용해 TSP Decision 문제도 NP - 완전임을 증명할 수 있음(해밀턴 사이클 문제가 TSP에 포괄됨)

    [증명이 잘 설명된 링크](https://zeddios.tistory.com/176)

* TSP Optimization을 재귀로 푼 코드

  ```c++
  /*
  tsp_input.txt 은
  2
  4
  0123
  1045
  2406
  3560
  6
  0 10 11 13 24 12
  10 0 16 11 8 19
  11 16 0 12 12 14
  13 11 12 0 10 18
  24 8 12 10 0 13
  12 19 14 18 13 0
  */
   
  #include <iostream>
  #include <stdio.h>
  using namespace std;
  #define INF 987654321
  #define MAX_N 6
  int N, Graph[MAX_N][MAX_N];
  int solve(int pos, int visited);
  
  int main()
  {   
      int tcCnt;
      freopen("tsp_input.txt", "r", stdin);
      cin >> tcCnt;
      for (int t = 1; t <= tcCnt; ++t) {
          cin >> N;
          for (int i = 0; i <N; ++i)
              for (int j = 0; j<N; ++j)
                //i 도시에서 j 도시로 가는 비용 
                  cin >> Graph[i][j];
  
          int ans = INF;
          for (int i = 0; i < N; ++i) {
              int tmp = solve(i, 1 << i);
            #i 번째를 시작점으로, i 번째 비트를 1로 업데이트 시키고 시작
              if (ans > tmp) ans = tmp;
          }
          cout << "#" << t << ' ' << ans << endl;
      }
      return 0;
  }
  
  int solve(int pos, int visited) //최소 pos = 0 visited = 1
  {
      if (visited == (1 << N) - 1) //만약 n이 4일 때 모든 도시 방문시 방문? -> 10000-1 => 1111
          return 0;
  
      int ret = INF;
      for (int next = 0; next < N; ++next)
      { // next : 가고자할 목적지
          if (!(visited & (1 << next)) && Graph[pos][next])
            // visited와 next를 and 연산해서 교집합이 있는지 체크(교집합 있음 가본 적 있는 곳)
            // Graph[pos][next])는 연결이 되어있는 지 체크하는 것, 이런 완전 그래프에선 의미가 없다. 
          {
              int tmp = Graph[pos][next] + solve(next, visited | (1 << next));
        // visited에 next를 추가시킴
              if (tmp < ret)
                  ret = tmp;
          }
      }
      return ret;
  }
  
  
  ```

  