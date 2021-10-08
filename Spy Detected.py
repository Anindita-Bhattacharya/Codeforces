t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    for i in a:
        if a.count(i)==1 :
            print((a.index(i))+1)
    t=t-1
