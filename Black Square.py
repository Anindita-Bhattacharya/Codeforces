a=list(map(int,input().split()))
b=int(input())
b=str(b)
b=list(b)
x1=b.count("1")*a[0]
x2=b.count("2")*a[1]
x3=b.count("3")*a[2]
x4=b.count("4")*a[3]
print(x1+x2+x3+x4)