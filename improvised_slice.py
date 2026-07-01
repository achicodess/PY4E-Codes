string="Hackethons are interesting!!"
name=input("Enter a word to be found in 'string': ") .lower() .strip()
if name in string:
	print("Present")
else:
	print("Not present")
