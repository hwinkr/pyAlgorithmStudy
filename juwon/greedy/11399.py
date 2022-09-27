n = int(input())
pi = list(map(int, input().split()))
    
pi.sort()

# 정렬된 리스트에서 [0]*n + [1]*(n-1) + ...하면 원하는 값을 구할 수 있다
sum_time = 0
for time in pi: 
    sum_time = sum_time + time * n
    n = n - 1

print(sum_time)