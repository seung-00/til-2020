# Ch 5. Database Design
## 개요
* E-R data model -> relational designs 
* normalization, denormalization process 연습
## Data Model(E-R Diagram) -> Relational Design
### each entity로 table 만들기
* entity identifier -> PK
* entity의 각 attribute -> column
* 정규화
### FK로 relationships 만들기
* 1:1, 1:N, N:M 구별
* ID 의존성 여부
### 정규화
* 왜 하는가?
	* 수정 문제(삽입, 수정, 삭제)를 해결하기 위해
* 어떻게 하는가?
  * Functional Dependency 찾음
  * Determinant 찾음
  * Candidate Key인지 확인
  	* 아니라면 기본 CK를 FK로 두고 새로운 PK
  * Normal Forms
  	* 보통 3NF, BCNF(모든 Determinant가 CK) 정도가 일반적으로 쓰임
* 예시
  * 예를 들어서 `CUSTOMER(CustomerNumber, CustomerName, City, State, ZIP, ContactName, Phone)` 가 있을 때
  * ZIP(우편번호) -> (City, State), ContactName -> Phone 라는 Functional Relationship이 있으므로 이 둘을 나눌 수 있음
* Denomalization
  * 그러나 이보다는 `CUSTOMER(CustomerNumber, CustomerName, City, State, ZIP)` 과 `CONTACT(ContatctName, Phone)`  으로 둘만 나누는 것이 좋음
    1. `City`~`ZIP` 은 항상 함께 쓰이므로 굳이 쪼갤 필요가 없음
    2. 수정 문제 발생 가능성도 적음
       * insert는 어차피 함께 됨
       * update는 자주 안 됨
       * delete 한 명의 고객을 위한 정보들이므로 각각 지울 필요가 없음
       * 쪼갤 수록 Join할 때 낭비가 발생함

### Representing Relationships

* 1:1 Relatitonship Example

  * 두 테이블의 우위가 없으므로 둘 중 한 쪽만 FK로 연결되면 됨

  * E-R은 어느쪽이 FK인지 고려하지 않으므로, 디자이너가 알아서 줘야함

  * 예시

    * `Employee(EmployeeNumber, LastName, Firstname, OfficeNumber, OfficePhone)` 와 `Locker(LockerNumber, LockerRoom, LockerSize)`

    * Employee에 LockerNumber(FK)를 넣는 경우 JOIN SQL

      ```sql
      SELECT *
      FROM LOCKER, EMPLOYEE
      WHERE LOCKER.LockerNumber = EMBPLOYEE.LockerNumber;
      ```

    * Locker에 EmployeeNumber(FK)를 넣는 경우 JOIN SQL

      ```sql
      SELECT *
      FROM LOCKER, EMPLOYEE
      WHERE LOCKER.EmployeeNumber = EMBPLOYEE.EmployeeNumber;
      ```

* 1:N Relatitonship Example

  * 자식 쪽(N)에  FK가 있어야 함

    * 한 instance에 하나의 값이 있어야 하므로, 부모 쪽에서 N개의 자식 PK를 FK로 가지고 있을 수 없음

  * 예시

    * `Item(ItemNumber, Description, Cost, ListPrice, QuantityOnHand)` 와 `QUOTATION(QuoteNumber, VendorName, Quantity, CostEach)`

    * JOIN SQL

      ```sql
      SELECT *
      FROM	ITEM, QUOTATION
      WHERE	ITEM.ItemNumber = QUOTATION.ItemNumber;
      ```

* N:M Relatitonship Example

  * 예시

    * `STUDENT(SID, StudentName, Phonem, EmailAddress)``, CLASS(ClassNumber, ClassTime, ClassName, Description)`

    * Intersection Table을 추가하여 관계를 표현한다.

      * `STUDENT_CLASS(SID(FK), ClassNumber(FK))`
      * 각각 N, M은 Intersection Table과 1:N 관계가 됨(학생 한 명이 여러 수업, 한 수업이 여러 학생)

    * JOIN SQL

      ```sql
      SELECT *
      FROM	STUDENT, CLASS, STUDENT_CLASS
      WHERE	STUDENT.SID = STUDENT_CLASS.SID
      	AND	STUDENT_CLASS.ClassNumber = CLASS.ClassNumber;
      ```

  * association relationship을 써서 관계에 추가 정보를 넣어줄 수도 있음(참고)

