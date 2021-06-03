# README.md

## Result Of (Object) Sequence Diagram

### UC-1
![osd1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd2_va1.png?raw=true)

### UC-2
![osd2](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd2_va3.png?raw=true)

### UC-3
![osd3](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd3_va1.png?raw=true)

## How the result came out

### We selected top 30% of requirements engineering
![selected_req](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/selected_req.png?raw=true)
These reqs are related to use case 1, 2, 3.

### We make sequence diagram based on existing use case and domain model

#### UC-1
![brief_osd1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/brief_osd1.png?raw=true)

#### UC-2
![brief_osd2](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/brief_osd2.png?raw=true)

#### UC-3
![brief_osd3](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/brief_osd3.png?raw=true)

##### Problem
- 기존 use case와 domain model은 현재 구현하지 않을 내용들이 모두 섞여있어 이를 기반으로 자세한 설계를 하기 어려움
- 기존 use case와 domain model에 실제 system 설계의 내용이 구체적이지 않았으며 일부 요구를 삭제하며 추가해야 하는 부분이 생김

* Use case와 Domain model을 선정한 30% 요구들에 맞게 재작성하기로 결정함

### Then we defined use case 1, 2, 3 again according to top 30% of reqs.

#### Briefly
![uc](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/uc.png?raw=true)

#### Detailed

##### UC-1: Prepare Payment
![uc1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/uc1.png?raw=true)

##### UC-2: Payment Process
![uc2](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/uc2.png?raw=true)

##### UC-3: Cart
![uc3](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/uc3.png?raw=true)

#### Use Case Diagram

##### About Payment Subsystem
![uc_diagram1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/uc_diagram1.png?raw=true)

##### About Cart Subsystem
![uc_diagram2](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/uc_diagram2.png?raw=true)

### We drew domain model again.

#### Detail

##### UC-1: Prepare Payment
![dm_uc1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/dm_uc1.png?raw=true)

##### UC-2: Payment Process
![dm_uc2](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/dm_uc2.png?raw=true)

##### UC-3: Cart
![dm_uc3](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/dm_uc3.png?raw=true)

#### Diagram

![dm1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/dm_diagram1.png?raw=true)
![dm2](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/dm_diagram2.png?raw=true)

### We made sequence diagram based on this.

#### Detailed

##### UC-1
![detail_osd1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd1.png?raw=true)

##### UC-2
![detail_osd2](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd2.png?raw=true)

##### UC-3
![detail_osd1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd3.png?raw=true)

### We found some variations in our diagrams.

#### UC-1

##### #1
![osd1_va1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd1_va1.png?raw=true)

#### UC-2

##### #1
![osd2_va1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd2_va1.png?raw=true)

##### #2
![osd2_va2](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd2_va2.png?raw=true)

##### #3
![osd2_va3](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd2_va3.png?raw=true)

#### UC-3

##### #1
![osd3_va1](https://github.com/idealization/software-engineering/blob/main/OSD/2.Payment_System/image/osd3_va1.png?raw=true)

### Finally, we chose the final version out of these variations.
