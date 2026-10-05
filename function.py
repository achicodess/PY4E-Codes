print("Function to count score each time answer is correct.")

def Score_Count():
 	answer_cache=["Beach"]
 	answer=input("Enter your answer: ")
 	score=0
 	if answer in answer_cache:
 		score=score+1
 		print("Score is",score)
 	else:
 		print("Error")

Score_Count()

