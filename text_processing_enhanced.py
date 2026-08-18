print("This program is about text processing.")

q1 = "What's ASCII abbreviated?"
ans1 = "American Standard Code for Information Interchange."

q2 = "What is the use of the 'ord()' function?"
ans2 = "The ord() function returns the numerical (Unicode/ASCII) value of a single character."

q3 = "What is Unicode?"
ans3 = "Unicode is a character encoding standard that supports a very large number of characters from many languages and symbol sets."

q4 = "Which encoding scheme is advised for data exchanged between systems, and why is it preferred?"
ans4 = "UTF-8 is preferred because it has a variable length (1 to 4 bytes) and is backward-compatible with ASCII."

q5 = "What does encode() do?"
ans5 = "encode() converts a string into bytes using a specified encoding (default is UTF-8)."

q6 = "What does decode() do?"
ans6 = "decode() converts bytes back into a string using a specified encoding (default is UTF-8)."

questions = [q1, q2, q3, q4, q5, q6]
answers = [ans1, ans2, ans3, ans4, ans5, ans6]

print("\nThe available questions are:")
for i, q in enumerate(questions, 1): #enumerate() adds a counter to an iterable and returns it as an enumerate object
    print(f"{i}. {q}")

try:
    opt = int(input("\nEnter your desired question number (1-6): "))
    if 1 <= opt <= 6:
        print(f"\nQ: {questions[opt-1]}")
        print(f"A: {answers[opt-1]}")
    else:
        print("Invalid input. Please enter a number between 1 and 6.")
except ValueError:
    print("Invalid input. Please enter a valid number.")