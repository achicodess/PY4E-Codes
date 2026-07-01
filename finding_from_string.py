text = "X-DSPAM-Confidence:    0.8475"
find=text.find(" ")
print(find)
fragment=text[find:] .strip()
print(fragment)