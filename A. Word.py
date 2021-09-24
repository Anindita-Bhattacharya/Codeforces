a=input()
b=list(a)
count=0
count2=0
for i in b:
    if (i.islower()):
        count=count+1 
    else:
        count2=count2+1
if(count>count2 or count==count2):
    print(a.lower())
if(count<count2):
    print(a.upper())
