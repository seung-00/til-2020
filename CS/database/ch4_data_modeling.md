 ## Ch 4. Data Modeling and the Entity-Relationship Model

### 개요

* ER diagram(ERD)을 이용한 데이터 모델링에서 배움. 5장에선 이를 RDB로 변환함
* 데이터베이스를 개발하기 위한 단계를 배움
* binary relationship에 대해 배움

### 3가지 단계

* Requirements Statge
  * 어떤 데이터에 대한 어떤 요구가 있으며 디비 구조를 어떻게 설계해야할 지
* Design Stage
  * 설계를 바탕으로 RDB로 전환
* Implementation Stage
  * RDBMS 구현
  * 실제 시스템 구축(Application)

### Requirements Stage

* Sources of requirements
  * User Interviews
    * 어떤 데이터, 기능이 필요 한가요?
  * Forms
    * 실제 업무에 사용하는 업무 문서 양식을 보여주세요.
    * 어떤 데이터를 사용하는지 직접 확인
  * Reports
    * 정기적인 보고서
  * Queries
    * 업무 수행할 때 필요한 검색 기능은 어떤게 있습니까?
  * Use Cases
    * 실제 사용하는 사례들(예를 들어 검색, 결제, 정보 수정)을 조사
  * Business Rules
    * 업무 수행 규칙들

### Requirements -> E-R Data Model -> RDB

* 아래 둘은 대응됨

* E-R Models consist of

  * Entity

    * Attributes
    * Identifier

  * RelationShip

    

  * Entity Class

  * Entity Instances

* RDB consist of

  * Table

    * Column
    * Primary key

  * Foreign key

    

  * Table(Design)

  * Records

* Entity class
  * a collection of entities
  * entity
    * 추적하기 원하는 데이터
  * Entity instance
    * 특정 실제 entity

* Attibutes
  
  * entity의 특성, column
* Identifiers
  * Entity instance는 ID를 갖는다. PK
  * 유일하기도 하기 유일하지 않기도 함(FK와 같은 상황)
  * Composite 할 때도 있다.

### Level of Entity Attribute Display

* E_R diagram

  * Maximum Cardinality

    * 한 instance가 다른 instance를 최대 몇 개 가질 수 있나
    * 다이아몬드 속에 표시됨

  * Minimum Cardinality

  * 주로 binary relationship으로 설계함

  * 1:1

    * 1명당 하나

    <img src="https://user-images.githubusercontent.com/46865281/81648269-65494900-9469-11ea-87c7-4845e1adac4f.png" width="500" height="150">

  * 1:N

    * 1 제품당 여러 견적서(달마다 다른 제품 수)

      <img src="https://user-images.githubusercontent.com/46865281/81648564-ddb00a00-9469-11ea-85b8-3dd5afff3d67.png" width="600" height="150">

  * N:M

    * instance 기준으로 생각
    * ITEM : SUPPLIER
      * ITEM 중 하나의 instance도 여러 SUPPLIER를 가질 수 있고, 하나의 SUPPLIER instance도 여러 item을 가질 수 있음.
    * STUDENT : DEPT
      * 만약 학생의 복수전공을 고려한다면, 다대다가 될 수 있을 것임.

### crow's foot model

* 위 전통적인 방식을 바꾼 것

* crow's foot symbols

  <img src="https://user-images.githubusercontent.com/46865281/81649869-f3263380-946b-11ea-87d5-0eca74427f7d.png" width="400" height="400">

  * 네 가지 조합이 가능

    * min cardinality: mandatory, optional(안쪽)
    * max cardinality: 1, Many(바깥쪽)

  * 예시

    <img src="https://user-images.githubusercontent.com/46865281/81650310-a7c05500-946c-11ea-9d33-ff2188160ccd.png" width="500" height="100">

    * 점원은 적어도 하나의 스킬은 가져야 함. 특정한 스킬을 가진 직원이 없을 수도 있다(optional).

* weak entity

  * strong entity 에 종속적인 것

    * 그래서 weak -> strong 방향 cardinality는 항상 최소 하나 최대 하나

  * 라운디드 사각형 모양

  * **ID-Dependent weak entity** 예시

    <img src="https://user-images.githubusercontent.com/46865281/81651350-962b7d00-946d-11ea-936b-cb91c75ab267.png" width="800" height="500">

    

    * strong entity에 의존적이면서 추가적인 정보를 제공함

    * crow's foot 모델에서, 연결 선은 점선이 디폴트

    * strong과 weak 중 ID Dependant인 경우 실선으로 표시함(더 긴밀하게 연결됐다는 의미)

      * non-ID dependant weak entity도 존재

      * strong과 종속적인 관계지만 ID를 별도로 관리하는 경우

      * 사례

        <img src="https://user-images.githubusercontent.com/46865281/81654030-469a8080-9470-11ea-93ec-88a3670787e5.png" width="500" height="200">

  * 정리 예시

    * <img src="https://user-images.githubusercontent.com/46865281/81653575-ec99bb00-946f-11ea-8534-0a217538fee0.png" width="800" height="500">

      