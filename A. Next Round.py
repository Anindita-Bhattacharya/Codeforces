count=0
n,k=map(int,input().strip().split())
a=list(map(int,input().split(" ")))
if a[0]<=0:
    print("0")
else:
    for i in range(len(a)):
        if(a[i]<a[k-1] or a[i]<=0):
            break
        else:
            count=count+1
    print(count)
