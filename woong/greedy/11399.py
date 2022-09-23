# i번 사람이 돈을 인출하는데 걸리는 시간이 Pi
# 줄을 서는 순서에 따라서 돈을 인출하는데 걸리는 시간의 합이 달라진다..?
# 시간의 합 최소

# 그렇다면 기다리는 시간을 최소로 만들어줘야한다 -> 돈을 뽑는데 걸리는 시간은 고정이기 때문에 기다리는 시간을 최소로 만들어주면 시간의 합을 최소로 만들수 있다.

import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))

times.sort()
tmp = 0
ans = 0

for time in times:
    tmp += time
    ans += tmp

print(ans)
