a=input()
a=a.lower()
b=input()
b=b.lower()
if(len(a)==len(b) and a<b):
    print("-1")
    
if(len(a)==len(b) and b<a):
    print("1")
if(len(a)==len(b) and b==a):
    print("0")
