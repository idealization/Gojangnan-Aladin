# Checkpoint 3: Implement and Demo
## Gojangnan Aladin: Online book recommendation system using Collaborative filtering

Describe our Implement and Demo based on top 30% Requirements Analysis


# Index
- [1. Basic](#1-basic)
- [2. Payment](#2-payment)
- [3. Recommendation](#3-recommendation)


# 1. Basic

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

