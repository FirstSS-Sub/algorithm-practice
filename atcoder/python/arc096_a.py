a, b, c, x, y = input().split()
a, b, c, x, y = int(a), int(b), int(c), int(x), int(y)
ans = 0
if a + b >= c * 2:
    if x < y:
        ans += x * c * 2
        if b >= c * 2:
            ans += (y - x) * c * 2
        else:
            ans += (y - x) * b
    else:
        ans += y * c * 2
        if a >= c * 2:
            ans += (x - y) * c * 2
        else:
            ans += (x - y) * a
else:
    ans += x * a + y * b
print(ans)
