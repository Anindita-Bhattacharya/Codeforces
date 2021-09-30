m,n=map(int,input().split())
count=0
for i in range(m):
    a=list(input().split())
    if "C" in a or "M" in a or "Y" in a  :
        count=count+1
if count>0:
    print("#Color")
else:
    print("#Black&White")
