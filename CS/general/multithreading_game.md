[김포프의 유튜브 동영상](https://www.youtube.com/watch?v=M1e9nmmD3II)을 정리한 글입니다.



# 바람직한 멀티스레딩 구조(게임 예시)

쓰레드의 발달과 게임 업계

* Early 90s
  * single CPU
  * 퍼포먼스가 아닌, non-bloking operation를 위해(blocking: 하나의 project만을 대기) 일종의 ux를 위한 것이었던 것
  * why overhead?
    * only one worker, context switch 비용

* What happened in mid-2000?
  * We hit the limit
    * CPU stopped getting faster(물리적인 어려움, 발열...)
  * 2-core CPU 등장
  * Main Thread, Render Thread 정도로 나눔
* End of 2006
  * Inter i7 CPU
    * 4 core

* Revisiting game loop

  * 기존에는, Main Thread, Render Thread, 오디오... 같은 식으로 프로세스 기반으로 나눴었음

  * object 중심으로 나누자!

  * similar operations on each

    * physics update, animation update(matrix math) ...
    * 계산이 비슷하네? 계산이 아닌 객체를 묶어서 이를 중심으로 thread를 나눠보자

  * ​    Task System(aka, job system)

    <img src="https://user-images.githubusercontent.com/46865281/79639756-a03cc180-81c8-11ea-935e-3478ef0591fa.png" alt="image" style="zoom:50%;" />

    

  * 서로 독립성이 유지됨, Barrier Lock을 통해 사람들이 추적이 가능해짐.

* Why is it better

  * No race cpndition
  * can adapt to any number of cores
  * minimum overhead
    * an aequal number of objects in each list, context switching 적음
  * More advanced topics
    * job stealing
    * dependancy graph

