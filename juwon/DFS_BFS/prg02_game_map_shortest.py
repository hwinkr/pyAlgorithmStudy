#-*- coding:utf-8 -*-

from collections import deque

def bfs(maps):
    
    N = len(maps) - 1 # 세로
    M = len(maps[0]) - 1 # 가로
    dx = [0, 1, 0, -1] # 4방향 북동남서 순서
    dy = [1, 0, -1, 0]

    q = deque()
    q.append([0,0])
    
    while q:
        a,b = q.popleft()
        
        if a == N and b == M: # 끝에 도달하면
            print(maps[a][b])
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx <= N and 0 <= ny <= M and maps[nx][ny] == 1: # 범위안에서 1이면(벽이 아니면)
                q.append([nx,ny])
                maps[nx][ny] = maps[a][b] + 1 # 앞으로 나아갈 수 있으면 (그 전의 값)+1 한 값을 나아갈 곳에 저장함
    
    if maps[N][M] == 1: # 끝에 도달하지 못하면
        print(-1)
    
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,0,1]]	

bfs(maps)

# print(maps)

