import sys
input = sys.stdin.readline

sugar = int(input())
cnt = 0
while sugar >= 0:
    if not sugar % 5:
        cnt += sugar // 5
        print(cnt)
        break
    cnt += 1
    sugar -= 3
else:
    print(-1)
