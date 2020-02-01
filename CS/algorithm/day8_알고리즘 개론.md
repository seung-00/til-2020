# 200130 알고리즘 개론

### 알고리즘 효율

1. 공간적 효율성 => 메모리
2. 시간적 효율성 => 시간



### **Big O 표기법**

* "최대 이 시간 안에는 끝난다!"



### 비트 연산

* &

  * 비트 단위로 AND 연산

* |

  * 비트 단위로 OR 연산

* ^

  * 비트 단위로 XOR 연산(같으면 0, 다르면 1)

* <<, >>

  * 피연산자의 비트 열을 이동시킴
  * 1<<n
    * 2^n 의 값을 가짐
    * 원소의 개수가 n인 모든 부분집합의 수를 의미함
  * I&(1<<j)
    * i의 j번째 비트가 1인가?

* 10진수를 2진수로 만드는 예제 코드

  ```c
  #include <stdio.h>
  
  void printBits(char n)
  {
    char i;
    for(i = 7; i >= 0; --i)
    {
      if (n & (1<<i)) print("1");
      else print("0")
    }
  }
  
  int main(int arge, char ** argv)
   //arguments count, arguments vector
  {
    char i;
    for (i = -5; i < 6; ++i)
    {
      printf("%3d = ", i);
      printBits(i);
      print("\n");
    }
    return 0;
  }
  ```



* bit를 이용해 부분집합을 표현할 수 있다.

  * 부분집합의 수는 해당 수가 포함된다 or 포함되지 않는다 

    => 해당 자리가 0 or 1 로 표현 가능

    

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200131113152939.png" alt="image-20200131113152939" style="zoom:33%;" />

  

* Bit를 이용한 부분집합 생성 코드

  ```c
  #include <stdio.h>
  
  void printSubsets(char arr[], int n)
  {
    for(int i = 0; i< (1<<n); ++i)
    {
      printf("{");
      for(int j=0; j<n; ++j)
      {
        if(i&(1<<j))
          printf("%c ", arr[j])
      }
      printf("}\n")
    }
  }
  
  int main(int argc, char** argv)
  {
    char data[] = {'A', 'B', 'C', 'D'};
    printSubsets(data, 4);
    return 0;
  }
  ```



* 실수의 표현

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200131120510561.png" alt="image-20200131120510561" style="zoom:33%;" />
  * 0.5= 2^(-1) = 0.1000으로 표현

  * 비트의 수를 늘릴수록 정밀도는 높아지지만 모든 10진수를 표현할 수는 없다. 결국 컴퓨터는 실수를 근사적을 표현함.

  * 따라서 실수 표현을 최대한 지양하는 것이 좋다

    예컨대, d = sqrt(dx^2 + dy^2) 보다, d^2 = dx^2 + dy^2 식으로 표현