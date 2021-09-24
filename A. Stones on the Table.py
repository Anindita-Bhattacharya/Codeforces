n=int(input())
a=input()
b=list(a)
count1=0
if b.count(b[0]==len(b)):
    print(len(a)-1)
else:
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            count1=count1+1 
    print(count1)
