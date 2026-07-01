users=["Achintyaa","Anirvin","Aransha","Sudeep","Raghav","Praful"]
name=input("Enter your name: ").strip()
 
if name in users:
	print("Welcome",name,"!")
else:
	print("Name not found.Please register as a user!!")
