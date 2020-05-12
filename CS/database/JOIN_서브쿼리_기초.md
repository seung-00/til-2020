## JOIN과 서브쿼리

### 개요

* JOIN, 서브쿼리는 SELECT에서 쓰이는 기능
* SELECT 쓸 때 대상 테이블들을 묶어줌. 정규화의 반대 과정이라 할 수 있음

* 두 테이블을 가정하자
  * 서브쿼리는 하위 셀렉트문의 결과 테이블을 상위 셀렉트문으로 전달해서 두 테이블을 연결함
  * JOIN은 A와 달리 하나의 셀렉트 문만 쓰면서 FROM에 두 테이블을 두고 WHERE에 조건을 줘서 연결함



### 개념

* 서브쿼리

  ```sql
  SELECT EmpName
  FROM EMPLOYEE
  WHERE DeptID IN
  (SELECT DeptID
  FROM DEPARTMENT
  WHERE DeptName LIKE `Account%`);
  ```

  * WHERE 뒤의 하위 SELECT의 결과로 새로운 테이블이 생김
  * IN을 통해 해당 테이블의 결과를 상위 SELECT로 매칭시키는 구조
  * 여러 단계로 확장 가능

* JOIN

  ```sql
  SELECT EmpName
  FROM EMPLOYEE, DEPARTMENT
  WHERE EMPLOYEE.DeptID = DEPARTMENT.DeptID
  AND DEPARTMENT.DeptNAME LIKE ‘A%’;
  ```

  * FROM 뒤의 두 테이블을 DeptID를 기준으로 매핑시킴
  * 정규화 과정에서 쪼개졌던 것을 다시 연결시키는 과정이라 볼 수 있음
    * 위 예시에서 DeptID가 EMPLOYEE에서 FK, DEPARTMENT에서 PK

  ```sql
  SELECT EmpName
  FROM EMPLOYEE AS E, DEPARTMENT AS D
  WHERE E.DeptID = D.DeptID
  AND D.DeptNAME LIKE ‘Account%’;
  ```

  * AS를 활용해서 약자를 만들어 테이블 명시를 할 수 있음
    * 테이블이 많아질 경우 유용함

* JOIN ON syntax

  ```sql
  SELECT EmpName,FROM EMPLOYEE AS E JOIN DEPARTMENT AS D
  ON E.DeptID = D.DeptID
  WHERE D.DeptName LIKE ‘Account%’;
  ```

  * 기능은 위 JOIN과 동일함
  * 뒤에 나오는 LEFT, RIGHT로 확장 가능
  * MS Access 에는 INNER JOIN 써야함

* LEFT(RIGHT) JOIN

  ```sql
  SELECT EmpName, DeptName
  FROM EMPLOYEE AS E LEFT JOIN DEPARTMENT AS D
  ON E.DeptID = D.DeptID
  WHERE EmpID>2;
  ```

  * 왼쪽(혹은 오른쪽) 테이블을 기준으로 연결함
  * JOIN은 두 테이블 교집합에 해당하는 행만 보여줌. 그래서 필요한 행이 사라질 수도 있음.
  * LEFT(RIGHT) JOIN을 쓰면 그 교집합에서 기준(왼쪽 or 오른쪽)이 되는 테이블의 행이 포함됨
  * 예를 들어, EMPLOYEE와 DEPARTMENT를 LEFT JOIN으로 연결하면, EMPLOYEE(LEFT)의 사원이 남았을 때(즉 부서가 없는 사원이 존재해도) 널 값을 가진채로 테이블에 포함됨



### 예시

* 닉네임을 직접 알 순 없지만 라스트 네임을 아는 경우...

  ```sql
  /*
  SELECT LastName, FirstName
  FROM CUSTOMER
  WHERE NickName IN("Billy", "Chris")
  아래와 같은 의미
  */
  
  SELECT LastName, FirstName
  FROM CUSTOMER
  WHERE NickName IN(
  SELECT NickName
  FROM SALESPERSON
  WHERE LastName = "Jones";
  )
  ```

  * 결과

  | LastName  | FirstName |
  | --------- | --------- |
  | Griffey   | Ben       |
  | Christman | Jessica   |

  

* 위와 동일한 결과

  ```sql
  SELECT C.LastName, C.FirstName
  FROM CUSTOMER AS C, SALESPESON AS S
  WHERE C.NickName = S.NickName AND S.LastName = "Jones";
  ```

  

* LEFT JOIN

  ```sql
  SELECT C.LastName, C.FirstName
  FROM CUSTOMER AS C LEFT JOIN SALESPESON AS S
  ON C.LastName = S.NickName
  ```

  

