n,h=map(int,input().split())
a=list(map(int,input().split()))
sum1=0
sum2=0
for i in a:
    if i<=h:
        sum1=sum1+1 
    else:
        sum2=sum2+2 
print(sum1+sum2)
