sh=input("Enter hours: ")
sr=input("Enter rate: ")
try:
    fh=float(sh)
    fr=float(sr)
except:
    print("Enter numerical values only!!")
    quit()
if fh>40:
    #print("Overtime")
    reg=fh*fr
    ot=(fh-40.0)*(fr*0.5)
    #print(reg,op)
    xp=reg+ot
else:
    #print("Regular")
    xp=fh*fr
print(xp)