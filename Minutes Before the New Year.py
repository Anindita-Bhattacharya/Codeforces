t=int(input())
while(t>0):
    m,n=map(int,input().split())
    sum1=(m*60)+n 
    print(1440-sum1)
    t=t-1
