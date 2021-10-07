a=input()
b="hello"
count=0
for i in range(len(a)):
    if a[i]=="h" and count==0:
        count=count+1 
    elif a[i]=="e" and count==1:
        count=count+1 
    elif a[i]=="l" and count==2:
        count=count+1 
    elif a[i]=="l" and count==3:
        count=count+1 
    elif a[i]=="o" and count==4:
        count=count+1 
    if count==5:
        break
if count==5:
    print("YES")
else:
    print("NO")
