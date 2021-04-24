# 🕵️‍♂️ Recommendation System Part

## Member : 좌민주👩‍🔬, 이보림👩‍🔬


<br>

## 4월 6일 도서 추천 시스템 개발팀 회의😊

## requirement 나누기 => 추천 카테고리별
### 1. content filtering
### 2. collaborative filtering
### 3. association rule mining
### => 메인 페이지에 추천 카테고리별 추천 도서 그룹별 표시

<br>

## Cause🤔

<br>

## ✔ Problem detected 원하는 책을 찾기 어렵다.
## Analysis of the causes
### * 책이 너무 많다.
### * 책의 카테고리가 너무 많다.
### * 책 관련 내용을 하나씩 알아보기 힙들다.
### * 내 취향의 책인지 알기 어렵다.
### * 책을 고를 때 시간이 오래 걸린다.

<br>

## ✔ Problem detected 추천결과에 대한 불만족
## Analysis of the causes
### * 너무 일방적인 추천 -> (이 책에 대한 추천 금지...?)

<br>

<br>

## ❔고객에게 물을 것 (business policy)
### * 위에서 추천 카테고리 선호도 조사 (1.2.3 중 무엇을 선호 하는 지) -> UI
### * 추천도가 같을 경우 (발행년도, 가격순, 책 이름순,...)
### * 접속자 모두에게 추천 시스템을 제공할 것인지 회원에게만 제공할 것인지

<br>

## ✨Solution constraints
### * 고객의 히스토리 데이터를 언제까지 갖고 있을 것인가(고객 선택지 <1. 검색기록 삭제>, 기본적으로 1,2년 정도...?) -> 깉이 의논
### * 추천 업데이트 주기가 어느정도 되어야 하는 가 (새로고침 될 때)
### * 사용자 데이터가 어느정도 쌓였을 때, 추천 시스템을 돌릴 지
### * 사용자 데이터가 극히 적은 상황일 때  어떻게 해결(베스트 셀러)


# Requirements (IEEE-830)
REQ-1(FR/5): The systmen should recommend books based on authorized user's history log: clicked, bought, wathed, searched book list. 

REQ-2(FR/1,2): The system shall show the recommended books to authorized user. When the books have same recommandation score, the aranges of the books are by name.

REQ-3(FR/4): The system shall show the recommandation page, which displays books to authorized user, after signing in and then user can view books using their mouse and select the books. 

REQ-4(NFR/2): The system shall maintain the user's history log of all attempted accesses for recommandation.

REQ-3(FR/3,4): The system shall update the displaying recommanded books every second, when the page is refreshed. 

REQ-6(FR/2,3): The system should display books based on Newest book, MD recommandation book, and books viewed by users of the same age and gender to authorized user when the user's history is lack.

REQ-7(FR/2,3): The system should display books based on Newest book, MD recommandation book, and best seller books to authorized user when the system's history(all user's history) is lack.

#


