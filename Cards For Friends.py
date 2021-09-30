t = int(input())
for i in range(t):
    w, h, n = list(map(int, input().split()))
 
    count = 1
    count1 = 1
    if w % 2 == 0:
        w2 = w
        while w2 % 2 == 0:
            count *= 2
            w2 /= 2
    if h % 2 == 0:
        h2 = h
        while h2 % 2 == 0:
            count1 *= 2
            h2 /= 2
    total = count1 * count
    if total >= n:
        print("YES")
    else:
        print("NO")
