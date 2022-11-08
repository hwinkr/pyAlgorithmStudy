from collections import deque
N, K = map(int, input().split())
visit = [0 for i in range(100001)]
queue = deque()
# 기준점
queue.append([N, 0])
# 
while queue:
    x, y = queue[0][0], queue[0][1]
    # 기준점이 K가 되었을 때 종료
    if x == K:
        break
    queue.popleft()
   # 케이스에 따라 늘려나감
    visit[x] = 1
    if x - 1 >= 0 and visit[x - 1] == 0:
        queue.append([x - 1, y + 1])
    if x + 1 <= 100000 and visit[x + 1] == 0:
        queue.append([x + 1, y + 1])
    if x * 2 <= 100000 and visit[x * 2] == 0:
        queue.append([x * 2, y + 1])
print(queue[0][1])