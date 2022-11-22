import sys
from collections import deque

n = int(sys.stdin.readline())

x, y = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]

visited = [0 for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


deq = deque()

deq.append(x)
cnt = 0
while deq:
    a = deq.popleft()
    for b in graph[a]:
        if visited[b] == 0:
            visited[b] = visited[a] + 1
            deq.append(b)

if visited[y] > 0:
    print(visited[y])