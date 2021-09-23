n = int(input())
 
a = list(map(int, input().split()))
 
hired =  0
u=0
 
for el in a:
    if el > 0:
        hired += el
        continue
    if hired > 0 and el < 0:
        hired -= 1
        continue
    if el < 0:
        u += 1
 
print(u)
