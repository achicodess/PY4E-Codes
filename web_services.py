print("Commanly used web services are: XML and JSON\n")
q1="1. Learn more about XML\n"
q2="2. Learn more about JSON\n"
q3="3. View Coclusion\n"
print("Questions are:\n ",q1,q2,q3)
try:
	opt=int(input("Enter your desired option out of the three: "))
except ValueError and opt>2:
	print("Invalid input!")
if opt==1:
	print("Abb.: eXtensible Markup Language")
	print("Used to store, organise and transport data that is understood both by humans and machines.")
elif opt==2:
	print("Abb.: JavaScript Object Notation")
	print("Python actually processes JSON. JSON represents data as nested lists and dictionaries.")
elif opt==3:
	print("To conclude, Python actually let's you connect to the web and other programming languages using it's own set of libraries allowing for a multi-language application and integration.\n")
else:
	print("Program terminated.")   

