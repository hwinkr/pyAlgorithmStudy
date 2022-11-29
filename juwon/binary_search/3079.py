N, M = map(int, input().split())

time = []
for _ in range(N):
    time.append(int(input()))
    
start = 0
end = max(time) * M

result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    
    for x in time:
        total += mid // x
    
    if total < M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)