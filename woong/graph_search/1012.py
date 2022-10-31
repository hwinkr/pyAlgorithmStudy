import sys

input = sys.stdin.readline
# * 파이썬의 재귀함수 제한은 default 로 1000 으로 설정되어 있다. 모든 테스트 케이스를 통과하기 위해서는 재귀함수 호출 제한을 명시적으로 늘려줘야 한다.
sys.setrecursionlimit(10000)

test = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    # * 이미 탐색한 밭의 위치를 재탐색하지 않기 위해서 한번 탐색한 위치는 다시 0으로 변경해준다. 시간 복잡도를 줄이기 위해서는 필수적으로 해줘야 한다.
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # * 지렁이의 다음 위치가 밭의 범위를 벗어 나지 않는 경우에만 계속 탐색을 진행한다.
        # * 파이썬은 index Error에 대해서 매우 엄격하기 때문에 필수적으로 해줘야 한다.
        if 0 <= nx < row and 0 <= ny < col:
            if graph[nx][ny] == 1:
                dfs(nx, ny)


for _ in range(test):
    # * 문제에서 행, 열이 아닌 가로, 세로로 제시한다면 row, col 로 변수를 저장해서 더 풀기 쉽도록 만드는 것이 좋겠다.
    col, row, cabbage_cnt = map(int, input().split())
    graph = [[0] * col for _ in range(row)]
    worm_cnt = 0
    for _ in range(cabbage_cnt):
        i, j = map(int, input().split())
        # ! 가로 세로 조심
        graph[j][i] = 1

    for i in range(row):
        for j in range(col):
            # * 배추가 심어져 있디면, 지렁이 한마리를 추가해주고 지렁이가 옮겨갈 수 있는 밭의 위치에 대해서 탐색을 시작해준다.
            if graph[i][j] == 1:
                worm_cnt += 1
                dfs(i, j)

    print(worm_cnt)
