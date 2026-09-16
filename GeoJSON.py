print("About GeoJSON")

info1="APIs are really useful webservices that follow certain rules published by the service providers that applications must follow to make use of their services."
info2="Examples of API include Google's Geocoding API"
info3="Primary source of understanding how an API works and how you can implement it is by reading the official documentation."
info4="Rate limiting refers to an API allowing 'x' number of request a day."
info5="Rate limiting is done because these are extreamely valuable and compute intensive processes. So, the provider might ask you to log in or buy their subcription or key to increase your limit etc."

print("What do you want to know??")

opt1="1.What is an API??"
opt2="2.Examples of APIs."
opt3="3.What's the primary source of understanding an API?"
opt4="4.What is rate limiting?"
opt5="5.Why is rate limiting required?"

print("The available information are: \n",opt1,opt2,opt3,opt4,opt5)

try:
	option=int(input("Enter your option (1-5)"))
except ValueError:
	print("Incorrect input!")

if option==1:
	print(info1)
elif option==2:
	print(info2)
elif option==3:
	print(info3)
elif option==4:
	print(info4)
elif option==5:
	print(info5)
else:
	print("Bad Input")

print("x-- Program executed successfully --x")

