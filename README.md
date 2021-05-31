# Checkpoint 3: Implement and Demo
## Gojangnan Aladin: Online book recommendation system using Collaborative filtering

Describe our Implement and Demo based on top 30% Requirements Analysis


# Index
- [1. Basic](#1-basic)
- [2. Payment](#2-payment)
- [3. Recommendation](#3-recommendation)


# 1. Basic

## requirements

![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/requirement/version.png)

## Setting

회원가입을 하고 로그인을 하면 책 리스트를 볼 수 있다. 검색창에 검색을 하면 그 키워드를 받고 filter을 적용해서 book data에서 해당 키워드가 있는 책을 전부 불러온다. 



## Database
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/data/bookdata.png)

subgroup 3 에서 사용한 book 의 데이터를 사용하였다. 

## DEMO

![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/main.png)

main 화면



#### 1) 고객의 경우
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/signup1.png)
계정이 없으면 sign up 을 한다.
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/signup2.png)
각 항목이 모두 채워지지 않으면 계정이 만들어지지 않는다.
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/booklist.png)
로그인을 하면 책 목록이 보인다. 
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/bookdetail1.png)
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/bookdetail2.png)
제목을 클릭하면 책 정보를 확인할 수 있다.

![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/search1.png)
책 검색을 하면 키워드에 맞는 책 리스트가 나온다.

![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/addtocartbutton.png)
우측 하단에 있는 add to cart 버튼을 누르면 '장바구니에 담겼습니다.' 확인창이 뜬다. 


#### 2) admin의 경우
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/admin1.png)
메인 화면에서 우측 하단 버튼을 누르면 다음 화면이 뜬다.
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/admin2.png)
어드민 계정으로 로그인 한 화면.
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/admin3-1.png)
book 정보 관리 가능
![image](https://github.com/idealization/software-engineering/blob/main/Implement/1.Basic_System/%EC%82%AC%EC%A7%84/demo/admin3-2.png)
계정들 확인 가능














# 2. Payment

### requirements

(환경 세팅: 개발 시 설치했던 django 등 라이브러리 버전, pip list 해서 걍 복붙해주세용)

### setting

(여기엔 회원가입 해야된다거나.. 뭐를 어떻게 맞춰줘야 된다거나.. 등등 주의할 점 써주면 될 듯!!)

## Database

(사진)

(설명)

## ~~ page, 과정별로

(사진)

(설명, 중간중간 디비 변화 등 같이 첨부)

## ~~ page

(사진)

(설명)

# 3. Recommendation

### requirements

Django                   3.2.3
Pillow                   8.2.0
Werkzeug                 1.0.1

### setting

models.py 파일에서 database를 수정할 시 해당 app의 상위 폴더(manage.py가 있는 폴더)에서
-> python manage.py makemigrations 
-> python manage.py migrate 
명령어를 수행하고,

CSS 등 static 폴더 안의 파일을 수정할 시
-> python manage.py collectstatic
명령어를 수행한 뒤, 

-> python manage.py runserver
명령어로 로컬 서버를 활성화한다.

장바구니와 결제 서비스를 이용하기 위해서는 고객 고유의 계정이 있어야 하므로 처음 실행 시 sign up, login 기능을 필수적으로 이행해야 한다.

## Database

(사진)

(설명)

## ~~ page, 과정별로

(사진)

(설명, 중간중간 디비 변화 등 같이 첨부)

## ~~ page

(사진)

(설명)

