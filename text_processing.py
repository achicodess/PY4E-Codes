print("This program is about text processing.")
print("The questions are 1.",q1 "2.",q2,"3.",q3,"4.",q4, "5.",q5, "6.",q6)
try:
	opt=int(input("Enter your desired question no.: "))
except opt>6 or ValueError:
	print("Invalid input.")

q1="What's ASCII abbrivated?"
ans1="American Standard Code for Information Interchange."
q2="What is the use of 'ord()' function?"
ans2="The ord() function tells us the numerical value of a simple ASCII charecter."
q3="What is Unicode?"
ans3="Unicode is another charecter set that is very complex and contains a large number of charecter sets for many different languages of the world and various type of charecters."
q4="Which encoding scheme is advised for encoding data exchanged between two systems?"
ans4="UTF-8"
q4="Why is UTF-8 preferred??"
ans4="Because it has dynamic length (From 1 to 4 bytes)"
q5="What does encode() do??"
ans5="encode() coverts data into UTF-8 or other desired type."
q6="What does decode() do??"
ans6="decode() converts bytes of data present in UTF-8 or other schemes to string."
