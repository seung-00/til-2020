# JDBC 실습(1)

* [부스트코스] 웹 백엔드 [1. SQL & JDBC 프로그래밍](https://www.edwith.org/boostcourse-web-be/lecture/58939/)를 듣고 정리함.
* 부스트코스는 이클립스 환경에서 진행함. 본 글은 인텔리제이에서 예제 내용을 진행함.
  * 또한 부코는 mysql 5.7x 버전이라 8.x 버전에서 문법이 안 맞는 부분이 있음
* 실습 환경
  * *OS X, mysql  Ver 8.0.21*
  *  *OpenJDK 1.8, IntelliJ IDEA 2020.1.4 (Ultimate Edition), Maven*



## 개발환경 구축

### jdk 1.8 설치

* java는 13까지 버전이 나왔지만 아직까지 java 8(jdk1.8)이 가장 많이 쓰이고 있다.
  * 부스트코스 강좌도 java 8 기준이니 따르도록 하자.

* *JDK* 라이센스 문제로 *OpenJDK* 를 설치한다.
  * *JDK* 라이센스 문제는 [요기1](https://zepinos.tistory.com/12)와 [요기2]([요기](https://zepinos.tistory.com/12)), *JDK*, *OpenJDK* 비교는 [요기3]([https://www.lpcinc.co.kr/blog/java-%EC%9C%A0%EB%A3%8C-%EB%85%BC%EC%9F%81-oracle-jdk%EC%99%80-openjdk%EC%9D%98-%EC%B0%A8%EC%9D%B4-%EC%A0%95%EB%A6%AC](https://www.lpcinc.co.kr/blog/java-유료-논쟁-oracle-jdk와-openjdk의-차이-정리))와 [요기4](https://engineering.linecorp.com/ko/blog/line-open-jdk/)에 잘 정리되어 있다.

* *OpenJDK* 8 설치

  * 최신 버전이 아닌 경우 tap으로  버전을 관리한다.
  * [AdoptOpenJDK 참고](https://github.com/AdoptOpenJDK/homebrew-openjdk), [brew tap 명령어 참고](https://stackoverflow.com/questions/34408147/what-does-brew-tap-mean)

  ```shell
  brew tap AdoptOpenJDK/openjdk
  brew cask install adoptopenjdk8
  ```

### jEnv로 자바 버전 관리

[링크1](https://madplay.github.io/post/manage-java-version-using-jenv)과 [링크2](https://wickso.me/java/jenv/)를 참고했다. 

* 자바의 버전을 확인해보면 java13 만 나온다.

  ```shell
  java --version
  
  # java 13.0.2 2020-01-14
  # Java(TM) SE Runtime Environment (build 13.0.2+8)
  # Java HotSpot(TM) 64-Bit Server VM (build 13.0.2+8, mixed mode, sharing)
  ```

* 다음 명령어로 설치된 모든 자바의 버전, 경로를 확인할 수 있다.

  ```shell
  /usr/libexec/java_home -V
  
  # Matching Java Virtual Machines (2):
  #   13.0.2, x86_64:	"Java SE 13.0.2"	/Library/Java/JavaVirtualMachines/jdk-13.0.2.jdk/Contents/Home
  #   1.8.0_262, x86_64:	"AdoptOpenJDK 8"	/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
  ```

* 다양한 *java* 버전을 한 pc로 관리하는 건 복잡한 일이다. *jEnv*는 OS X에서 *JDK* 버전 관리를 편하게 해주는 도구다. *brew*로 쉽게 설치 가능하다.

  `brew install jenv`

  * 설치 이후 명령어로 확인해보면 아직 *jdk*가 관리 중인 상태가 아님을 알 수 있다.

    ```shell
    jenv versions
    system (set by /Users/.../.jenv/version)
    ```

  * 환경설정 파일을 수정해서 *jEnv*를 초기화시켜주자. 난 *zsh* 사용 중이라 `~/.zshrc` 을 수정해줬다.

    ```shell
    # bash 에선 vim ~/.bash_profile
    vim ~/.zshrc
    
    # 아래 두 줄 추가
    export PATH="$HOME/.jenv/bin:$PATH"
    if which jenv > /dev/null; then eval "$(jenv init -)"; fi
    
    # 적용
    source ~/.zshrc
    ```

* 이제 설치된 자바를 jEnv에 추가해준다. 경로는 위에서 확인했다. `jenv versions` 로 확인해보면 자바 버전들이 관리 중인 상태임을 알 수 있다.

  ```shell
  jenv add /Library/Java/JavaVirtualMachines/jdk-13.0.2.jdk/Contents/Home
  
  # oracle64-13.0.2 added
  # 13.0.2 added
  # 13.0 added
  # 13 added
  
  jenv add /Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
  
  # openjdk64-1.8.0.262 added
  # 1.8.0.262 added
  # 1.8 added
  
  jenv versions
  
  # * system (set by /Users/seungyoungoh/.jenv/version)
  #   1.8
  #   1.8.0.262
  #   13
  #   13.0
  #   13.0.2
  #   openjdk64-1.8.0.262
  #   oracle64-13.0.2
  ```

* `jenv versions` 출력 결과에서 * 표시된 부분이 전역적으로 설정된 자바 버전을 의미한다. `jenv global 1.8`  으로 *JDK* 1.8을 전역으로 설정하자.

  ```shell
  jenv global 1.8
  jenv versions
  
  #   system
  # * 1.8 (set by /Users/seungyoungoh/.jenv/version)
  #   1.8.0.262
  #   13
  #   13.0
  #   13.0.2
  #   openjdk64-1.8.0.262
  #   oracle64-13.0.2
  ```

  

### MySQL Connector 설치

* DB에 맞는 드라이버를 설치해줘야 한다. [mysql 웹사이트](https://dev.mysql.com/downloads/)에서 압축 파일을 받을 수 있다. 아래의 그림을 따라가면 됨

  <img src="https://user-images.githubusercontent.com/46865281/88481749-333f8180-cf98-11ea-857e-9c178a289fc0.png" width="1200" height="300">

### 인텔리제이 연동

* mysql connector 압축을 풀고 인텔리제이에서 설정

  * 인텔리제이 실행시키고 Project Structure 들어감(우측 상단 아이콘, cmd+;)
  * Libraries 카테고리에서 + 클릭,  압축을 푼 *mysql-connector ... -bin.jar* 파일을 추가시켜 준다.

* 새로운 프로젝트 생성(maven)

  * 위에서 설정한 *JDK 1.8*을 추가하자. */Library/Java*에 위치가 있을거다.

  <img src="https://user-images.githubusercontent.com/46865281/88552582-394c6580-d05f-11ea-8608-8d058a6d7bc7.png" width="630" height="400">

* pom.xml dependency 작성, 아래 부분을 추가한다.

  ```xml
  ...
  	<dependencies>
          <dependency>
              <groupId>mysql</groupId>
              <artifactId>mysql-connector-java</artifactId>
              <version>5.1.49</version>
          </dependency>
      </dependencies>
  ...
  ```

* 우측 상단에 새로고침 같이 생긴 Load Maven Changes 버튼을 누르면 연동 시작

* 연동이 완료되면 *Externernal Libraries*에 *Maven: mysql-connector-java:...*가 생긴다.
