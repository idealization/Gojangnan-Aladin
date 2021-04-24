# Use cases

# USE CASES

-use case model

| Actor |	Actor'sGoal |	Use Case Name |
|:---|:---:|---:|
Log Collector	| To collect user's history log		| UC-1: History|
Recommender		| To recommend books	| 	UC-2: Recommend |
Recommender		| "To recommend Books viewed by users of the same age and gender, Newest book and MD recommandation book on book board"		| UC-1, UC-2 |
Recommender	| 	"To recommend Best seller books, Newest book and MD recommandation book on book board"		| UC-2 |
Recommender		| To arrange the recommended book list when they have same recommend degree		| UC-2	| 
Viewer		| To display recommended book		| UC-3: Display |
Customer 		| To find out book to buy on book board //surf around the displayed books  	| 	UC-4: Browser	| 
Customer 		| To click book image to get detailed information for the book 		| UC-4	| 
Customer 		| To press arrow buttons and get more books to see		| UC-3	| 
Customer 		| To press refresh buttons and get new recommended book list		| UC-3	| 

# Traceability Matrix

|:---|:---:|---:|
Traceability Matrix					|
Req't	|PW	|UC1	|UC2	|UC3	|UC4|
REQ1	|5|	X|	X|	|	|
REQ2	|1|	|	X|	X|	|
REQ3	|4|X|	|	X|	|
REQ4	|2|	X| |	|	|X|
REQ5	|4|	X|	X|	X|	|
REQ6	|3|	X	|X| |	|
REQ7	|3|	X|	X|	|	|
Max 	|PW| 5	|5	|4|	2|
Total |	PW|	21|	16|	9|	2|


# UseCaseDiagram

![UseCaseDiagram최종](https://user-images.githubusercontent.com/55435898/115821559-fb3d7000-a43d-11eb-87b3-70bb2d58c10b.PNG)

