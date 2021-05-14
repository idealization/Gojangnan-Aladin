# Checkpoint 2: System Design Document(SDD)

Sequence Diagram and Class Diagram for Use Case based on top 30% Requirements Analysis

# 1. Basic

## UC-1: Customer Account

### (Object) Sequence Diagram

![]()

**장점**:

**단점**:

#### Variation 1

![]()

**장점**:

**단점**:

#### Variation 2

![]()

**장점**:

**단점**:

#### 최종 선택된 OSD

![]()

**선택한 이유**:

### Class Diagram based on selected OSD

![]()

## UC-2: Search Book

### (Object) Sequence Diagram

![]()

**장점**:

**단점**:

#### Variation 1

![]()

**장점**:

**단점**:

#### Variation 2

![]()

**장점**:

**단점**:

#### 최종 선택된 OSD

![]()

**선택한 이유**:

### Class Diagram based on selected OSD

![]()

## UC-9: Book Data

### (Object) Sequence Diagram

![]()

**장점**:

**단점**:

#### Variation 1

![]()

**장점**:

**단점**:

#### Variation 2

![]()

**장점**:

**단점**:

#### 최종 선택된 OSD

![]()

**선택한 이유**:

### Class Diagram based on selected OSD

![]()

## UC-10: Admin Account

### (Object) Sequence Diagram

![]()

**장점**:

**단점**:

#### Variation 1

![]()

**장점**:

**단점**:

#### Variation 2

![]()

**장점**:

**단점**:

#### 최종 선택된 OSD

![]()

**선택한 이유**:

### Class Diagram based on selected OSD

![]()

# 2. Payment

## UC-1: Prepare Payment

### (Object) Sequence Diagram

![]()

**장점**:

**단점**:

#### Variation 1

![]()

**장점**:

**단점**:

#### Variation 2

![]()

**장점**:

**단점**:

#### 최종 선택된 OSD

![]()

**선택한 이유**:

### Class Diagram based on selected OSD

![]()

## UC-2: Payment Process

### (Object) Sequence Diagram

![]()

**장점**:

**단점**:

#### Variation 1

![]()

**장점**:

**단점**:

#### Variation 2

![]()

**장점**:

**단점**:

#### 최종 선택된 OSD

![]()

**선택한 이유**:

### Class Diagram based on selected OSD

![]()

## UC-3: Cart

### (Object) Sequence Diagram

![]()

**장점**:

**단점**:

#### Variation 1

![]()

**장점**:

**단점**:

#### Variation 2

![]()

**장점**:

**단점**:

#### 최종 선택된 OSD

![]()

**선택한 이유**:

### Class Diagram based on selected OSD

![]()

# 3. Recommendation

## UC-1: History

### (Object) Sequence Diagram

![image](https://user-images.githubusercontent.com/49024958/118250088-0df91100-b4e1-11eb-9fe5-c69b1a917298.png)

**장점**:
-logger가 바로 사용자의 데이터를 받아 controller가 전달하는 내용을 기다리지 않는다. 
-비정상 접근을 염려해두고 사용자가 가지고 있던 key를 다시 한번 체크하도록 checker를 두었다. 

**단점**:
-logger가 바로 사용자의 데이터를 받고, 그 data가 책에 관한 내용인지 필터하고 보내야한다. 
-또한 로그인 되어있는 사용자의 id는 이미 유효한 id인지 확인을 거친 id이다.
#### Variation 1

![image](https://user-images.githubusercontent.com/49024958/118250007-fb7ed780-b4e0-11eb-8b5a-a7e14aa189ed.png)

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

![image](https://user-images.githubusercontent.com/49024958/118250741-bc04bb00-b4e1-11eb-8b33-cbaeb3b1e9e2.png)

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

![image](https://user-images.githubusercontent.com/49024958/118250708-b5764380-b4e1-11eb-8224-fd1044dbbf9f.png)
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
![image](https://user-images.githubusercontent.com/49024958/118250708-b5764380-b4e1-11eb-8224-fd1044dbbf9f.png)

**선택한 이유**:
데이터의 중복 로드를 해결해야할 가장 큰 우선순위로 보았다. origin에 비해 controller의 역할이 단순해졌고, 사용자의 기록에 따라 추천이 수행되려면 recommendtation이 효율적으로 데이터를 받아야하기 때문이다.

### Class Diagram based on selected OSD

![23](https://user-images.githubusercontent.com/49024958/118251313-6250c080-b4e2-11eb-8ea0-37ab6a05aeef.png)

## UC-3: Display

### (Object) Sequence Diagram

![]()

**장점**:

**단점**:

#### Variation 1

![]()

**장점**:

**단점**:

#### Variation 2

![]()

**장점**:

**단점**:

#### 최종 선택된 OSD

![]()

**선택한 이유**:

### Class Diagram based on selected OSD

![]()

## UC-4: Browser

### (Object) Sequence Diagram

![]()

**장점**:

**단점**:

#### Variation 1

![]()

**장점**:

**단점**:

#### Variation 2

![]()

**장점**:

**단점**:

#### 최종 선택된 OSD

![]()

**선택한 이유**:

### Class Diagram based on selected OSD

![]()
