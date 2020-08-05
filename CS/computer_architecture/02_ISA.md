# 컴퓨터구조

## Instruction Set Architecture(ISA)

### Machine Language

* Programming language
  * High-level programming languages
    * Procedual(절차적) languages: C, PASCAL, FORTRAN
    * Object-Oriented languages: C++, Java, ...
    * Functional languages: Lisp, Scheme
  * Assembly programming languages: symbolic machine languages
  * Machine languages: binary, IA32, IA64, ARM
* Translator
  * Compiler: translate a high-level language -> machine language
  * Assembler: assembly language -> machine language
  * Interpreter: translate and excute programs directly
    * JVM: translate/execute Java bytecode to native machine instructions



### Compiler

* Compiler
  * A program that translates a source program -> a target program
  * Source program
    * Usually written in high-level programming languages such as C, C++, Java, Python, ...
  * Target program
    * Usually written in machine languages such as x86, Alpha, MIPS, ARM instructions, ...
* What qualities do you want in a compiler?
  *  Generate correct code
    * 정확한 번역
  * Target codes run fast
    * 코드 최적화
  * Compiler runs fast
    * 컴파일 눌렀을 때 바로 바로
  * Support for separate compilation, good diagnostics for errors



### Compile Process

<img src="https://user-images.githubusercontent.com/46865281/89161955-4c56bc80-d5ae-11ea-9dcc-3803c4c76e4e.png" width="700" height="700">

* Preprocessor
  * source program에서 `#include` 와 같이 호출한 파일들을 체크한다. 내 source program 쭉 읽어서 갖다 쓰는 부분만 가져다가 `#include`에 copy & paste 한다. (전체 카피하면 너무 많으니까)
* Compiler
  * Preprocessing으로 확장된 소스 프로그램을 어셈블리 프로그램으로 바꿔준다.
    * 어셈블리어 역시 사람이 이해할 수 있게 표기된 언어다. 기계어는 0과 1로 이루어진 명령어의 조합이고 다만 어셈블리어는 이에 근접한 언어다.
    * 여기서 소스 최적화가 이루어짐

* Assembler
  * 기계어(object file)로 만듬. 각 파일마다 여러 object file이 나옴
* Linker
  * 여러 object file(module)을 엮어서 하나의 실행 프로그램을 만듬



### Register

* CPU가 요청을 처리하는 데이터의 임시저장 공간
  * 1 bit의 정보를 저장할 수 있는  플립플의 집합
* 레지스터 공간은 작고 비싸지만 CPU에 직접 연결되어 있어서 **연산 속도가 RAM, HDD, SDD보다 훨씬  빠름**
* CPU는 자체적으로 데이터를 저장할 수 없으므로 레지스터가 필요함. 메모리(RAM)으로 데이터를 직접 전송할 수 도 없음.
  * 레지스터를 이용해 연산처리 및 번지 지정을 도와줌
  * 현재 계산을 수행 중인 값을 저장하는데 사용됨



### Machine State

* ISA 는 machine states 와 instructions을 정의한다.
* Resisters
  * 레지스터
    * 산술 연산, 논리 연산 등을 가능하게 하는 기본 정보가 저장되어 있음
  * 메모리 계층 구조
    * Registers <-> Caches <-> Memory <-> Hard Disk
      * 레지스터로 들어와야 CPU가 데이터를 조작할 수 있음
      * Registers are visble to programmers and maintained by programmers
      * Caches are invisible to programmers and maintaned by HW



### Machine Instruction

* Opcode: 동작을 명시해준다.

  * ex) ADD, MULT, LOAD, STORE, JUMP

* Operands: 데이터 저장 장소를 명시해준다.

  * Source operands

  * Destination operands

  * 예시

    * Memory operand, ex) 8(R2), x1004F
    * Register operand, ex) R1

    

