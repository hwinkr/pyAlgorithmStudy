import sys
sys.setrecursionlimit(10000) # 백준에서 임의로 막아놓은 재귀함수의 최댓값(?)을 늘리기 위해

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M: # 그래프 밖으로 나가는것을 방지
        return False
    
    if graph[x][y] == 1: # 1을 만나면 (배추가 심어진 곳이라면)
        graph[x][y] = 2 # 2로 바꾸고
        dfs(x-1, y) # 상하좌우에 배추가 있는지 계속해서 확인한다
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True # 있을 때만 True값을 반환한다 = 뭉처져있는 한 파트에 대해서 한번의 True값만 반환한다
    return False


T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    
    M, N, K = map(int, input().split()) # 가로길이:M, 세로길이:N, 배추가 심어져있는 위치의 개수:K
    
    graph = [[0]*M for _ in range(N)]; # 그래프 초기화

    for _ in range(K): 
        X, Y = map(int, input().split()) # 가로값:X, 세로값:Y
        graph[Y][X] = 1 # 배추가 심어진 위치를 1로 바꾸기
    # print(graph)
    
    result = 0 
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result+= 1
    # print(graph)
    print(result)
    