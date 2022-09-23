import sys
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = times[0][1]

for i in range(1, n):
    if end_time <= times[i][0]:
        cnt += 1
        end_time = times[i][1]

print(cnt)
