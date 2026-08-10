name=input("Enter your name: ")
print("Welcome", name)
try:
	userid=int(input("Enter your userid: "))
	password=int(input("Enter your password: "))
except ValueError:
	print("Only number credentials allowed.")
listuserid=["1234", "4321"]
listpassword=["2026","6202"]
if userid and password in listuserid and listpassword:
	print("Login sucessful. Redirecting to homepage.")
else:
	print("User not found / Incorrect credentials.")
