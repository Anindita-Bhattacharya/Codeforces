t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    x=True
    for i in range(len(a)-1):
        if abs(a[i]-a[i+1])>1:
            x=False
            break 
    if(x):
        print("YES")
    else:
        print("NO")
            
    t=t-1
