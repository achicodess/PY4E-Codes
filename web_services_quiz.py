print("Welcome to the Web Services Quiz!")

que1="What are the key terms in XML??"
print("Question 1: ",que1)
answer1=input("Enter your answer (any 2): ").lower()
key_terms=["tags", "attributes","serialisation","deserialization"]
correct_macth=[term for term in key_terms if term in answer1]

if len(correct_macth) >= 2:
    print("Correct answer!!")
else:
    print("Oops that's wrong!")

que2="What is an XML Schema??"
print("Question 2: ",que2)
ans2="XML Schema is a contract that governs the type of information that is allowed to pass through the web.".lower()
answer2=input("Enter your answer: ") .lower()
if answer2==ans2:
	print("Correct answer!")
else:
	print("Oops that's the wrong answer!")

print("x--End of the quiz.--x")



