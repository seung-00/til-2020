# JDBC 실습(2)

* [부스트코스] 웹 백엔드 [1. SQL & JDBC 프로그래밍](https://www.edwith.org/boostcourse-web-be/lecture/58939/)를 듣고 정리함.
* 부스트코스는 이클립스 환경에서 진행함. 인텔리제이에서 예제를 따라가기 어려워서 정리해둠.
  * 또한 부코는 mysql 5.7x 버전이라 8.x 버전에서 문법이 안 맞는 부분이 있음
* 실습 환경
  * *OS X, mysql  Ver 8.0.21*
  *  *OpenJDK 1.8, IntelliJ IDEA 2020.1.4 (Ultimate Edition), Maven*



## DB 실습

### 트러블 슈팅

* mysql 8.x의 경우 계정 생성과 권한 부여를 동시에 할 수 없다.
  
*  즉 `grant all privileges on db이름.* to 계정이름@'localhost' identified by ＇암호’;` 요런게 불가
  
* 생성한 유저에게 권한을 주려고 하니 `ERROR 1410 (42000): You are not allowed to create a user with GRANT`와 같은 오류 메세지를 받았을 수 있다. 
  * 나 같은 경우, mysql을 생성할 때 계정 호스트를 권한 부여할 때 그대로 입력하지 않아서 문제가 발생했다.
    
    * 즉, `CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'password'; ` 이렇게 *localhost* 로 생성하고 권한을 다음과 같이 wildcard로 주면 안 된다는 의미 `GRANT ALL ON db1.* TO 'jeffrey'@'%';` **(x)**
    
    * > The specified user just doesn't exist on your MySQL (so, MySQL is trying to create it with GRANT as it did before version 8, but fails with the limitations, introduced in this version).
      >
      > MySQL's pretty dumb at this point, so if you have 'root'@'localhost' and trying to grant privileges to 'root'@'%' it treats them as different users, rather than generalized notion for root user on any host, including localhost.
    
      [참고](https://stackoverflow.com/questions/50177216/how-to-grant-all-privileges-to-root-user-in-mysql-8-0)

### msyql

[참고](https://dev.mysql.com/doc/refman/8.0/en/)

* mysql 루트 계정으로 접속, db 확인, user 확인

  ```shell
  mysql -uroot -p
  
  show databases;
  select user, host from user;
  ```

* db 생성, 계정 생성, 권한 부여

  ```shell
  CREATE DATABASE connectdb;
  
  CREATE USER 'connectuser'@'localhost' IDENTIFIED BY '1234';
  GRANT ALL ON *.* TO 'connectuser'@'localhost';
  ```

* db 혹은 유저 삭제(참고)

  ```shell
  DROP DATABASE connectdb;
  DROP USER 'connectuser'@'localhost';
  ```

* 테이블 생성

  ```sql
  mysql -hlocalhost -uconnectuser -p
  mysql> use connectdb
  
  mysql> CREATE TABLE role(   
    role_id    INTEGER(11) NOT NULL PRIMARY KEY,  
    description	VARCHAR(10));
             
  mysql> DESC ROLE;
  +-------------+-------------+------+-----+---------+-------+
  | Field       | Type        | Null | Key | Default | Extra |
  +-------------+-------------+------+-----+---------+-------+
  | role_id     | int         | NO   | PRI | NULL    |       |
  | description | varchar(10) | YES  |     | NULL    |       |
  +-------------+-------------+------+-----+---------+-------+
  2 rows in set (0.03 sec)
  ```

* INSERT

  ```sql
  mysql> insert into ROLE (role_id, description) values ( 100, 'CEO');
  select role_id, description from role;
  
  +---------+-------------+
  | role_id | description |
  +---------+-------------+
  |     200 | CEO         |
  +---------+-------------+
  1 row in set (0.01 sec)
  ```

### java

* 패키지 생성

  * 부스트코스 내용대로 *src>main>java* 디렉토리에 *kr.or.connect.jdbcexam*패키지를 생성하고 *kr.or.connect.jdbcexam.dao, kr.or.connect.jdbcexam.dto*를 생성한다.

  <img src="https://user-images.githubusercontent.com/46865281/88671462-49c51480-d121-11ea-90b3-2d160917ea7c.png" width="630" height="400">

* 자바 클래스 생성

  * *kr.or.connect.jdbcexam.dao*에 *RoleDao*, *kr.or.connect.jdbcexam.dto*에 *Role* 자바 클래스를 만든다.

* 자바 코드 작성

  * 강의 참고

    * Role.java

    * RoleDao.java
  
    * JDBCExam1
  
      
      
      
  
  