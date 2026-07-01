# lits start with []
friends=["Rohan", "Arth", "Sunil", "Govind"]
print(friends[2])
for yes in friends:
	print(yes, "is invited.")
	print("Welcome", yes)
print("*To check if a name is there in the list, use the tool below.*")
checktool=input("Enter name: ")
print(checktool in friends)
respo=input("Any more attending?? (Yes/No)")
if respo.lower()=="yes":
	try:
		extra=input("Enter name: ") 
		friends.append(extra)
		print(friends)
	except ValueError:
		print("Enter valid input.")
	quit()
else:
	print("Exiting...")
	quit()


	


