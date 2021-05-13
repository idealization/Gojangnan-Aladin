# UC1 - History
goal: To collect customer's history log

# Original
![image](https://user-images.githubusercontent.com/49024958/118085118-cac57200-b3fc-11eb-86fc-557a8ae691a1.png)

# var1
logger가 log를 받고 필터까지 하는데, 하나의 컨셉이 수행하는 주요 역할을 명확히 하기 위해서, controller에게서 정보를 받고 의미있는 데이터를 남기는 필터를 행하도록 바꾸었다. 
![OSD (2)](https://user-images.githubusercontent.com/49024958/118085627-ad44d800-b3fd-11eb-9dc0-53390509b2e9.png)


# var2
logDB가 ID를 받고 logger가 필터할 때까지 대기하는 것이 신경쓰임, 따라서 filter data를 event로 하여서 event가 발생시 ID를 보내도록 하였다.
![OSD (1)](https://user-images.githubusercontent.com/49024958/118085536-85557480-b3fd-11eb-9c76-2f13528f2c60.png)
