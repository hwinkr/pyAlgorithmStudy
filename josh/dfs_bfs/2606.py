n = int(input()) # 컴퓨터 개수
v = int(input()) # 연결선 개수
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
for i in range(v):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = 1
    for n in graph[v]:
        if visited[n]==0:
            dfs(n)

dfs(1)
print(sum(visited)-1)