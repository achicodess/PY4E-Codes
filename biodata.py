name=input("Enter user name: " )
data=input("Enter bio-data of user: ")
obj=open("bdata1.txt","w")
obj.writelines(data)
try:
	obj1=open("bdata1.txt", "r")
	if True:
		print("Data in file is: ")
		print(bdata1.txt)
	else:
		print("Error opening file.")
except:
	print("Error opening file.")


