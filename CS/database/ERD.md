## **ERD(Entity Relationship Diagram)**

## 개요

> "구조"화된 데이터를 저장하기 위해 데이터베이스를 쓴다. 이 데이터의 "구조" 및 그에 수반한 제약 조건들은 다양한 기법에 의해 설계될 수 있다. 그 기법 중 하나가 개체-관계 모델링(Entity-Relationship Modelling)이다. 줄여서 ERM이라고 한다. ERM 프로세스의 산출물을 가리켜 개체-관계 다이어그램(Entity-Relationship Diagram)이라 한다. 줄여서 ERD라 일컫는다. 데이터 모델링 과정은 데이터 모델을 그림으로 표현하기 위해 표시법을 필요로 한다. ERD는 개념적 데이터 모델 혹은 시맨틱 데이터 모델의 한 타입이다.
>
> 출처: 위키백과

- ERD로 Entity-Relationship Modelling을 표현하고 이후 이를 RDB로 변환할 수 있다.
- Entity(개체)는 표현하고자 하는 테마이며 하나의 Table에 대응된다. Instance는 Record에 대응된다.



### 3가지 단계

DB 설계는 다음의 단계를 거치며, ERD는 클라이언트의 요구를 확인하는 단계와 RDB를 설계하는 단계 중간에 쓰인다.

- Requirements Statge
  - 어떤 데이터에 대한 어떤 요구가 있으며 디비 구조를 어떻게 설계해야할 지
- Design Stage
  - 설계를 바탕으로 RDB로 전환
- Implementation Stage
  - RDBMS 구현
  - 실제 시스템 구축(Application)



### Cardinality

- Cardinality(관계성)은 Entity 사이의 관계를 의미한다(1:1, 1:多 ...)

- Maximum Cardinality

  - 한 instance가 다른 instance를 최대 몇 개 가질 수 있는지를 나타낸다. 

    - 1(단일) 아니면 many(다수)

  - 예시를 들어 이해해보자!

    - 다음 다이어그램 1:1 관계를 표현하고 있다. 직원과 라커는 각각 일대일로 대응되기 때문이다.

      <img src="https://blog.kakaocdn.net/dn/cWb9vc/btqFLfx88sa/uFx5KsH5rWQ0zIYgfAkgB1/img.png" width="400" height="70">

    - 다음 다이어그램은 N:1 관계를 표현한다. 한 품목에 여러 견적서가 대응될 수 있다. 또한 한 학과에 여러 학생들이 대응될 수 있다.

      <img src="https://blog.kakaocdn.net/dn/kRfTN/btqFLgX8On3/HlS4YYqk841n1bUPgqS8G0/img.png" width="400" height="130">

    * 이번에는 N:M이다. 하나의 품목이 여러 공급자로부터 공급될 수도 있고, 하나의 공급자가 여러 품목을 제공할 수 있다.

      * 즉 커피를 A사, B사, C사에서 공급할 수 있고, A사는 커피 말고도 차를 공급하고 있을 수도 있다는 말.

        <img src="https://user-images.githubusercontent.com/46865281/87846194-199f9980-c909-11ea-9de4-43edcb106405.png" width="400" height="60">

* Minimum Cardinality

  * 한 instance가 다른 instance를 최소 몇 개 가져야 하는지 나타낸다

    * 0(optional) 혹은 1(mandatory)

  * 예시를 들어 이해해보자.

    * 아래 다이어그램에서 빨간 원은 minimum cardinality = 0을 의미하고, 빨간 직선은 minimum cardinality = 1을 의미한다 
      * 공급자 Instance는 품목 Instance가  Null일 수 있지만, 품목 Instance는 공급자 Instance가 필요하다는 것을 의미

    <img src="https://user-images.githubusercontent.com/46865281/87846909-8f5a3400-c90e-11ea-894b-d60380cfd1da.png" width="400" height="52">



### Crow's Foot

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/ERD-artist-performs-song.svg/370px-ERD-artist-performs-song.svg.png" width="400" height="100">

그림 출처: 위키피디아

* ERD는 주로 Crow's Foot 표기법으로 표기된다. 
  * Crow's Foot은 Entity 사이의 관계를 선으로 나타내고 Maximum/Minimum Cardinality를 선의 끝에 표시한다
  * Entity는 사각형 or 모서리가 둥근 사각형으로 나타낸다.
* 선
  * 실선: Weak Entity와 Strong Entity가 ID-Dependent로 연결된 경우 실선으로 표기한다. 
    * 즉 부모 테이블의 PK가 자식 테이블의 FK로 쓰이는 경우이다. 두 Entity 사이의 관계가 그만큼 타이트하니까 점선이 아닌 실선이 쓰인다고 생각하면 될듯!
    * Weak, Strong Entity 개념은 아래에 설명
  * 점선: 위의 경우를 제외한 경우 점선이 쓰인다.
* Cardinality
  * 까마귀 발 마지막 기호로 Cardinality를 표현하며 바깥쪽은 Maximum, 안쪽은 Minimum을 의미한다.
  * 고리: 0을 나타낸다. 즉 Minimum Cardinality에서 Optional을 의미함
  * 직선(세로선): 1을 나타낸다. Maximum, Minimum 모두 동일
  * 까마귀발: 다수를 나타낸다. 즉 Maximum에서 N의 경우

* 위에 올린 위키피디아의 그림은 Artist Entity와 Song Entity의 관계를 표현한 Crow's Foot ERD이다.
  * 아티스트는 여러 음악에 대응될 수 있으며(Max=many) 없을 수도 있다(Min=0).
  * 음악은 최대 한 명의 아티스트에 대응되(Max=1) 최소 한 명은 있어야 한다(Min=1).
    * 물론 실제 음악은 여러 아티스트가 듀엣으로 부르거나, 피쳐링 할수도 있다. 고객의 요구와 가정에 따라 같은 주제여도 다르게 ERD가 그려질 수 있는 것이다.

### Strong/Weak Entity

* Strong Entity 없이 존재할 수 없는 Enity

  * 예를 들어 BUILDING과 APARTMENT 라는 두 Entity를 가정하자. APARTMENT는 BUILDING 없이 존재할 수 없는 Weak Entity다.
  * ERD에서 Weak Entity는 모서리가 둥근 사각형으로 나타낸다.

* Weak  Entity에는 ID-Dependant Weak Entity와 Non ID-Dependant가 있다.

  * ID-Dependant Weak Entity는 Srong Entity의 ID(Primary Key)를 Composit ID의 요소로 가져다 쓴다.

  * 이때 각 Entity는 점선이 아닌 실선으로 연결된다.

    <img src="https://user-images.githubusercontent.com/46865281/87849437-a8211480-c923-11ea-81b0-af209f40ff39.png" width="650" height="170">

    

  * Non ID-Dependant Weak Entity는 Strong Entity와 독립적인 ID를 가진다.

    * 아래 다이어그램에서 오른쪽이 Non ID-Dependan Entity임

    <img src="https://user-images.githubusercontent.com/46865281/87849528-4ad99300-c924-11ea-8c8e-d2b7bb73ae94.png" width="650" height="460">

* 예시들

<img src="https://user-images.githubusercontent.com/46865281/87854612-209ccb00-c94e-11ea-8c30-6d06b195a3d1.png" width="650" height="460">

### SuperType/SubType Entity

* SuperType, SubType은 OOP의 상속과 같은 개념이다

* SuperType Entity의 속성들은 Subtype Entity도 물려받으며 ID 역시 동일하다.

* SuperType과 SubType 간에는 IS-A 관계가 성립한다. 즉 동일한 대상을 의미함

  * 아래 다이어그램은 SUDENT라는 SuperType Entity와 UDERGRADUATE, GRADUATE 라는 Subtype Entity가 연결되어 있다.

  <img src="https://user-images.githubusercontent.com/46865281/87855245-f0572b80-c951-11ea-9005-fd169e399d21.png" width="400" height="300">

### Recursive Relationship

* 지금까지는 다대다, 다대일, 일대일 관계들에 대해 다뤘다.  다음 예시를 통해 한 Entity만으로 재귀적인 관계를 표현할 수 있음을 알수 있다.

  * 관계는 실질적으로 Entity와 Entity가 아닌 Instance와 Instance 간에 이뤄지는 것이므로 가능한 것임

* 아래 다이어그램은 추천인 관계를 나타낸 ERD다. 

  <img src="https://user-images.githubusercontent.com/46865281/87855365-b6d2f000-c952-11ea-9d98-11109ea4b210.png" width="400" height="300">