### 순열과 조합

* 순열은 순서가 존재하고 조합은 존재하지 않음

* 조합으로 풀 수 있는 문제를 순열로 풀 수도 있음. 그러나 낭비가 발생함. 구분할 줄 알아야 함.

  * 순열: 선택의 순서가 결과에 영향을 주는 경우

    * 예컨대, TSP는 각 경로마다 가중치가 다를 수 있기 때문에 1-2-3 과 2-1-3이 다를 수 있음

  * 조합: 선택의 순서가 결과에 영향을 주지 않는 경우

  * 예제:

    1. {1, 2, 3, 4} 중 2개를 골라 만들 수 있는 최대 수는 얼마인가 => 43 (순열)

    * 코드

      ```c++
      /*
      tsp_input.txt 은
      2
      4
      1 2 3 4
      5
      2 1 3 5 4
      */
      
      #include <iostream>
      #include <stdio.h>
      using namespace std;
      
      #define MAX_N 10
      
      int N, Nums[MAX_N];
        
      int solve(int cnt, int used, int val);
      
      int main()
      {
        int tcCnt;
        freopen("number_intput.txt", "r", stdin);
        
        cin >> tcCnt;
        for (int t = 1; t <= tcCnt; ++t)
        {
          cin >> N;
          for (int i = 0; i<N; ++i)
            cin >> Nums[i];
          
          cout << "#"<<t<<' '<< solve(0,0,0) << endl;
        }
          return 0;
      }
      int solve(int cnt, int used, int val)
      {
        if(cnt == 2) return val;
        
        int ret = 0;
        for(int i=0; i<N; ++i)	// N은 전역 변수
        {
          if (used&(1<<i)) continue;
          
          int tmp = solve(cnt+1, used|(1<<i), val*10+Nums[i]);
          if (tmp > ret) ret = tmp;
        }
        return ret;
      }
      ```

      

    1. {1, 2, 3, 4} 중 2개를 더해 만들 수 있는 최대 값은 얼마인가 => 7 (조합)

       ```c++
       /*
       tsp_input.txt 은
       2
       4
       1 2 3 4
       5
       2 1 3 5 4
       */
       
       #include <iostream>
       #include <stdio.h>
       using namespace std;
       
       #define MAX_N 10
       
       int N, Nums[MAX_N];
         
       int solve(int cnt, int used, int val);
       
       int main()
       {
         int tcCnt;
         freopen("number_intput.txt", "r", stdin);
         
         cin >> tcCnt;
         for (int t = 1; t <= tcCnt; ++t)
         {
           cin >> N;
           for (int i = 0; i<N; ++i)
             cin >> Nums[i];
           
           cout << "#"<<t<<' '<< solve(0,0,0) << endl;
         }
           return 0;
       }
       
       int solve(int pos, int cnt, int val)
       {
         if (cnt == 2) return val;
         if (pos == N) return -1;  // 끝까지 갔음에도 2개가 없는 경우, 제외 시킴
         
         int ret = 0, tmp;
         
         // 선택하는 경우
         tmp = solve(pos+1, cnt+1, val + Nums[pos]);
         if (tmp>ret) ret = tmp;
         
         // 선택하지 않는 경우
         tmp = solve(pos+1, cnt, val);
         if (tmp>ret) ret = tmp;
         
         return ret;
       }
       
       ```

       * bit 부분집합 적용

       ```c++
       /*
       tsp_input.txt 은
       2
       4
       1 2 3 4
       5
       2 1 3 5 4
       */
       
       #include <iostream>
       #include <stdio.h>
       using namespace std;
       
       #define MAX_N 10
       
       int N, Nums[MAX_N];
         
       int solve(int cnt, int used, int val);
       
       int main()
       {
         int tcCnt;
         freopen("number_intput.txt", "r", stdin);
         
         cin >> tcCnt;
         for (int t = 1; t <= tcCnt; ++t)
         {
           cin >> N;
           for (int i = 0; i<N; ++i)
             cin >> Nums[i];
           
           cout << "#"<<t<<' '<< solve(0,0,0) << endl;
         }
           return 0;
       }
       
       // value에 있는 bit 개수를 구하는 코드
       // 1의 자리를 기준으로 오른쪽으로 계속 이동시키면서 센다.
       int countBits(int value)
       {
         int count = 0;
         while (value>0)
         {
           if((value&1) == 1)	count++;
           value = value >> 1;
         }
       }
       
       int solve(int pos, int cnt, int val)
       {
         int ret = 0;
         //전체 부분집합
         for (int i = 0; i<(1<<N); ++i)
         {
           if (countBits(i)==2)
           {
             int sum = 0;
             for (int j = 0; j<N; ++j)
             {
               //집합에 해당되는 값을 찾기 위해
               if (i&(1<<j))	sum += Nums[j]
             }
           }
         }
       }
       ```



### 완전 탐색

**예제: Baby-gin Game**

- 설명

  - 0~9사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
  - 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.
  - 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.

- 입력 예

  1. 667767은 두 개의 triplet이므로 baby-gin (666,777)
  2. 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin(456,000)
  3. 101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 baby-gin이 아니다. (123을 run으로 사용하더라도 011이 run이나 triplet이 아님)

- 어떻게 Baby-gin 여부 판단?

  - 정렬
    - 예제 1,2에 적합하나 234345인 경우 233/445 같은 식의 판단 쉽지 않음(greedy) - **순서가 영향을 준다**
  - Brute-force 이용.
  - 완전 탐색은 조합적 문제에 대한 brute-force임. **완전 탐색을 통한 Baby-gin 접근**
  - 고려할 수 있는 모든 경우의 수 생성하기
    - 6개의 숫자로 만들 수 있는 모든 숫자 나열 (중복 포함)
    - ex) {2,3,5,7,7,7} -> 235777, 237577,...... 777532
  - 해답 테스트 하기
    - 앞의 3자리와 뒤의 3자리를 잘라, run과 triplet 여부를 테스트하고 최종적으로 baby-gin판단

- code

  ```c++
  #include <iostream>
  #include <stdio.h>
  using namespace std;
  
  int Nums[6];
  
  int solve(int arr[], int pos, int used);
  
  int main()
  {
      //babyGin_input.txt
      //4
      //1 2 4 7 8 3
      //6 6 7 7 6 7
      //0 5 4 0 6 0
      //1 0 1 1 2 3
      
      int tcCnt;
      freopen("babyGin_input.txt", "r", stdin);
      
      cin >> tcCnt;
      for(int t = 1; t <= tcCnt; ++t)
      {
          for (int i=0; i<6; ++i) cin>>Nums[i];
          
          int arr[6];
          cout<<"#"<<t<<' '<<solve(arr, 0, 0)<<endl;
      }
      return 0;
  }
  
  int solve(int arr[], int pos, int used)
  {
      if (pos ==6)
      {
          cout<<"check -> ";
          for (int k = 0; k<6; ++k)
          {
              cout<<arr[k];
          }
          cout<<endl;
          int tri =0, run=0;
          for (int i=0; i<2; ++i) //앞에 셋, 뒤에 셋
          {
              // 0과 1, 1과 2를 비교(run)
              if (arr[i*3+1] == arr[i*3] && arr[i*3+2] == arr[i*3+1]) ++run;
              // 마찬가지(triple)
              else if (arr[i*3+1] == arr[i*3] && arr[i*3+2] == arr[i*3+1])    ++tri;
          }
          if (run + tri == 2) return 1;
          
          return 0;
      }
      for (int i= 0; i <6; ++i)
      {
          // pos에 뭘 넣을지 arr 0~5까지 하나씩 해보는 것이다.
          
          if(used&(1<<i)) continue;
          // i 번쨰 값이 used에 있다.
          
          arr[pos] = Nums[i];
          // 0~5까지 채우고 pos 6일때 조건 걸림
          // babygin이 판단되면 1 리턴으로 반복이 끝남. 아니라면 계속 탐색
          // 이런 순열 문제의 경우 재귀 속에 반복문이 들어간다는 것이 특징임. if 써줘야 함
          if (solve(arr, pos+1, used | (1<<i)))   return 1;
      }
      return 0;
  }
  
  ```

  