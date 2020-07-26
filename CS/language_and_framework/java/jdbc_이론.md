# JDBC

* [부스트코스 웹 백엔드 강좌](https://www.edwith.org/boostcourse-web-be/lecture/58939/)를 듣고 정리

### JDBC(Java Database Connectivity) 개요

> JDBC(Java Database Connectivity)는 자바에서 데이터베이스에 접속할 수 있도록 하는 자바 API이다. JDBC는 데이터베이스에서 자료를 쿼리하거나 업데이트하는 방법을 제공한다.
>
> 출처: 위키피디아

- JAVA 프로그램에서 SQL문을 실행하기 위한 자바 API
- JAVA는 표준 인터페이스인 JDBC API 제공
- 접속하려는  DBMS 서버에 따라 다른 JDBC 드라이버가 필요함

### JDBC 단계별 절차

1. IMPORT

   *  import java.sql.*;`

2. 드라이버 로드 (db별로 다름, 여기서는 전부 mysql 기준)

   * `Class.forName("com.mysql.jdbc.Driver")`

3. 접속, Connection 객체 생성

   ```java
   String dburl = "jdbc:mysql://localhost/dbName";\
   Connection conn = DriverManager.getConnection(dburl, ID, PW);
   ```

4. Statement 객체 생성

   * `Statement stmt = conn.createStatement();`

5. 질의 실행

   * `ResultSet rs = stmt.executeQuery("select no from user");`

6. ResultSet으로 결과 받기

   * DB로부터 결과 셋 주소를 참조해서 next 메소드로 마지막까지 하나씩 꺼내옴!

   ```java
   ResultSet rs = stmt.executeQuery("select no from user");
   while(rs.next())
   	System.out.println(rs.getlnt("no"));
   ```

7. 모든 객체를 닫음

   ```java
   rs.close();
   stmt.close();
   con.close();
   ```

### JDBC 클래스의 생성관계

* **DriverManager**
  * **Connection**
    * **Statement**
      * **ResultSet**

### 소스코드 예제

```java
public List<GuestBookVO> getGuestBookList(){
		List<GuestBookVO> list = new ArrayList<>();
		GuestBookVO vo = null;
		Connection conn = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		try{
			conn = DBUtil.getConnection();	// 접속, Connection 객체 생성(따로 모듈 만듬)
			String sql = "select * from guestbook";
			ps = conn.prepareStatement(sql);	// Statement 객체 생성
			rs = ps.executeQuery();	// 질의 실행
			while(rs.next()){	// ResultSet으로 결과 받기
				vo = new GuestBookVO();
				vo.setNo(rs.getInt(1));
				vo.setId(rs.getString(2));
				vo.setTitle(rs.getString(3));
				vo.setConetnt(rs.getString(4));
				vo.setRegDate(rs.getString(5));
				list.add(vo);
			}
		}catch(Exception e){
			e.printStackTrace();
		}finally {
			DBUtil.close(conn, ps, rs);	// 모든 객체 닫음
		}		
		return list;		
	}
```

