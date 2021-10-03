m,n=map(int,input().split())
s=input()
b=list(s)
for j in range(n):
    i=0
    while(i<len(b)-1):
        if b[i]=="B" and b[i+1]=="G":
            b[i]="G"
            b[i+1]="B"
            i=i+1
        i=i+1
print("".join(b))
