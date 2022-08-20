n = int(input())
ans = 0
for i in range(n):
    count = 0
    for j in range(i+1):
        if (i+1) % 2 == 1:
            if (i+1) % (j+1) == 0:
                count += 1
    if count == 8:
        ans += 1
print(ans)
