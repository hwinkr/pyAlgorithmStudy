N = int(input())
request = list(map(int, input().split()))
money = int(input())

start = 0
end = max(request)

while start <= end:
    total = 0
    mid = (start+end) // 2
    
    for x in request:
        if x >= mid:
            total += mid
        else:
            total += x
    
    print(start, mid, end)
    print(total)

    
    if total <= money:
        start = mid + 1
    else:
        end = mid - 1

print(end)

            