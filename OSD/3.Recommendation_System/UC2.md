# UC-2 Recommend

# origin
![image](https://user-images.githubusercontent.com/49024958/118102608-fa33a900-b413-11eb-8242-432ae4f99c75.png)

# var1
기존에는 data라는 concept을 추가하여 데이터를 임시로 모아두었다가 모든 데이터가 모이면 한번에 recommendation을 하게 하였다. 변형1에서는 data를 사용한 방법을 없애고, event가 발생하면 keyStorage가 userID를 각 디비에 보내면 디비가 recommendation으로 보내진다.
![OSD2](https://user-images.githubusercontent.com/49024958/118102649-061f6b00-b414-11eb-92ec-f507c977a6f8.png)

# var2
상품의 종류가 바뀌지 않는 이상 자주 바뀌지 않는 book DB와 기존의  log가 누적되어서 쌓이는 log DB는 추천을 할 때마다 데이터를 load하는 것은 비효율적이다. 
1) 따라서 booklog data는 업데이트 되었는지 판단하고, 변동사항이 없다면 이미 load된 데이터를 사용하도록 변형하였다. 이를 위한 전제조건은, admin에 의해서 보유 도서의 정보가 변경이 되었을 때 update 변수가 true로 변경되어야한다.
2) logDB connection은 timestamp를 활용하였다. 이전에 추천을 할 때 읽었던 log 데이터를 제외하고, 추천을 시작한 시점에서 그전과 비교했을 때 추가된 데이터만 읽어들이는 것이다. 즉, log 데이터를 매번 처음부터 끝까지 읽지 않고도 event가 발생해(사용자의 클릭, 검색으로 인해 들어온 데이터) log DB connection에는 이전에 추천을 마쳤던 시간이 저장되어 이 과 db 데이터의 timestamp를 비교하여 새로운 데이터가 있다면 추가한다.
![Copy of OSD2(1)](https://user-images.githubusercontent.com/49024958/118155412-2fabb700-b453-11eb-9093-a0831336d377.png)

