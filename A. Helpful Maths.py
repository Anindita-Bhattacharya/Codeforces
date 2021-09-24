a=input()
b=a.replace("+",'')
b=list(b)
c=[]
d=[]
for i in b:
    i=int(i)
    c.append(i)
c.sort()
for i in c:
    i=str(i)
    d.append(i)
s='+'
s=s.join(d)
print(s)
