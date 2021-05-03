# Use cases

# USE CASES

-use case model

| Actor |	Actor'sGoal |	Use Case Name |
|:---|:---:|---:|
Log Collector	| To collect user's history log		| UC-1: History|
Recommender		| To recommend books	| 	UC-2: Recommend |
Recommender		| To recommend Books viewed by users of the same age and gender, Newest book and MD recommandation book on book board (Situations where the algorithm cannot be used)		| UC-1, UC-2 |
Recommender	| 	To recommend Best seller books, Newest book and MD recommandation book on book board		| UC-2 |
Recommender		| To arrange the recommended book list when they have same recommend degree		| UC-2	| 
Customer		| To display recommended book		| UC-3: Display |
Customer 		| To browse books to buy on book board //surf around the displayed books  	| 	UC-4: Browser	| 
Customer 		| To click book image to get detailed information about the book 		| UC-4	| 
Customer 		| To press arrow buttons and get more books to see		| UC-3	| 
Customer 		| To press refresh buttons and get new recommended book list		| UC-3	| 

# Traceability Matrix


-Traceability Matrix

|Req't	|PW	|UC1	|UC2	|UC3	|UC4| (Basic System)UC1 |
|:---|:---:|:---:|:---:|:---:|:---:|---:|
REQ1	|5|	X|	X|	|	|X|
REQ2	|1|	|	X|	X|	| |
REQ3	|4|X|	|	X|	|X|
REQ4	|2|	X| |	|	X|X|
REQ5	|4|	X|	X|	X|	|X|
REQ6	|3|	X	|X| |	|X|
REQ7	|3|	X|	X|	|	|X|
Max 	|PW| 5	|5	|4|	2|5|
Total |	PW|	21|	16|	9|	2|21|


# UseCaseDiagram

![image](https://user-images.githubusercontent.com/49024958/115996040-b457a200-a618-11eb-913e-72c51f5fe9a8.png)

