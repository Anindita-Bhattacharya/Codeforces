a=int(input())
count=0
while(a!=0):
    if(a%10==7 or a%10==4):
        count=count+1 
    a=a//10 
if count==7 or count==4:
    print("YES")
else:
    print("NO")
