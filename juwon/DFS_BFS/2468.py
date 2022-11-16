import sys
sys.setrecursionlimit(10**6) # 1000으로 되어있는 재귀함수 호출 제한을 늘리기 위해

def dfs(x, y, graph):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    graph[x][y] = 0
    
    for i in range(4): # 계속해서 dfs함수를 진행할 수 있다면 진행하고
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] > 0:
                dfs(nx, ny, graph)
    return True # 아니면 True를 반환한다


N = int(input()) # 2차원 배열 행,열 개수

graph = [] # 그래프 초기화
for i in range(N): # 그래프 입력
    graph.append(list(map(int, input().split())))
    
for i in range(N): # 배열안에서 가장 큰 수 max_num 찾기
    max_num = 0
    if max_num < max(graph[i]):
        max_num = max(graph[i])
        
graph_copy = [[0]*N for _ in range(N)] # *비가 0~max_num까지 오는데
                                       # *그때마다 새로운 그래프를 써야하기 때문
safe_list = [] # 0~max_num일때 각각 안전한장소 개수
for rain in range(max_num+1):
    # print("rain:",rain)
    for x in range(N):
       for y in range(N):
           if rain >= graph[x][y]: # 침수된곳은 -1로 아닌곳은 그 수로 2차원 배열 만들기
               graph_copy[x][y] = -1
           else:
               graph_copy[x][y] = graph[x][y]
    # print(graph_copy)
    safe = 0 # 안전한 장소 개수 초기화
    for i in range(N):
        for j in range(N):
            if graph_copy[i][j] > 0:
                if dfs(i, j, graph_copy) == True:
                    safe += 1
                    # print(safe, i, j)
    safe_list.append(safe) 
    # print(graph_copy)
    # print("-----------")
# print(safe_list)
print(max(safe_list)) # 안전장소 리스트 중에서 가장 큰 수 출력