from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y): # 바깥부분만 탐색하도록
    q = deque()
    q.append([x,y])
    graph[x][y] = hours
    


X, Y = map(int, input().split())

graph = []
for i in range(X):
    graph.append(list(map(int, input().split())))
    
hours = 2

while graph in 1:
    
    last_cheeze = 0
    
    bfs(0, 0)
    
    for i in range(X):
        for j in range(Y):
            if graph[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if graph[nx][ny] == hours:
                        last_cheeze += 1
                        graph[i][j] = 0
                        break
    # 그래프에 있는 모든 hours를 0으로 바꾸고
    hours += 1
    
print(hours-1)
print(last_cheeze)