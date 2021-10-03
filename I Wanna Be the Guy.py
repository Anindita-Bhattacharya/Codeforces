n=int(input())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
X1=X[1:]
Y1=Y[1:]
Z=X1+Y1
Z=list(set(Z))
sum1=sum(Z)
sum2=n*(n+1)//2 
if sum1==sum2:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
