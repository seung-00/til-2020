# 컴퓨터구조

## Performance

  ### Performance Metrics

* **response time(Latency, 반응시간)**: time elapsed between start end of a program
* **throughtput(연산 능력)**: amount of work done in a fixed time
* 지금은 throughput이 중요해서 latency를 손해보더라도 throughput을 많이 높이고자 함

* **Performance_x** = 1/Execution time_x

* Clock cycle: 신호가 목적지 도달
  * Clock cycle time = 1/Clock speed
* **CPU execution time = CPU clock cycles(required for executing a program) * Clock cycle time**
  * 만약 프로세서가 3GHz frequency를 가지면 clock은 1초에 30억번 찍음 
  * 만약 1.5 GHz 프로세서 위에서 프로그램이 20억 clock cycle 동안 돌아간다면 1.333초 걸림 
* **CPU clock cycles = instructions in the program *avg clock cycles per instruction(CPI)**
* **CPU execution time = clock cycle time * instructions * avg CPI**
* Q. If a 2 GHz processor graduates an instruction every third cycle, how many instructions are there in a program that runs for 10 seconds?
  * 명령어 하나에 3클락, 즉 CPI =3임. 2 GHz CPU에 프로그램 짜서 돌려보니까 10초 걸렸대. 그럼 저 공식에 집어 넣으면 10 = 0.5 * X * 3 이니까 instruction은 20/3

### Factors Influencing Performance

Enecution time = clock cycle time * number of instrs * avg CPI

* Clock cycle time
  * manufacturing process(how fast is each transistor )
    * 반도체  나노 공정...
* Number of instrs
  * the quality of the compiler, the instruction set architecture
* CPI
  * CPU 설계 이슈

### Benchmark Suites

* Each CPU vender announces SPEC rating for their system
  * a meausre of execution time for a fixed collection of programs
  * is a function of specific CPU, memory system, IO system, os, compiler
  * enables easy comparison of different systems
* SPEC CPU
  * System Performance Evaluation Corporation
    * 많이 쓰이고 보편화 된 프로그램 collection(gcc, ftp ...)을 만드는 산업 컨소시엄, 레이팅용
      * 프로세서 마다 특정 프로그램에 특화되어있을 수 있음(예컨대 플로팅 연산에 특화, AI 특화)
      * 따라서 SPEC은 어디까지나 일반적인 성능 평가일 뿐 특정한 프로그램의 퍼포먼스의 예측하기에 적합하지 않을 수 있음

  ### Common Principles

* Energy
  * systems leak energy even when idle
    * 놀아도 어떤 양은 소모된다
  * performance improvements typically also result in energy improvements
    * 퍼포먼스를 향상시키면 에너지도 절감된다. idle에도 에너지는 소모되니까 성능을 내는게 좋다는 의미
* **90-10 rule**
  * 10% of the program accounts for 90% if execution time 
* **priciple of locality**
  * the same data/code will be used again (temporal locality), nearby data/code will be touched next (spatial locality)
    * 특정 변수를 건드렸다는 얘기는, 한동안 그 변수를 사용할 일이 높다는 소리