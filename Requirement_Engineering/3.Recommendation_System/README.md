# ๐ต๏ธโโ๏ธ Recommendation System Part

## Member : ์ข๋ฏผ์ฃผ๐ฉโ๐ฌ, ์ด๋ณด๋ฆผ๐ฉโ๐ฌ


<br>

## 4์ 6์ผ ๋์ ์ถ์ฒ ์์คํ ๊ฐ๋ฐํ ํ์๐

## requirement ๋๋๊ธฐ => ์ถ์ฒ ์นดํ๊ณ ๋ฆฌ๋ณ
### 1. content filtering
### 2. collaborative filtering
### 3. association rule mining
### => ๋ฉ์ธ ํ์ด์ง์ ์ถ์ฒ ์นดํ๊ณ ๋ฆฌ๋ณ ์ถ์ฒ ๋์ ๊ทธ๋ฃน๋ณ ํ์

<br>

## Cause๐ค

<br>

## โ Problem detected ์ํ๋ ์ฑ์ ์ฐพ๊ธฐ ์ด๋ ต๋ค.
## Analysis of the causes
### * ์ฑ์ด ๋๋ฌด ๋ง๋ค.
### * ์ฑ์ ์นดํ๊ณ ๋ฆฌ๊ฐ ๋๋ฌด ๋ง๋ค.
### * ์ฑ ๊ด๋ จ ๋ด์ฉ์ ํ๋์ฉ ์์๋ณด๊ธฐ ํ๋ค๋ค.
### * ๋ด ์ทจํฅ์ ์ฑ์ธ์ง ์๊ธฐ ์ด๋ ต๋ค.
### * ์ฑ์ ๊ณ ๋ฅผ ๋ ์๊ฐ์ด ์ค๋ ๊ฑธ๋ฆฐ๋ค.

<br>

## โ Problem detected ์ถ์ฒ๊ฒฐ๊ณผ์ ๋ํ ๋ถ๋ง์กฑ
## Analysis of the causes
### * ๋๋ฌด ์ผ๋ฐฉ์ ์ธ ์ถ์ฒ -> (์ด ์ฑ์ ๋ํ ์ถ์ฒ ๊ธ์ง...?)

<br>

<br>

## โ๊ณ ๊ฐ์๊ฒ ๋ฌผ์ ๊ฒ (business policy)
### * ์์์ ์ถ์ฒ ์นดํ๊ณ ๋ฆฌ ์ ํธ๋ ์กฐ์ฌ (1.2.3 ์ค ๋ฌด์์ ์ ํธ ํ๋ ์ง) -> UI
### * ์ถ์ฒ๋๊ฐ ๊ฐ์ ๊ฒฝ์ฐ (๋ฐํ๋๋, ๊ฐ๊ฒฉ์, ์ฑ ์ด๋ฆ์,...)
### * ์ ์์ ๋ชจ๋์๊ฒ ์ถ์ฒ ์์คํ์ ์ ๊ณตํ  ๊ฒ์ธ์ง ํ์์๊ฒ๋ง ์ ๊ณตํ  ๊ฒ์ธ์ง

<br>

## โจSolution constraints
### * ๊ณ ๊ฐ์ ํ์คํ ๋ฆฌ ๋ฐ์ดํฐ๋ฅผ ์ธ์ ๊น์ง ๊ฐ๊ณ  ์์ ๊ฒ์ธ๊ฐ(๊ณ ๊ฐ ์ ํ์ง <1. ๊ฒ์๊ธฐ๋ก ์ญ์ >, ๊ธฐ๋ณธ์ ์ผ๋ก 1,2๋ ์ ๋...?) -> ๊น์ด ์๋ผ
### * ์ถ์ฒ ์๋ฐ์ดํธ ์ฃผ๊ธฐ๊ฐ ์ด๋์ ๋ ๋์ด์ผ ํ๋ ๊ฐ (์๋ก๊ณ ์นจ ๋  ๋)
### * ์ฌ์ฉ์ ๋ฐ์ดํฐ๊ฐ ์ด๋์ ๋ ์์์ ๋, ์ถ์ฒ ์์คํ์ ๋๋ฆด ์ง
### * ์ฌ์ฉ์ ๋ฐ์ดํฐ๊ฐ ๊ทนํ ์ ์ ์ํฉ์ผ ๋  ์ด๋ป๊ฒ ํด๊ฒฐ(๋ฒ ์คํธ ์๋ฌ)


# Requirements (IEEE-830)
REQ-1(FR/5): The systmen should recommend books based on authorized user's history log: clicked, bought, wathed, searched book list. 

REQ-2(FR/1,2): The system shall show the recommended books to authorized user. When the books have same recommandation score, the aranges of the books are by name.

REQ-3(FR/4): The system shall show the recommandation page, which displays books to authorized user, after signing in and then user can view books using their mouse and select the books. 

REQ-4(NFR/2): The system shall maintain the user's history log of all attempted accesses for recommandation.

REQ-5(FR/3,4): The system shall update the displaying recommanded books every second, when the page is refreshed. 

REQ-6(FR/2,3): The system should display books based on Newest book, MD recommandation book, and books viewed by users of the same age and gender to authorized user when the user's history is lack.

REQ-7(FR/2,3): The system should display books based on Newest book, MD recommandation book, and best seller books to authorized user when the system's history(all user's history) is lack.

# UI result ( UI process is on the pdf file)

![Uploading image.pngโฆ]()
