n=int(input())
coins=list(map(int,input().split()));
coins.sort()
coins=coins[::-1]
num1=0 
count=0 
for i in range(len(coins)):
    num1=num1+coins[i]
    count=count+1
    if num1>sum(coins)-num1:
        print(count)
        break
    
        
