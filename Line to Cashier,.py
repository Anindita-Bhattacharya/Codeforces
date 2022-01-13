
n=int(input())
num=[]
x=list(map(int,input().split()))
for i in range(n):
    a=list(map(int,input().split()))
    x1=0
    for j in a:
        x1=x1+(j*5)
    x1=x1+(15*x[i])
    num.append(x1)
print(min(num))
