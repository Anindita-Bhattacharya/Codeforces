a1=[]
for i in range(5):
    b=list(map(int,input().strip().split()))[:5]
    a1.append(b)
if(a1[2][2]==1):
    print("0")
else:
    for i in range(5):
        for j in range(5):
            if(a1[i][j]==1):
                row=i 
                column=j 
    
    k=row+1  
    l=abs(3-k) 
    column=column+1 
    m=abs(3-column) 
    print (l+m) 
