n=0
X=int(input())
for i in range(X):
    a=input()
    if a[0]=='+' or a[1]=='+':
        n=n+1 
    else:
        n=n-1
print(n)
