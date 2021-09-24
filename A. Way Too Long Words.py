n=int(input())
while(n>0):
    a=input()
    if len(a)<=10:
        print(a)
    else:
        b=len(a)
        print(a[0]+str(b-2)+a[-1])
    n=n-1
