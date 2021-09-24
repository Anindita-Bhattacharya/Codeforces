n,m=map(int,input().split())
sum1=0
for i in range(10):
    sum1=sum1+n 
    if sum1%10 ==0 or sum1%10==m:
        print(i+1)
        break 
