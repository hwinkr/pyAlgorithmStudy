N = int(input())

graph = [list(input().rstrip()) for i in range(N)] # 그래프 생성
visited = [[0] * N for i in range(N)] # 방문한 정점
houses = []
house = 0


def search(i, j): # 탐색
    # 종료
    global house
    if i < 0 or j >= N or i >= N or j < 0 or graph[i][j] == '0':
        return
    graph[i][j] = '0' # 탐색한 지점 0으로 변경
    visited[i][j] = 1 # 방문한 정점 표시
    house += 1  # 마을 수 갱신

    # 상하좌우 탐색
    search(i + 1, j)
    search(i, j + 1)
    search(i - 1, j)
    search(i, j - 1)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] == '1':
            search(i,j)
            houses.append(house)
            house = 0

print(len(houses))
for i in sorted(houses):
    print(i)