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

Django                   3.2.3
Pillow                   8.2.0

### setting

(여기엔 회원가입 해야된다거나.. 뭐를 어떻게 맞춰줘야 된다거나.. 등등 주의할 점 써주면 될 듯!!)

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

# 3. Recommendation

## 30% Requirement

1. (REQ-1) The system should recommend books based on authorized customer's history log.(collaborative recommendation 알고리즘만 구현)
2. (REQ-3) The system shall show the recommendation page, which displays books to  customer and then user can view books.
3. (REQ-5) The system shall maintain the customer's history log of all attempted accesses for recommendation.
4. (REQ-6) The system shall update the displaying recommended books every second, when the page is redirected.

**How to run**

- First input secrets.json(written django "SECRET_KEY" : "~")
- In terminal, execute 1) python [manage.py](http://manage.py)  makemigrates

    2) python [manage.py](http://manage.py)  migrate

    3) python [manage.py](http://manage.py)  runserver

To implement 30% of requirements, we mainly coded on the recommendation for recommend1(out of 3recommendation tab, the first one) tab and main page htmls. 

## Demo

Main page for customerID: 3001 

- The recommend 1 tab is the result of collaborative filtering by Matrix Factorization theorem. After the customer logged in, he can see the main page below. (Assumed that the customer has already visited our website).
- The "Gojangnan Aladin" recommends the book lists for him based on customers book-lookup table(Log DB). When the customer click a book, the Logger colects the book he clicked.

![bandicam_2021-05-31_23-20-38-878](https://user-images.githubusercontent.com/49024958/120211566-0751f400-c26c-11eb-88fe-4fa05d0e04d2.jpg)

When pressing the right arrow button:

- Customer can view more books lists when click the left/right arrows.

![bandicam_2021-05-31_23-20-42-375](https://user-images.githubusercontent.com/49024958/120211555-04570380-c26c-11eb-8cb7-82ec5ae8791f.jpg)
Click the arrow button again.

![bandicam_2021-05-31_23-21-51-588](https://user-images.githubusercontent.com/49024958/120211549-028d4000-c26c-11eb-84ac-321aa8b8e42c.jpg)

When pressing the refresh button

- The recommended book list has changed.

![bandicam_2021-05-31_23-22-08-305](https://user-images.githubusercontent.com/49024958/120211522-fc975f00-c26b-11eb-878c-600170571334.jpg)

The recommend result is personalized to users. When another user logged in, and the userID 

Main page for customerID: 617

![main_page_for_user_617](https://user-images.githubusercontent.com/49024958/120211508-fa350500-c26b-11eb-86b2-722543d99cfe.jpg)

Until now, this is subgroup3's demo for 30% requirements. 

---

## Page Redirection with subgroup1


Now, here is the redirect structure with subgroup 1. 

1. When the customer click a book image, the page is redirected to subgroup1's detail book page.

![bandicam_2021-05-31_23-48-06-537](https://user-images.githubusercontent.com/49024958/120211487-f43f2400-c26b-11eb-896f-0d548c06f200.jpg)

![bandicam_2021-05-31_23-45-03-126](https://user-images.githubusercontent.com/49024958/120211476-f1443380-c26b-11eb-85d2-6ed741b0d78c.jpg)

2. When the customer click a "search 검색" button, the page is redirected to subgroup1's page.

![bandicam_2021-05-31_23-49-07-515](https://user-images.githubusercontent.com/49024958/120211470-eee1d980-c26b-11eb-9f6f-5940ca859d2b.jpg)

![bandicam_2021-05-31_23-48-53-446](https://user-images.githubusercontent.com/49024958/120211462-ebe6e900-c26b-11eb-97a0-962170eff815.jpg)
---

## Database Structure (mysqlite)

![bandicam_2021-05-31_23-52-45-943](https://user-images.githubusercontent.com/49024958/120211418-e2f61780-c26b-11eb-9111-80f9bce0bdf4.jpg)

1. Book DB scheme

![bandicam_2021-05-31_23-54-41-919](https://user-images.githubusercontent.com/49024958/120211397-dd98cd00-c26b-11eb-926a-3b3e75a87c68.jpg)

2. Log DB scheme

![bandicam_2021-05-31_23-54-27-827](https://user-images.githubusercontent.com/49024958/120211383-da9ddc80-c26b-11eb-9ab0-ca2c90301f5d.jpg)


