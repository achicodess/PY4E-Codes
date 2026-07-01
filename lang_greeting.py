print("Supported languages: Hindi, English, French, Portuguese and Dutch")
print("Press hindi, dutch, portu, english and fr")
name=input("Enter your name: ").strip()
#srtip() removes whitespaces from beggining and end of "name" string if the user enters one.
lang=input("Enter your language: ").lower()
#lower() coverts all charecters to lowercase.
if lang=="hindi":
	print("Namaste",name)
elif lang=="dutch":
	print("Hallo",name)
elif lang=="portuguese":
	print("Oi",name)
elif lang=="english":
	print("Hello",name)
elif lang=="french":
	print("Bonjour",name)
else:
	print("Please enter only the supported languages")