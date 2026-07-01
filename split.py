mail="From learnpy@drchuckmail.com Sun Jun 29 19:05"
words=line.split()
email=words[1]
pieces=email.split("@")
print(pieces[1])