print("Learn more about Service Oriented Approach (SOA)\n")

print("How does this work?: You will learn about SOA in the form of questions followed by their answers. You need not answer the questions.\n")

abt="SOA is the integration of multiple web services into one application using APIs."
how="This is possible by creating infrastructure for an application so that multiple web services are integrated and work together."
way="Multiple Systems Approach: First, two systems work together and split the problem. Then, when service becomes useful, many other applications want to make use of that application!"
abtAPI="APIs are certain rules published by the services that application must follow to make use of their services."
examples="In education industry: UCAS\n,In research industry: myGrid\n,Resource Provider for both: e-Framework."

question1="1. What is SOA??\n"
question2="2. How is it applied??\n"
question3="3. In what way can it be implemented??\n"
question4="4. What is an API??\n"
question5="5. Learn about examples.\n"

print("The questions are:\n",question1,question2,question3,question4,question5)


quest=input("Enter the desired question number 1-5: ")

if quest==question1:
	print(abt)
elif quest==question2:
	print(how)
elif quest==question3:
	print(way)
elif quest==question4:
	print(abtAPI)
elif quest==question5:
	print(examples)
else:
	print("Enter a valid option number.")

print("Congratulations!! You have sucessfully learnt about SOA(s)!!")




