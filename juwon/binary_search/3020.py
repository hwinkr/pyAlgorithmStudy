# -- 수정중 --
N, H = map(int, input().split())
obstacle = []
for _ in range(N):
    obstacle.append(int(input()))
    
start = 0
end = H

result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    
    for x in obstacle:
        