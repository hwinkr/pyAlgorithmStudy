import sys
input = sys.stdin.readline
nums = input().split('-')

lst = []

for num in nums:
    sum = 0
    num = num.split('+')
    for a in num:
        sum += int(a)
    lst.append(sum)

ans = lst[0]
for i in range(1, len(lst)):
    ans -= lst[i]

print(ans)
