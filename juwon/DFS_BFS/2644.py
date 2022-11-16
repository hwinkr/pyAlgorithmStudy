from collections import deque # bfs에서의 큐 사용

n = int(input()) # 전체 사람의 수 (정점의 개수)
result_x, result_y = map(int, input().split()) # 비교할 두 대상
m = int(input()) # 부모자식의 관계의 개수 (간선의 개수)

graph = [[] for _ in range(n+1)] # 그래프 초기화
visited = [0] * (n+1) # 방문기록 초기화

for _ in range(m): # 그래프 연결
    x, y = map(int, input().split())
    graph[x].append(y) 
    graph[y].append(x) 
            
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] += 1 # 처음은 1
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1 # 이전 방문노드에서 +1
    

bfs(result_x)
    
if visited[result_y] > 0: # result_x와 result_y과 연결되어 있다면
    print(visited[result_y] - 1)
else: # 아니라면
    print(-1)