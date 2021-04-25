# gojangnan aladin

# Problem Statement

## Business Goal

1. 웹사이트를 통한 온라인 도서 구매 시스템을 원한다.
2. 선택지를 줄일 수 있게 도서를 추천해준다.
3. 빠르고 편한 결제 시스템이 있어야 한다.
4. 관리자가 운영을 전반적으로 관리할 수 있어야 한다.

## The Problem

 우선적으로 각 회원들마다 맞춤형으로 도서가 추천되어야 합니다. 로그인을 하면 첫 화면서 추천도서가 뜨고, 비슷한 사용자가 구매한 책이 뜨는 겁니다. 각 도서 이미지나 제목을 클릭하면 책을 구매할 수 있어야 합니다. 또한 검색을 통해 책을 찾고 구매할 수도 있어야합니다. 검색을 하면 도서 리스트가 보이고 원하는 도서를 클릭하면 도서 정보페이지로 들어가 도서의 정보를 보고 구매할 수 있어야 합니다.    
 즉시 구매할 수도 있고 장바구니를 통해 원하는 여러 책을 장바구니에 담아 놓고, 장바구니에 있는 책을 한번에 구매할 수 있길 원합니다. 장바구니에 담아둔 책을 장바구니에서 삭제하거나 장바구니에 있는 책 중 일부만 주문할 수 있기도 해야 합나다. 결제 시스템도 있어야 합니다. 받은 책에 대해서 일정 기간내에는 반품을 할 수 있도록 반품하기 버튼도 있었으면 합니다.
 각 회원은 자기 정보를 볼 수 있어야 합니다. 기본적인 회원 정보에 회원 등급이 있었으면 합니다. 회원등급은 Blue, Silver, Gold, Diamond로 뒤로 갈 수록 높은 등급입니다. 기본적인 회원 정보는 이름, 아이디, 비밀번호, 주소, 전화번호 등 배달 시 필요한 정보들입니다.
 
 관리자는 도서, 회원, 배송 관리를 할 수 있어야 합니다. 사이트에 도서를 추가하고 삭제하고 도서의 상태를 변경할 수 있어야 합니다. 회원들이 어떤 책을 구매했는지 볼 수 있고, 회원들의 등급에 따라 혜택을 부여할 수 있도록 회원 관리 기능이 있었으면 합니다. 주문된 책을 배송해야 하니 현재 진행해야하는 주문, 진행되고 있는 주문, 완료된 주문으로 구분해서 주문을 볼 수 있어야 합니다. 각 책 별 총 매출액과 가장 잘 팔린 책 등을 기간을 설정해 볼 수 있었으면 합니다. 특정 기간의 총 매출액도 볼 수 있으면 좋겠습니다.

## Scenarios

### User scenario

책 주문을하기 위해 컴퓨터 혹은 핸드폰에서 인터넷을 켜 도서 구매 사이트로 이동합니다. 사용자는 사이트의 홈화면에서 로그인 버튼을 눌러 로그인 페이지로 이동합니다. 회원 로그인하기와 관리자 로그인하기 중 회원 로그인하기를 선택해 로그인합니다.

회원가입을 한다면 로그인 버튼을 눌러 로그인 페이지에 있는 회원가입 버튼을 통해 회원가입합니다. 회원가입은 아이디, 비밀번호, 이름, 나이, 성별, 주소, 비밀번호를 모두 입력합니다. 이후 인증이 완료된 후 가입하기 버튼을 클릭해 하면 회원가입이 완료됩니다. 로그인 후 홈 화면에서 '...님을 위한 추천 도서'를 볼 수 있습니다. 추천 도서란에 있는 도서를 클릭하면 도서 정보페이지로 이동합니다.

검색엔진을 통해 원하는 도서의 이름을 입력하면 정확도 순의 도서 목록을 볼 수 있습니다. 도서 목록은 도서 이미지, 책 제목, 저자 이름 등으로 이루어져 있습니다. 스크롤을 내리고 페이지를 넘기며 원하는 도서를 찾고 해당 도서를 찾았다면 책 이미지 혹은 책 제목을 클릭하여 도서 정보 페이지로 이동합니다.

선택된 도서의 세부 정보와 미리보기를 볼 수 있습니다. 세부 정보는 제목, 저자, ISBN, 가격, 목차, 줄거리, 출판사 등등 입니다. 또한 도서 리뷰란에서 다른 사용자들이 작성한 리뷰를 볼 수 있고, 새로운 리뷰를 작성할 수도 있습니다.

도서 정보 페이지에 있는 '즉시 구매'를 클릭하면 도서 구매 페이지로 이동합니다. '즉시 구매'가 아닌 '장바구니' 클릭 시, 도서가 장바구니에 담깁니다. 장바구니 페이지는 '장바구니 보기' 버튼을 통해 볼 수 있습니다. 장바구니 페이지로 이동하면 여태까지 장바구니 담아둔 책 리스트를 볼 수 있습니다. 구매를 원치 않게 된 도서를 장바구니 페이지에서 제거하고, 장바구니에 담긴 책 중 구매를 원하는 도서만 선택합니다. 이후 '구매하기' 버튼을 클릭하면 선택된 도서만 구매할 수 있는 구매 페이지로 이동합니다.

구매페이지에서 구매할 책 목록, 금액을 볼 수 있습니다. 구매인, 구매인 전화번호, 배송지를 입력합니다. 포인트 사용을 선택하면 최종 금액을 볼 수 있습니다. 최종 금액과 회원 등급에 따라 적립될 예상 포인트를 볼 수 있습니다. '결제하기' 버튼을 통해 결제 시스템으로 이어지며, 결제 시스템을 통해 책을 구매하게 됩니다. 구매한 책은 장바구니에서 자동 삭제 됩니다.

'내 정보' 버튼에서 회원의 정보와 구매한 책, 배송 정보 등을 볼 수 있습니다. 회원 정보란에서는 회원 가입시 입력한 정보와 회원 등급을 볼 수 있습니다. 회원 가입 시 입력한 정보는 수정할 수 있으며 비밀번호를 변경할 수도 있습니다. 구매 목록란에서는 여태까지 구매했던 모든 도서 리스트를 볼 수 있습니다. 배송 정보란에서는 구매 정보와 배송 상태를 알 수 있습니다. 배송 준비 중이면 '배송 준비 중', 배송 중이라면 '배송 중', 배송 완료되었다면 '배송 완료'로 그 상태를 알 수 있습니다.

### Admin scenario

인터넷을 켜 도서 구매 사이트로 이동합니다. 사이트의 홈 화면에서 로그인 버튼을 누릅니다. 로그인 페이지로 이동하여 회원 로그인과 관리자 로그인 중 관리자 로그인을 선택합니다. 관리자로 로그인을 하면 사이트 관리 페이지로 이동합니다.
사이트 관리 페이지에서는 도서 관리, 거래 관리, 회원 관리를 할 수 있습니다.

도서 관리 페이지에서는 사이트에 새롭게 도서를 등록하거나 등록된 도서를 삭제할 수 있습니다. 또한 등록된 도서들의 상태를 알 수 있습니다. 총 판매 권수, 환불된 책 권수, 책이 팔린 기록, 품절 혹은 절판 상태 등등을 볼 수 있습니다. 기간 별로 각 도서의 상태를 볼 수도 있으며 판매 권 수 등으로 도서 리스트를 재정렬 가능합니다. 수 많은 도서가 등록되어 있으므로 검색기능을 통해 도서를 검색할 수도 있습니다. 각 도서 상태를 변경할 수도 있습니다.

거래 관리 페이지에서는 모든 거래 기록과 모든 배송 정보를 볼 수 있습니다. 거래 기록에서는 현재까지의 총 판매액, 기간별 판매액 등을 볼 수 있습니다. 배송 정보는 세부적으로 배송 완료, 배송 중, 배송 준비 중으로 나눠지며 앞의 상태에 따라 배송 정보를 선별하여 볼 수도 있습니다. 어떤 회원이 언제 어떤 책들을 주문했으며 배송 상태가 어떠한지 볼 수 있습니다.

회원 관리 페이지에서는 모든 회원의 정보를 볼 수 있습니다. 각 회원의 등급부터 회원 이름, 아이디, 회원 등급, 구매한 책 목록, 현재 주문 진행 여부, 회원이 남긴 comment 등을 모두 볼 수 있습니다. 회원 등급은 기본적으로 시스템에 의해 자동으로 관리됩니다. 관리자가 조정 가능한 부분은 회원 삭제, 회원 등급, 회원 포인트 조정입니다.

# Form Sub-Groups

Divide work to #3 sub groups based on business goal 
1) 선택지를 줄일 수 있게 도서를 추천해준다 : 보림, 민주
2) 빠르고 편한 결제 시스템이 있어야 한다 : 상화, 희민
3) 서점 기본 시스템 ( 로그인 / 회원가입 / 검색 기능 / 관리자 운영 )  : 다인, 태림

# Software Development Method

## Waterfall Method

# Gathered Requirements

## IEEE-830

### Sub Group 1: Basic System

### Sub Group 2: Payment System
![SubGroup2_IEEE-830](./Requirement_Engineering/2.Payment_System/image/IEEE-830_after_CustomerChallenge.png)

### Sub Group 3: Recommendation System
![image](https://user-images.githubusercontent.com/55435898/115983492-51481a00-a5dc-11eb-81bb-c7554d5c5728.png)

# System Model

## Use Case model

### Sub Group 1: Basic System

#### Use Case Diagram

#### Use Case Details

#### Traceability Matrix

### Sub Group 2: Payment System

![Use case type](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/Use%20case%20type.jpg)
![Use Cases_after_CustomerChallenge](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/Use%20Cases_after_CustomerChallenge.PNG)

#### Use Case Diagram

1. Payment Subsystem

![UC Diagram1-1](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/UC%20Diagram1-1.png)

2. Cart page Subsystem

![UC Diagram2-1](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/UC%20Diagram2-1.png)

3. Purchase history page Subsystem

![UC Diagram3-1](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/UC%20Diagram3-1.png)

#### Use Case Details
![UC-1](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/UC-1.png)
![UC-2](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/UC-2.png)
![UC-3](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/UC-3.png)
![UC-4_after_CustomerChallenge](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/UC-4_after_CustomerChallenge.jpg)
![UC-5_after_CustomerChallenge](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/UC-5_after_CustomerChallenge.jpg)
![UC-6_after_CustomerChallenge](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/UC-6_after_CustomerChallenge.jpg)

#### Traceability Matrix
![Traceability_Matrix](https://github.com/idealization/software-engineering/blob/main/Use_Cases/2.Payment_System/image/Traceability_Matrix.png)

### Sub Group 3: Recommendation System
![image](https://user-images.githubusercontent.com/55435898/115983553-d3384300-a5dc-11eb-85e1-857de1c692ab.png)

#### Use Case Diagram

![image](https://user-images.githubusercontent.com/55435898/115983172-99663d00-a5da-11eb-9616-6d48a2fa3aa3.png)

#### Use Case Details
* UC - 1 <br>
![image](https://user-images.githubusercontent.com/49024958/115984086-2a8be280-a5e0-11eb-893a-324035f74736.png)

* UC - 2 <br>
![image](https://user-images.githubusercontent.com/49024958/115984092-3e374900-a5e0-11eb-836e-2772d75a33d4.png)

* UC-3 <br>
![image](https://user-images.githubusercontent.com/55435898/115983454-1d6cf480-a5dc-11eb-9225-9a445e620a8b.png)

* UC-4 <br>
![image](https://user-images.githubusercontent.com/55435898/115983465-26f65c80-a5dc-11eb-8a4d-f67ada2d1e22.png)

#### Traceability Matrix
![image](https://user-images.githubusercontent.com/55435898/115983569-ed722100-a5dc-11eb-8d07-a7e6802bb1a5.png)

## Domain model

### Sub Group 1: Basic System

#### Domain model for UC-?:

- Extracting the Responsibilities

- Extracting the Associations

- Extracting the Attributes

#### Diagram

#### Domain model for UC-?:

- Extracting the Responsibilities

- Extracting the Associations

- Extracting the Attributes

#### Diagram

#### Traceability Matrix

### Sub Group 2: Payment System

#### Domain model for UC-1: Prepare Payment

- Extracting the Responsibilities
![Domain1-1](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain1.png)
- Extracting the Associations
![Domain1-2](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain2.png)
- Extracting the Attributes
![Domain1-3](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain3.png)

#### Diagram
![Diagram1](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Diagram1.jpg)

#### Domain model for UC-2: Payment Process

- Extracting the Responsibilities
![Domain2-1](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain4.png)
- Extracting the Associations
![Domain2-2](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain5.png)
- Extracting the Attributes
![Domain2-3](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain6.png)

#### Diagram
![Diagram2](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Diagram2.jpg)

#### Domain model for UC-3: Cart

- Extracting the Responsibilities
![Domain3-1](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain7.png)
- Extracting the Associations
![Domain3-2](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain8.png)
- Extracting the Attributes
![Domain3-3](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain9.png)

#### Diagram
![Diagram3](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Diagram3.jpg)

#### Domain model for UC-4: Manage Purchase history and state

- Extracting the Responsibilities
![Domain4-1](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain10.png)
- Extracting the Associations
![Domain4-2](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain11.png)
- Extracting the Attributes
![Domain4-3](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain12.png)

#### Diagram
![Diagram4](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Diagram4.png)

#### Domain model for UC-5: Manage Point

- Extracting the Responsibilities
![Domain5-1](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain13.png)
- Extracting the Associations
![Domain5-2](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain14.png)
- Extracting the Attributes
![Domain5-3](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain15.png)

#### Diagram
![Diagram5](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Diagram5.png)

#### Domain model for UC-6: Confirm Expenditure

- Extracting the Responsibilities
![Domain6-1](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain16.png)
- Extracting the Associations
![Domain6-2](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain17.png)
- Extracting the Attributes
![Domain6-3](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Domain18.png)

#### Diagram
![Diagram6](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Diagram6.png)

#### Traceability Matrix
![Traceability_Matrix_Domain](https://github.com/idealization/software-engineering/blob/main/Domain_Model/2.Payment_System/img/Traceability_Matrix.png)

### Sub Group 3: Recommendation System

#### Domain model for UC-1:

- Extracting the Responsibilities
![image](https://user-images.githubusercontent.com/49024958/115983405-d848c280-a5db-11eb-8d0a-2f50f18a8323.png)
- Extracting the Associations
![image](https://user-images.githubusercontent.com/49024958/115983376-af283200-a5db-11eb-910d-8dd6b0cde184.png)
- Extracting the Attributes
![image](https://user-images.githubusercontent.com/49024958/115983325-70927780-a5db-11eb-8770-58b865f3c16b.png)
#### Diagram
![image](https://user-images.githubusercontent.com/49024958/115955398-25bc2580-a531-11eb-8864-eb16e7bf0a44.jpg)
#### Domain model for UC-2:

- Extracting the Responsibilities
![image](https://user-images.githubusercontent.com/49024958/115983561-dc291480-a5dc-11eb-887b-45de2b56efcc.png)
- Extracting the Associations
![image](https://user-images.githubusercontent.com/49024958/115983513-78065080-a5dc-11eb-8010-5c17ddf2957c.png)
- Extracting the Attributes
![image](https://user-images.githubusercontent.com/49024958/115983292-4a6cd780-a5db-11eb-8b60-440af8d01c9d.png)
#### Diagram
![image](https://user-images.githubusercontent.com/49024958/115955402-29e84300-a531-11eb-9bd7-660979924b27.jpg)

#### Domain model for UC-3:

- Extracting the Responsibilities
![image](https://user-images.githubusercontent.com/55435898/115983305-5eb0d480-a5db-11eb-86f1-010ef907545e.png)

- Extracting the Associations
![image](https://user-images.githubusercontent.com/55435898/115983322-6e301d80-a5db-11eb-9150-6f48431a2c8f.png)

- Extracting the Attributes
![image](https://user-images.githubusercontent.com/55435898/115983340-8142ed80-a5db-11eb-85fc-5f293ca5a222.png)

#### Diagram
![image](https://user-images.githubusercontent.com/55435898/115983350-915acd00-a5db-11eb-87ec-939b2a7d1cd6.png)

#### Domain model for UC-4:

- Extracting the Responsibilities
![image](https://user-images.githubusercontent.com/55435898/115983703-bf411100-a5dd-11eb-8afd-d7e26584e301.png)

- Extracting the Associations
![image](https://user-images.githubusercontent.com/55435898/115983389-bc452100-a5db-11eb-928d-88dc42959c13.png)

- Extracting the Attributes
![image](https://user-images.githubusercontent.com/55435898/115983394-c404c580-a5db-11eb-92a6-55d41e758e15.png)

#### Diagram
![image](https://user-images.githubusercontent.com/55435898/115983401-cf57f100-a5db-11eb-8860-b625fd566356.png)

#### Traceability Matrix
![image](https://user-images.githubusercontent.com/49024958/115956235-a7628200-a536-11eb-8778-9e5374fa88bd.png)
## User Interface mockups

### Sub Group 1: Basic System

### Sub Group 2: Payment System

**1. 장바구니 페이지**

![장바구니 페이지](https://github.com/idealization/software-engineering/blob/main/Requirement_Engineering/2.Payment_System/image/%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%20%ED%8E%98%EC%9D%B4%EC%A7%80.PNG)

**2. 주문 과정**

![주문과정1](https://github.com/idealization/software-engineering/blob/main/Requirement_Engineering/2.Payment_System/image/%EC%A3%BC%EB%AC%B8%EA%B3%BC%EC%A0%951.PNG)

![주문과정2](https://github.com/idealization/software-engineering/blob/main/Requirement_Engineering/2.Payment_System/image/%EC%A3%BC%EB%AC%B8%EA%B3%BC%EC%A0%952.PNG)

**3. 결제 성공 / 실패 페이지**

- 결제 성공

![결제 성공 페이지](https://github.com/idealization/software-engineering/blob/main/Requirement_Engineering/2.Payment_System/image/%EA%B2%B0%EC%A0%9C%20%EC%84%B1%EA%B3%B5%20%ED%8E%98%EC%9D%B4%EC%A7%80.png)

- 결제 실패

![결제 실패 페이지](https://github.com/idealization/software-engineering/blob/main/Requirement_Engineering/2.Payment_System/image/%EA%B2%B0%EC%A0%9C%20%EC%8B%A4%ED%8C%A8%20%ED%8E%98%EC%9D%B4%EC%A7%80.png)

**4. 주문 및 배송 조회 페이지**

![주문 및 배송 조회 페이지](https://github.com/idealization/software-engineering/blob/main/Requirement_Engineering/2.Payment_System/image/%EC%A3%BC%EB%AC%B8%20%EB%B0%8F%20%EB%B0%B0%EC%86%A1%20%EC%A1%B0%ED%9A%8C%20%ED%8E%98%EC%9D%B4%EC%A7%80_After_CustomerChallenge.PNG)

**5. 결제 취소 팝업창**

![결제 취소 팝업창](https://github.com/idealization/software-engineering/blob/main/Requirement_Engineering/2.Payment_System/image/%EA%B2%B0%EC%A0%9C%20%EC%B7%A8%EC%86%8C%20%ED%8C%9D%EC%97%85%EC%B0%BD.png)

### Sub Group 3: Recommendation System
