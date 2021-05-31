# Checkpoint 3: Implement and Demo

Sequence Diagram and Class Diagram for Use Case based on top 30% Requirements Analysis


# Index
- [1. Basic](#1-basic)
- [2. Payment](#2-payment)
- [3. Recommendation](#3-recommendation)


# 1. Basic

## UC-1: Customer Account

### (Object) Sequence Diagram

![osd1](https://github.com/idealization/software-engineering/blob/268fa8bb1007bee435057cc8e93b0aed9242c06e/OSD/01_basic/image/osd1.jpg)

**장점**: sign in 하려는 주체에 따라 과정을 분리함으로써 데이터베이스 상에 저장된 로그인 정보 (id와 password, 변수로는 key)를 불러오고 입력값과 비교하는 과정에서 효율성이 높아진다.

**단점**: customer의 sign in과 admin의 sign in에 대한 비슷한 과정이 반복적으로 나타난다. 

#### Variation 1

![osd1-1](https://github.com/idealization/software-engineering/blob/268fa8bb1007bee435057cc8e93b0aed9242c06e/OSD/01_basic/image/osd1-1.jpg)

**장점**: 비슷한 과정을 통합하여 시스템의 동작을 더 간결하게 표현 및 구현할 수 있다.

**단점**: sign in 동작 시 접근해야 하는 데이터의 양이 더 많아지고 효율성이 떨어진다.

#### 최종 선택된 OSD

![osd1](https://github.com/idealization/software-engineering/blob/268fa8bb1007bee435057cc8e93b0aed9242c06e/OSD/01_basic/image/osd1.jpg)

**선택한 이유**: 불필요한 연산을 제거하고 시스템의 효율성을 높이기 위해 sign in의 주체에 따라 과정이 분리되는 방식을 채택한다.

## UC-2: Search Book, UC-3: Add to Cart, UC-4: Book Detail

### (Object) Sequence Diagram

![osd234](https://github.com/idealization/software-engineering/blob/268fa8bb1007bee435057cc8e93b0aed9242c06e/OSD/01_basic/image/osd234.jpg)

**선택한 이유**: 각 usecase는 사용자 입력 및 데이터 출력의 순차적 과정을 따른다.

### Class Diagram based on selected OSD

![0102](https://github.com/idealization/software-engineering/blob/c0e9b3e4612fd8f4dd7229a707f1aebb6349bf4a/Class_Diagram/01_basic/image/0102.jpg)
![0304](https://github.com/idealization/software-engineering/blob/c0e9b3e4612fd8f4dd7229a707f1aebb6349bf4a/Class_Diagram/01_basic/image/0304.jpg)


## UC-9: Book Data

### (Object) Sequence Diagram

![image](https://github.com/idealization/software-engineering/blob/main/OSD/01_basic/image/osd09.jpg)

**장점**: 수정된 내용을 모두 db connection에 저장하놓고 있다가 수정이 모두 끝나면 한번에 update를 한다. 

**단점**: 수정할 때마다 update 되는 것이 아니라 만약 실수로 시스템이 꺼져버리면 수정된 내용이 전부 사라질 수 있다.

#### Variation 1

![image](https://github.com/idealization/software-engineering/blob/main/OSD/01_basic/image/osd09-1.jpg)

**장점**: 수정할 때마다 update가 되므로 중간에 시스템이 꺼져도 내용은 그대로 있다.

**단점**: 계속 db connection 과 database 에 update를 해야하기 때문에 시간이 느리다.


#### 최종 선택된 OSD

![image](https://github.com/idealization/software-engineering/blob/main/OSD/01_basic/image/osd09.jpg)

**선택한 이유**: 계속 database에 update를 하거나 load할 필요가 없으니 빨리빨리 수정이 가능하다.

### Class Diagram based on selected OSD

![image](https://github.com/idealization/software-engineering/blob/main/Class_Diagram/01_basic/image/09.jpg)

## UC-10: Admin Account

### (Object) Sequence Diagram

![image](https://github.com/idealization/software-engineering/blob/main/OSD/01_basic/image/osd10.jpg)

**장점**: authorizer 가 있기 때문에 정보에 신뢰성이 있고 vaild한 데이터만 저장하는 검문소 역할을 할 수 있다.

**단점**: save 하기 전 authorizer가 있기 때문에 시간이 더 걸린다

#### Variation 1

![iamge](https://github.com/idealization/software-engineering/blob/main/OSD/01_basic/image/osd10-1.jpg)

**장점**: authorizer 가 없기 때문에 빨리 database에 update가 가능하다.

**단점**: authorizer가 없어서 vaild한 데이터가 들어오지 않더라고 database에 저장될 수 있다.


#### 최종 선택된 OSD

![image](https://github.com/idealization/software-engineering/blob/main/OSD/01_basic/image/osd10.jpg)

**선택한 이유**: 시간이 조금 더 걸리지만 vaild 한 데이터만 저장하도록 한다

### Class Diagram based on selected OSD

![image](https://github.com/idealization/software-engineering/blob/main/Class_Diagram/01_basic/image/10.jpg)

# 2. Payment

## UC-1: Prepare Payment

### (Object) Sequence Diagram

![UC-1_draft](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd1.png?raw=true)

**장점**

- Shorter communication chain

**단점**

- Extra responsibility for Controller
  - Controller가 각 Concept별 연결 뿐만 아니라 Request용 data 선별 및 생성 작업까지 책임짐
  - makeBookRequest()

#### Variation 1

![UC-1_va1](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd1_va1.png?raw=true)

**장점**

* Controller focused on its specialty == Strong Cohesion
  * Controller에서 request를 위한 data 선별 및 생성 책임을 Requester로 분리하여 Controller는 각 Concept간 연결에만 책임을 지고, Request는 Database Connection에 request하는 작업의 책임을 갖음

**단점**

- Longer communication chain
  - Requester Concept가 추가되면서 communication chain이 길어짐

#### 최종 선택된 OSD

variation1

![UC-1_selectedOSD](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd1_va1.png?raw=true)

**선택한 이유**: 두 OSD 모두 고객의 요구를 잘 반영하지만 variation1이 이후 시스템 유지 보수에 있어 더 적합하다고 판단했기 때문

### Class Diagram based on selected OSD

![UC-1_CD](https://github.com/idealization/software-engineering/raw/main/Class_Diagram/02_payment/img/UC-1,3_va1.png?raw=true)

## UC-2: Payment Process

### (Object) Sequence Diagram

![UC-1_draft](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd2.png?raw=true)

**장점**

- Archiver는 DB에 tuple을 추가하는 update query를 담당하고, Deleter는 DB에서 일부 tuple을 제거하는 delete query를 담당하여 두 책임을 분리시킴

**단점**

- Longer communication chain
- Extra responsibility for Controller
  - Controller가 각 Concept별 연결 뿐만 아니라 Request용 data 선별 및 생성 작업까지 책임짐
  - makeBookRequest()
- Controller가 DB에 어떤 작업을 해야 하는지 판단해서 Archiver와 Deleter 둘 중 어느 Concept와 연결되야 할지 판단함

#### Variation 1

![UC-2_va1](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd2_va1.png?raw=true)

**장점**

- Shortest communication chain
  - 기존 OSD에서 Archiver와 Deleter를 제거하고 해당 작업을 Controller가 하도록 변경

**단점**

- Extra responsibility for Controller
  - Controller가 각 Concept별 연결 뿐만 아니라 Request용 data 선별 및 생성 작업까지 책임짐
  - makeBookRequest()
- Controller가 DB에 어떤 작업을 해야 하는지 판단해서 Archiver와 Deleter 둘 중 어느 Concept와 연결되야 할지 판단함

#### Variation 2

![UC-2_va2](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd2_va2.png?raw=true)

**장점**

- Controller focused on its specialty == Strong Cohesion
  * Controller에서 request를 위한 data 선별 및 생성 책임을 Requester로 분리하여 Controller는 각 Concept간 연결에만 책임을 지고, Request는 Database Connection에 request하는 작업의 책임을 갖음
- Controller는 어던 데이터를 Request에 넘겨야하는지만 판단하고 Data에 따라 update query인지 delete query인지는 Requester가 결정함
- 모든 책임을 최대한 분리하여 high cohesion principle에 가장 부합함

**단점**

- Longest communication chain
- Archiver와 Deleter모두 Database connection의 method를 호출하는 것이므로 책임이 비슷한데 분리되어 expert doer principle에 위배됨

#### Variation 3

![UC-2_va3](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd2_va3.png?raw=true)

**장점**

- Shorter communication chain
- Controller focused on its specialty == Strong Cohesion
  * Controller에서 request를 위한 data 선별 및 생성 책임을 Requester로 분리하여 Controller는 각 Concept간 연결에만 책임을 지고, Request는 Database Connection에 request하는 작업의 책임을 갖음
- Controller는 어던 데이터를 Request에 넘겨야하는지만 판단하고 Data에 따라 update query인지 delete query인지는 Requester가 결정함

**단점**

- Not shortest communication chain

#### 최종 선택된 OSD

variation3

![UC-2_selectedOSD](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd2_va3.png?raw=true)

**선택한 이유**: variation3은 적당히 짧은 communication chain을 가지며 Strong Cohesion Principle에 부합하고, 또한 어느정도 비슷한 기능끼리 묶여있으며, 유지 보수 비용이 적은 편인 OSD이기 때문

### Class Diagram based on selected OSD

![UC-2_CD](https://github.com/idealization/software-engineering/raw/main/Class_Diagram/02_payment/img/UC-2_va3.png?raw=true)

## UC-3: Cart

### (Object) Sequence Diagram

![UC-2_draft](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd3.png?raw=true)

**장점**

- Shorter communication chain

**단점**

- Extra responsibility for Controller
  - Controller가 각 Concept별 연결 뿐만 아니라 Request용 data 선별 및 생성 작업까지 책임짐
  - makeBookRequest()

#### Variation 1

![UC-3_va1](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd3_va1.png?raw=true)

**장점**

* Controller focused on its specialty == Strong Cohesion
  * Controller에서 request를 위한 data 선별 및 생성 책임을 Requester로 분리하여 Controller는 각 Concept간 연결에만 책임을 지고, Request는 Database Connection에 request하는 작업의 책임을 갖음

**단점**

- Longer communication chain
  - Requester Concept가 추가되면서 communication chain이 길어짐

#### 최종 선택된 OSD

variation1

![UC-3_selectedOSD](https://github.com/idealization/software-engineering/raw/main/OSD/02_payment/image/osd3_va1.png?raw=true)

**선택한 이유**: 두 OSD 모두 고객의 요구를 잘 반영하지만 variation1이 이후 시스템 유지 보수에 있어 더 적합하다고 판단했기 때문

### Class Diagram based on selected OSD

![UC-3_CD](https://github.com/idealization/software-engineering/raw/main/Class_Diagram/02_payment/img/UC-1,3_va1.png?raw=true)

# 3. Recommendation

## UC-1: History

### (Object) Sequence Diagram

![image](https://user-images.githubusercontent.com/49024958/118250007-fb7ed780-b4e0-11eb-8b5a-a7e14aa189ed.png)

**장점**:
-logger가 바로 사용자의 데이터를 받아 controller가 전달하는 내용을 기다리지 않는다. 

-비정상 접근을 염려해두고 사용자가 가지고 있던 key를 다시 한번 체크하도록 checker를 두었다. 

**단점**:
-logger가 바로 사용자의 데이터를 받고, 그 data가 책에 관한 내용인지 필터하고 보내야한다. 

-또한 로그인 되어있는 사용자의 id는 이미 유효한 id인지 확인을 거친 id이다.
#### Variation 1

![image](https://user-images.githubusercontent.com/49024958/118250088-0df91100-b4e1-11eb-9fe5-c69b1a917298.png)

**장점**:
외부에서 전달되는 데이터를 받고 event가 발생했음을 알려주는 역할을 controller로 지정했다. 따라서 logger는 사용자의 입력을 대기할 필요없이 controller한테서 메시지를 받으면 필터를 수행하고 db에 데이터를 전송한다. 

**단점**:
db connection은 고객 ID와 데이터를 모두 받아야 db로 저장이 된다. 그런데, logger와 keystroage는 서로의 존재를 모르기 때문에 둘 중 하나가 잘못 되면 log db는 대기하게 되거나 다른 문제가 생길 수 있다.
예를 들어 필터를 하던 중에 새로운 입력이 들어오면 사용자의 id만 갱신되어 전달될 수 있다.

#### Variation 2

![image](https://user-images.githubusercontent.com/49024958/118250096-12252e80-b4e1-11eb-8ddf-c448a6a12297.png)

**장점**:
logger의 filter data를 event로 정의하고, event가 발생시 keystorage가 ID를 보내도록 하여 log db의 활성화 시간을 줄인다.

**단점**:
logger가 필터를 한 후 keystorage에게 메세지도 보내고, db connection에 data를 보내야한다. 

#### 최종 선택된 OSD
(variation 2)
![image](https://user-images.githubusercontent.com/49024958/118250186-25d09500-b4e1-11eb-96d9-4a6a14e86add.png)

**선택한 이유**:
지금 단계에서는 권한이 확인된 key라면 버그에 의해 비정상 접근이 발생하는 가능성을 배제하였다.
controller가 오직 하나의 객체에 메세지를 전달함으로서 사용자 입력이 연속으로 들어왔을 때 빠르게 처리가 가능하고, log 데이터와 ID가 한 묶음이라는 것이 눈에 잘 들어온다. 

### Class Diagram based on selected OSD

![12](https://user-images.githubusercontent.com/49024958/118251161-2f0e3180-b4e2-11eb-9395-ac7ef9bd338e.png)

## UC-2: Recommend

### (Object) Sequence Diagram

![image](https://user-images.githubusercontent.com/49024958/118250708-b5764380-b4e1-11eb-8224-fd1044dbbf9f.png)

**장점**:
data라는 concept을 추가하여 데이터를 임시로 모아두었다가 모든 데이터가 모이면 한번에 recommendation을 하게 하였다. 따라서 recommendation이 필요한 데이터를 받기 위한 대기 시간이 줄어든다. 

**단점**:
먼저 처리할 수 있는 데이터도 다른 데이터와 한번에 들어오기 때문에 data를 받은 다음 추천을 위해 처리할 일이 몰린다.

#### Variation 1

![image](https://user-images.githubusercontent.com/49024958/118250732-b9a26100-b4e1-11eb-94ba-d4408fe16d5e.png)
(부연 설명)
페이지와 버튼이 새로고침이 되는 event가 발생하면 keyStorage가 userID를 각 디비에 보낸다. 그러면 DB가 recommend로 보내진다.

**장점**:
먼저 전송된 데이터를 recommendation이 사용할 수 있다. controller는 오직 keystorage에게만 새로고침 event를 전송한다. 따라서 ID를 가지고 있는 keystorage가 바로 ID가 필요한 객체에 전달을 할 수 있다.

**단점**:
event가 발생할 때마다 매번 db가 새로 로드된다. 특히 book DB의 특성 상 admin에 의해 상품 리스트가 변경되지 않으면 기존에 로드한 데이터와 중복되는 것이 많다. log data 또한 과거의 log는 계속 누적되기 때문에 새로 받을 필요가 없다.

#### Variation 2

![image](https://user-images.githubusercontent.com/49024958/118250741-bc04bb00-b4e1-11eb-8b33-cbaeb3b1e9e2.png)
(부연 설명)
(과정)
1. 따라서 booklog data는 업데이트 되었는지 판단하고, 변동사항이 없다면 이미 load된 데이터를 사용하도록 변형하였다. 이를 위한 전제조건은, admin에 의해서 보유 도서의 정보가 변경이 되었을 때 update 변수가 true로 변경되어야한다.
2. logDB connection은 timestamp를 활용하였다. 이전에 추천을 할 때 읽었던 log 데이터를 제외하고, 추천을 시작한 시점에서 그전과 비교했을 때 추가된 데이터만 읽어들이는 것이다. 즉, log 데이터를 매번 처음부터 끝까지 읽지 않고도 event가 발생해(사용자의 클릭, 검색으로 인해 들어온 데이터) log DB connection에는 이전에 추천을 마쳤던 시간이 저장되어 이 과 db 데이터의 timestamp를 비교하여 새로운 데이터가 있다면 추가한다.

**장점**:
option 조건을 두어 DB에서 중복된 데이터를 update 변수와 timestamp를 통해서 추려낼 수 있다. 따라서 데이터 로드가 중복되지 않는다. 

**단점**:
데이터의 수가 많아질수록 추천 알고리즘이 돌아가는 시간도 길어진다면, contoller가 다음 event를 전달하기까지 시간이 걸린다.  

#### 최종 선택된 OSD
(variation 2)
![image](https://user-images.githubusercontent.com/49024958/118250741-bc04bb00-b4e1-11eb-8b33-cbaeb3b1e9e2.png)

**선택한 이유**:
데이터의 중복 로드를 해결해야할 가장 큰 우선순위로 보았다. origin에 비해 controller의 역할이 단순해졌고, 사용자의 기록에 따라 추천이 수행되려면 recommendtation이 효율적으로 데이터를 받아야하기 때문이다.

### Class Diagram based on selected OSD

![23](https://user-images.githubusercontent.com/49024958/118251313-6250c080-b4e2-11eb-8ea0-37ab6a05aeef.png)

## UC-3: Display

### (Object) Sequence Diagram

![image](https://user-images.githubusercontent.com/55435898/118111390-96fb4400-b41e-11eb-9fbf-0e6e76cd2c86.png)

**장점**: 컨트롤러에서 바로 사용자가 클릭한 버튼에 대한 처리를 바로바로 할 수 있다. 그리고 더 가볍게 처리할 수 있다.

**단점**: 버튼이 추가 될 경우 컨트롤러의 코드를 수정해야 하는 등 추가 기능에 대한 수정이 힘들다.

#### Variation 1

![image](https://user-images.githubusercontent.com/55435898/118111445-ab3f4100-b41e-11eb-9f23-768c2143aa7b.png)

**장점**: 인터페이스 페이지에 더 다양한 버튼 등 기능이 추가 될 경우 컨트롤러의 수정 없이 버튼컨트롤러 수정과 새로운 기능만 수정해주면 된다.

**단점**: 더 많은 메모리를 사용하며 덜 직관적이다.


#### 최종 선택된 OSD

![image](https://user-images.githubusercontent.com/55435898/118111445-ab3f4100-b41e-11eb-9f23-768c2143aa7b.png)

**선택한 이유**: 추후에 추천 알고리즘을 무엇을 사용하느냐에 따라 필요한 버튼이나 추가 기능이 생길 가능성이 크기 때문에 더 많은 메모리를 사용하더라도 기능을 추가하기 편한 OSD를 선택하였다.

### Class Diagram based on selected OSD

![image](https://user-images.githubusercontent.com/55435898/118206675-f64c6900-b49d-11eb-80a9-c676ba297e90.png)

## UC-4: Browser

### (Object) Sequence Diagram

![image](https://user-images.githubusercontent.com/55435898/117532035-74cd8480-b020-11eb-9516-b7a44481e83c.jpg)

**장점**: 인터페이스 페이지에서 사용자 행동에 대한 값을 받으면 컨트롤러에서 바로 판단하여 관련된 행동 요청을 보내기 때문에 빠르고 간단하다. 그리고 logger로 보낼 쓸모있는 log가 발생할 때만 Logger로 보낸다.

**단점**: 인터페이스 페이지에 키 값이 다양해지면 컨트롤러의 코드를 수정해야하는 위험성이 있다.

#### Variation 1

![image](https://user-images.githubusercontent.com/55435898/117681212-d3dff480-b1ec-11eb-8486-cbf193235518.jpg)

**장점**: key컨트롤에서 key관련 행동들을 모두 처리하기 때문에 key가 생성, 제거, 수정 등이 발생할 경우 변환이 쉽다.

**단점**: 들어온 key가 관련 행동이 없는 의미없는 key값이라도 마지막에 logger로 data를 전달해야하는 행위를 해야한다. 그리고 만약 key가 추가되지 않을 예정이라면 메모리나 구조들이 이렇게 커질 필요가 없어보인다.

#### 최종 선택된 OSD

![image](https://user-images.githubusercontent.com/55435898/117681212-d3dff480-b1ec-11eb-8486-cbf193235518.jpg)

**선택한 이유**: 인터페이스 페이지가 프로그램상에서 메인페이지이기 때문에 새로운 key가 생기거나 바뀔 확률이 높다. 그리고 메인페이지에 점점 더 다양한 기능을 넣을 때마다 key값이 많이지고 이에 해당하는 행동을 해야하는 메소드들도 많아지는 등 구조가 더 커질 가능성이 많기 때문에 선택하였다.

### Class Diagram based on selected OSD

![image](https://user-images.githubusercontent.com/55435898/118111064-25bb9100-b41e-11eb-92c8-4326f3d408f3.png)
