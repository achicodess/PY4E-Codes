print("About Py Objects\n")

about=print("Objects are like the carriers of data which operate inbetween an input and the respective output.")
terminologies=["class","method","attribute","object"]
classs="Class is a template."
method="A function inside of a class that defines the capablity of a class."
attribute="A bit of data in the class."
objectt="Object is a particular instance in a class."

print("The terminologies of python objects are: ",terminologies)

try:
	learn=input("\nWhich of these do you want to learn about??")
except NameError:
	print("Error")
if learn=="class":
	print(classs)
elif learn=="method":
	print(method)
elif learn=="attribute":
	print(attribute)
elif learn=="object":
	print(objectt)
else:
	print("Check your spelling or input.")



