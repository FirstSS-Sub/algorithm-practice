s = input()
dic = {"A", "C", "G", "T"}
temp = 0
ans = 0
for i in s:
    if i in dic:
        temp += 1
    else:
        temp = 0
    if temp > ans:
        ans = temp
print(ans)
