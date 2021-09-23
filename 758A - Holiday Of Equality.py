n=int(input())
a=list(map(int,input().strip().split()))
b=max(a)
sum1=0
for i in range(len(a)):
    sum1=sum1+(b-a[i])
print(sum1)
    
    
