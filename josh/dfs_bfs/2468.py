import sys

#상 하 좌 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# x,y 지점을 기준으로 주변을 탐색하는 재귀함수 
def sink_DFS(x, y, h):
    # 상하좌우 좌표를 반복문으로 받음
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        # 자신이 건너갈 nx, ny 좌표에 대한 유효성을 확인
        if (0 <= nx < N) and (0 <= ny < N) and not sink_table[nx][ny] and water_board[nx][ny] > h:
            sink_table[nx][ny] = True
            sink_DFS(nx, ny, h)


N = int(sys.stdin.readline())
water_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#입력값에 따른 물 높이 board 생성


# 물에 잠김 여부를 확인
cnt = 1
for k in range(max(map(max, water_board))):
    sink_table = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if water_board[i][j] > k and not sink_table[i][j]:
                count += 1
                sink_table[i][j] = True
                sink_DFS(i, j, k)
    cnt = max(cnt, count)

print(cnt)