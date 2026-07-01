name=input("Enter your name: ")
prompt=input("What do you want to discover today? ",name)
msg1=("What is the weather like today??").lower()
msg2=("How can I improve my company's performance??").lower()
msg3=("My sales is beggining to pick up, what do I do next??").lower()
if prompt==msg1:
	temp=["hot", "cold", "normal", "Hot", "Cold", "Normal"]
	try:
		feel=input("How do you currently feel in your room?? Is it hot or cold or at a normal temperature??")
	except ValueError:
		print("Seems like it's not a temperature condition. Try again!!")
	if feel=="Hot" or "hot":
		print("The weather today seems to be around 30 to 35 degree celcius.")
	elif feel=="Cold" or "cold":
		print("There seems to be a slight dip in temperatures with the current being 15 to 20 degree celcuis.")
	else:
		print("Room temperatures are the best. The temperature now is around 25 to 26 degree celcius.")
elif prompt==msg2:
	data=input("Please tell me more about your company: ")
	obj=open("sample.txt", "w")
	obj.a(data)
	obj.readlines()
elif prompt==msg3:
	print("That is awesome!! Please give me more information on how the progress has been so far.")
else:
	print("Oops. We ran into a problem. We are trying our best to expand the AI's database.")
	quit()