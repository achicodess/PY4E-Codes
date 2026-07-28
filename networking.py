print("Concepts of Networking")

print("1. Know more about Networking")
print("2. Learn with examples")
print("3. Exit program \n")

try:
	choice=int(input("Enter an option: "))
except ValueError:
	print("Only numbers allowed!")
	choice=None

if choice == 1:
	print("Great choice.")
	print("Networking in computer science is the study of how connected devices share data, using communication protocols, and physical or wireless links")
elif choice == 2:
	print("Got it! \n")
	print("(A) The Internet, your home Wi-Fi networks, and office printer setups can be taken as examples.")
	print("(B) HTTP/HTTPS: This is the protocol used by your web browser to load and view websites.")
	print("(C) DNS (Domain Name System): This system translates human-friendly names (like google.com) into computer IP addresses.")
elif choice==3:
	print("See you in a while :)")
elif choice is not None:
    print("\nPlease enter a valid menu option (1, 2, or 3).")
	