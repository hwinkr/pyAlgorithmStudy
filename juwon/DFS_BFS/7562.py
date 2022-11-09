from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1] # 8방향
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs():
    q = deque()
    q.append([x,y]) # 입력받은 x,y를 한번에 append함
    graph[x][y] = 1 # 위치에 1증가시킴
    
    while q:
        a,b = q.popleft() # (ex: 처음 pop은 x,y , 그 이후는 8방향 ...) 
        
        if a == goal_x and b == goal_y: # 목표지점에 도착시 끝
            print(graph[goal_x][goal_y] - 1) # 처음부터 1로 시작하므로 1을 빼고 출력
            return 
        
        for i in range(8): #8방향으로 bfs
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0: # 범위안에서 안가본 곳일 때
                q.append([nx, ny])
                graph[nx][ny] = graph[a][b] + 1 # 위치에 1증가시킴


T = int(input())

for _ in range(T):
    
    l = int(input())
    x,y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    
    graph = [[0]*l for _ in range(l)] # 그래프 초기화
    bfs()    
    