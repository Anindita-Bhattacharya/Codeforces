t=int(input())
count=0
while(t>0):
    a1=[]
    a,b,c=map(int,input().split())
    a1.append(a)
    a1.append(b)
    a1.append(c)
    if(a1.count(1)==3 or a1.count(1)==2):
        count=count+1 
    t=t-1
print(count)
