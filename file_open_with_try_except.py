name=input("Enter name of file to be opened: ")
mode=input("Enter type of mode to oprn file in: ")
try:
	obj=("name","mode")
	count=0
	for line in obj:
		realcount=count+1
		print("The number of lines is:",realcount)
except:
	print("File not found")
