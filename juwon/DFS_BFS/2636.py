import sys
from collections import deque
input = sys.stdin.readline

def bfs(): 
    q = deque()
    q.append([0,0]) # 0,0부터 시작
    visited[0][0] = 1
    cnt = 0
    
    while q:
        x,y = q.popleft()
        for i in range(4): # 동서남북 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<X and 0<=ny<Y and visited[nx][ny] == 0: # 범위안에서 방문안한곳이 있을 때
                if graph[nx][ny] == 0: # 그곳이 0이라면 큐에 넣고 방문처리
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    
                elif graph[nx][ny] == 1: #* 그곳이 1이라면 큐에 넣지 않고 방문처리한다 이때 1은 가장자리 치즈임을 알 수 있다
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt



X, Y = map(int, input().split())
graph = []
for i in range(X):
    graph.append(list(map(int, input().split())))
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []

hours = 0 # 치즈가 녹아 없어지는 시간
while 1:
    hours += 1

    visited = [[0]*Y for _ in range(X)]    
    cnt = bfs()
    if cnt == 0:
        break

print(hours - 1)
print(ans[-2])
