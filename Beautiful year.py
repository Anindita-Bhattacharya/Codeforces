year=int(input())
while(1):
    year=year+1 
    temp=year
    a=year%10
    year=year//10 
    b=year%10 
    year=year//10 
    c=year%10 
    year=year//10 
    d=year%10 
    if a!=b and b!=c and c!=d and a!=c and a!=d and b!=d:
        print(temp)
        break
    year=temp
 
