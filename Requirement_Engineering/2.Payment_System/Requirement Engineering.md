# Requirement Engineering

## IEEE - 830


![IEEE-830_of_Subgroup2](https://github.com/idealization/software-engineering/blob/main/Requirement_Engineering/2.Payment_System/image/IEEE-830.png?raw=true)



## Business Policy

- Discussed

  | REQ  | Business Policy | Feedback |
  | :----- | :--------------- | :-------- |
  | REQ-4 | 포인트 사용 단위 | 1원 단위로 사용 가능 |
  | REQ-8 | 구매 확정 선택 가능 기간, 해당 기간이 지난 후 처리 방식 | 구매확정 기간은 배송이 완료된 직후부터 1주일. 1주일 이후에는 자동 구매 확정 |
  | REQ-9 | 구체적인 환불 정책 | 포인트 사용 금액에 대해선 포인트로 환불. 실제 결제 금액은 카드 내역 취소로 환불. 환불은 구매 확정 전까지 가능 |
  | REQ-10 | 교환 신청 가능 기간 | 환불 및 교환 가능 기간은 구매 확정 전까지임 |
  | REQ-15 | 간단 정보에 포함되는 사항 | 책 표지 이미지, 책 제목, 가격, 수량 |
  | REQ-23 | Delivery state 종류 | 배송 준비 중, 배송 중, 배송 완료 |
  | REQ-24 | 회원 등급별 포인트 적립 비율 | Blue : 1%, Silver - 2%, Gold - 3%, Diamond - 4% |
  | REQ-25 | 회원 등급 변경(등급 상승, 등급 유지, 등급 하락) 기준 | 1개월 기준, 매달 1일에 회원 등급 갱신. 기준 : Blue : 0원, Silver - 5만원, Gold - 10만원, Diamond - 20만원, 1개월 동안은 총 구매 금액 기준 |
  
  

- Undiscussed

  | REQ    | Business Policy                            |
  | :----- | :----------------------------------------- |
  | REQ-9  | 흠이 있는 물건이라고 어떻게 판단할 것인가? |
  | REQ-21 | Detail에 들어가야 할 사항                  |



## Discuss Need

1. 회원 등급 관리(조정) : 해당 부분은 Subgroup1이 해야 하는 일인 듯 하다. 논의가 필요하다.
2. 배송 상태 변경은 관리자가 직접 해야 하는 것인가? 아니면 다른 배송 관리 시스템이 정보를 주는 것인가?
