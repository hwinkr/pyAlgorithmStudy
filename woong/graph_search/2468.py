import sys

sys.setrecursionlimit(100000)  # 이 문제는 호출 제한을 무려 십만으로 해줘야함.. 참 많이도 호출한다
input = sys.stdin.readline

# dfs
def dfs(x, y):
    visited[x][y] = True

    for dx, dy in DIRECTION:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < n) and (0 <= ny < n):
            if not visited[nx][ny] and graph[nx][ny] > height:
                dfs(nx, ny)


n = int(input())  # 2 <= n <= 100
graph = [list(map(int, input().split())) for _ in range(n)]
DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]
max_height = max(max(graph))
max_area = -1

for height in range(max_height):
    visited = [[False] * n for _ in range(n)]
    area = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and not visited[i][j]:
                area += 1
                dfs(i, j)

    max_area = max(max_area, area)

print(max_area)
