import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = []
for _ in range(N):
    times.append(int(input()))

# left는 0초, right는 최대 걸리는 시간 * M(심사할 사람의 명수)
left = 0
answer = right = max(times) * M

while left <= right:
    # mid는 M명을 심사하는데 걸리는 시간
    mid = (left+right) // 2
    people = 0
    print(left, right)
    for time in times:
        # mid를 각각 심사대에서 심사하는데 걸리는 시간으로 나눠서 몇명을 심사할 수 있는지 계산
        people += mid//time
    # people이 M 미만이면 시간을 더 늘려야함 left = mid + 1
    if people < M:
        left = mid + 1
    # 아니라면 시간을 줄여도 돼서 right를 mid -1하면서 크기 비교
    else:
        right = mid - 1
        answer = min(answer, mid)

print(answer)

