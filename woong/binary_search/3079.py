# * 입국심사
# * 모든 사람이 입국 심사를 하는데 걸리는 시간의 최.솟.값

import sys

input = sys.stdin.readline


passport_cnt, people = map(int, input().split())
times = [int(input()) for _ in range(passport_cnt)]
times.sort()

start = 0
end = times[-1] * people  # 모든 사람이 가장 오래 걸리는 심사대에서 심사를 받을 경우에 걸리는 시간
# * 주어진 시간 동안 하나의 심사대에서 심사할 수 있는 사람의 수로 판단한다

while start <= end:
    mid = (start + end) // 2
    tmp = 0

    # * 주어진 시간 동안 몇명을 검색할 수 있는가?
    # * 에를 들어서 mid 값이 28이고, 어떤 심사대에서 심사하는데 걸리는 시간이 7 이라면 주어진 28 동안 4명을 심사할 수 있는 것이다.
    for time in times:
        tmp += mid // time

    if tmp >= people:  # 이 경우는, 주어진 시간이 너무 많다는것, 시간을 줄여야한다 시간을 줄이면서 가능한 최솟값을 찾는다.
        end = mid - 1
        ans = mid
    else:  # 이 경우는, 주어진 시간이 적다는것 따라서 조건을 만족하지 못하는 경우이고 심사할 수 있는 시간을 늘려주고 다시 판단한다
        start = mid + 1

print(ans)
