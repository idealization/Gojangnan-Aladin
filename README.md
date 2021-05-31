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

models.py 파일에서 database를 수정할 시 해당 app의 상위 폴더(manage.py가 있는 폴더)에서

-> python manage.py makemigrations 

-> python manage.py migrate 
명령어를 수행하고, (migrate는 첫 실행 시마다 수행)

CSS 등 static 폴더 안의 파일을 수정할 시

-> python manage.py collectstatic
명령어를 수행한 뒤, 

-> python manage.py runserver
명령어로 로컬 서버를 활성화한다.

장바구니와 결제 서비스를 이용하기 위해서는 고객 고유의 계정이 있어야 하므로 처음 실행 시 sign up, login 기능을 필수적으로 해야 한다.


## Demo

![login](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(2).png)

cart page와 payment page에 접근하기 위해 고객이 식별돼야 하므로 login을 먼저 한다. 사용자 계정이 없다면 sign up을 눌러 회원가입을 할 수 있다. subgroup2의 역할은 아니지만, demo를 위해 간단히 구현하였다.

![main](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(3).png)

login을 하면 보이는 메인 화면이다. 이 화면 역시 subgroup2의 역할은 아니지만, demo를 위해 간단히 구현하였다. user는 'sangh'으로 테스트하였다.

![main2](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(4).png)

![main3](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(5).png)

![main4](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(6).png)

메인 화면에는 위와 같이 도서 목록이 나온다. 일부 도서의 표지 사진, 제목, 가격만 볼 수 있게 구현해 놓았다.

![main_toggle](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(7).png)

![business](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(8).png)

메인 화면에서 도서의 카테고리를 설정하면 해당 카테고리에 속한 도서 목록을 볼 수 있으며, business & investing 카테고리를 클릭한 모습이다. 또한, 장바구니 버튼과 검색 버튼이 있다. subgroup2의 역할에 따라 장바구니 페이지를 구현하였고, 장바구니 버튼을 눌러 접속할 수 있다.

![out_of_stock](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(9).png)

도서 목록에서 한 도서를 클릭하면, 위와 같이 detail 화면이 뜬다. 이 또한 subgroup2의 역할은 아니지만, demo에서 재고가 있어야 구매를 할 수 있고 구매를 하면 재고가 줄어들어야 하는 상황을 나타내기 위해 간단히 구현하였다. 이 사진은 현재 도서 database에서 해당 도서의 재고가 없기 때문에 구매할 수 없는 상황이다.

![detail](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(10).png)

도서 database에 해당 도서의 재고가 있다면 add to cart 버튼을 확인할 수 있다. 이 버튼을 누르면 장바구니에 상품이 담긴다.

![cart](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(11).png)

위의 상품을 장바구니에 담고 난 후의 cart page 화면이다. 현재 'The Art Book'을 1권 담은 상태이고, 위 main page에서 확인할 수 있었던 장바구니 아이콘 옆에는 1이 표시되었다. 이때 책 옆에 표시되는 추가, 삭제 버튼을 통해 구매 수량을 조절하거나 해당 상품을 장바구니에서 제거할 수 있다.

![cart2](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(12).png)

위의 상황에서 'Batman: Three Jockers' 책을 추가한 화면이다. 따라서 SKU가 9인 책이 1권, SKU가 2인 책이 3권 들어있다. 이 책을 3권 구매하는 것으로 수량을 조절하면, 위의 장바구니 아이콘 옆에는 4가 표시되고 더이상 재고가 없기 때문에 추가 버튼이 없어진다. 이 상황을 DB와 비교하며 살펴보면 다음과 같다.

![user](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(13).png)

이 때의 auth_user DB이다. 현재 테스트하고 있는 'sangh'이 있고, 'sangh'의 고유 번호(id)는 8임을 확인할 수 있다.

![cart](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(14).png)

모든 유저의 cart DB이다. user와 cart 고유 id가 저장된다. user_id가 8인 유저의 cart 고유 번호(id)는 22임을 확인할 수 있다.

![cart_item](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(15).png)

cart에 들어있는 상품을 나타내는 cartItem DB이다. cart_id가 22인 행을 보면, product_id가 9인 책이 1권, product_id가 2인 책이 3권 들어있음을 확인할 수 있다. 이는 위의 cart page에서 확인했던 내용과 같다.

![prepare](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(16).png)

cart page에서 Prepare to Checkout 버튼을 누르면 구매하기 위해 필요한 배송 정보를 입력할 수 있다. 

![prepare2](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(17).png)

Name, Phone, Address를 형식에 맞게 입력해야 한다.

![buy](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(18).png)

배송 정보를 입력하고 나면, Buy 버튼을 눌러 결제 과정을 시작할 수 있다. 고객이 입력한 배송 정보가 간단하게 나타나고, PG사의 결제 페이지가 나타난다. 그러나 이번 구현에서는 우리의 가맹점 번호가 없어서 PG사의 결제 서비스를 연결하지 못했다.

![cart2](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(19).png)

결제하고 난 후의 cart DB 모습이다. 위에서 첨부한 cart DB 화면과 비교해 보면, 결제한 상품이 cart에서 제외되었음을 확인할 수 있다.

![cart_item2](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(20).png)

cartItem DB 또한 결제한 상품이 삭제되었다.

![pay](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(21).png)

구매 내역을 나타내는 DB이다. user_id가 8인 'sangh'의 구매 내역이 추가되었고, 이 구매 내역 id는 2로 설정되었다.

![order](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(22).png)

주문한 책의 정보를 나타내는 DB이다. product_id가 9인 책이 1권, product_id가 2인 책이 3권 주문된 내역이 추가되었다. 또한, 이 주문 내역의 id는 2라고 알맞게 표시된다.

![orderinfo](https://github.com/idealization/software-engineering/blob/main/Implement/2.Payment_System/Screenshots/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(23).png)

주문한 고객의 정보를 나타내는 DB이다. order_id가 2인 주문 정보의 고객이 'sangh'로 설정되었음을 확인할 수 있다.

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


