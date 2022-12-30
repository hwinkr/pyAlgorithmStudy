N, H = map(int, input().split())
obstacle = []
for _ in range(N):
    obstacle.append(int(input()))
    
bottom = []
top = []

for i in range(N):
    if i%2 == 0:
        bottom.append(obstacle[i])
    else:
        top.append(obstacle[i])
        
top.sort()
bottom.sort()

result = N
count = 0

def binary(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(1, H+1):
    bottom_count = len(bottom) - binary(bottom, i-0.5, 0, len(bottom)-1)
    top_count = len(top) - binary(top, H-i+0.5, 0, len(top)-1)
    
    if result == bottom_count + top_count:
        count += 1
    elif result > bottom_count + top_count:
        count = 1
        result = bottom_count + top_count

print(result, count)