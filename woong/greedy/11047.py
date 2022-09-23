import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n - 1, -1, -1):
    cnt += k // lst[i]
    k %= lst[i]
 
print(cnt)
