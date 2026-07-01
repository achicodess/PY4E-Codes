dicto={"Paul": "New", "Harish": "Old", "Satish": "Old", "Sonam": "New"}
print(dicto)
try:
	inp=input("Enter user name: ")
except ValueError:
	print("Enter alphabets only.")

for names in dicto:
	if names in dicto:
		print("User found in database")
	elif:
		opt=input("Want to add user??(Y/N)")
	elif opt==Y:
	new=input("Enter name: ")
	dicto.append(new)
else:
	quit()
print("Program executed successfully.")


	



