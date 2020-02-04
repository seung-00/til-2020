### 탐욕 알고리즘(Greedy Algorithm)

* 각 단계에서 국소 최적해를 구해서 최종적으로 전역 최적해를 구하고자 하는 것

* 그리디 알고리즘이 잘 작동되기 위해 두 조건이 만족되어야 함.

  1. 탐욕스런 선택 조건(greedy choice property)

  2. 최적 부분 구조 조건(optimal substructure)

  * 한 번의 선택이 다음 선택과 무관해야 하며, 문제의 최적해(전역 최적해)가 부분 문제에 대해서도 최적해(국소 최적해)라는 것

* 위와 같은 조건을 만족하지 못해도 탐욕 알고리즘은 **근사 알고리즘**으로서 NP 문제에 쓰일 수 있다.

* 예제: **집합 커버링 문제**

  > 미국의 몇 개 주에 라디오를 들려줘야 한다. 주는 "mt", "wa", "or", "id", "nv", "ut", "ca", "az" 이 있으며 kone ~ kfive 방송국 중 최소한의 방송국을 선택해 모든 주의 사람들이 방송을 들을 수 있도록 해야한다. 이를 정확하게 풀려면 모든 방송국의 부분 집합을 나열한 뒤, 모든 주를 커버할 수 있으면서 원소가 적은 부분 집합을 골라야함.  이 경우 부분집합을 고를 때 **O(2^n)**(n은 방송국의 수) 시간이 걸리므로 좋은 방법이 아님 그리디 알고리즘으로 근사한 해답을 구하는 것이 좋음

  ```python
  states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
  stations["kone"] = set(["id", "nv", "ut"])
  stations["ktwo"] = set(["wa", "id", "mt"])
  stations["kthree"] = set(["or", "nv", "ca"])
  stations["kfour"] = set(["nv", "ut"])
  stations["kfive"] = set(["ca", "az"])
  final_stations = set()
  
  while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
      ## 아직 방송이 필요한데 아직 커버 안 된 주들(states_needed) 중 현재 고려하는 방송국이 커버하는 주(sates_for_station)의 집합
      covered = states_needed & states_for_station	
      if len(covered) > len(states_covered):	
        best_station = station
        states_covered = covered
  	
    states_needed -= states_covered	## 커버된 주 제외
    final_stations.add(best_station)
  ```



* 예제: **배낭 짐싸기[Knapsack]**

  배낭에 담을 수 있는 총무게 30kg으로 정해져 있고,
  각 물건의 무게와 가치가 있음, 이때 최대 가치값은?

  |       | 무게 | 값     |
  | ----- | ---- | ------ |
  | 물건1 | 25kg | 10만원 |
  | 물건2 | 10kg | 9만원  |
  | 물건3 | 10kg | 5만원  |

  * **[접근1] 완전 탐색**

    * 모든 부분집합을 구하고 비교

    * 시간 복잡도 지수적 증가(NP)

    * 최적해: (물건2, 물건3), 20kg, 14만원

      

  * **[접근2] Knapsack에 대한 탐욕적 방법1**

    * 값이 비싼 물건부터 채운다

    * 탐욕적 방법의 결과: 물건1,25kg,10만원

      

  * **[접근4]Knapsack에 대한 탐욕적 방법2**

    |       | 무게 | 값      | 값/kg     |
    | ----- | ---- | ------- | --------- |
    | 물건1 | 5kg  | 50만원  | 10만원/kg |
    | 물건2 | 10kg | 60만원  | 6만원/kg  |
    | 물건3 | 20kg | 140만원 | 7만원/kg  |

    * 무게 당 값이 높은 순서로 물건을 채운다.

    * 역시 최적해 못구함

      

  * **Fractional Knapsack**

    - **물건 잘라 넣을 수 있다**는 조건 추가
    - 탐욕적 방법으로 최적해 가능: (물건1 + 물건3+ 물건2의 절반, 30kg, 220kg)

  

