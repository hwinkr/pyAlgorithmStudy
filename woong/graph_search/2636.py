from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    melt_count = 0

    while que:
        x, y = que.popleft()

        for (dx, dy) in DIRECTION:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheezes[nx][ny] == 0:
                    que.append((nx, ny))
                # * 가장자리가 1이다, que 에 추가하지 않음 => 추가하면 안쪽으로 들어가서 또 녹임
                # ! 가장자리 1을 방문 표시와 녹이고, 다시 que 에 추가하지 않는 것이 핵심
                elif cheezes[nx][ny] == 1:
                    cheezes[nx][ny] = 0
                    melt_count += 1

    return melt_count


if __name__ == "__main__":
    row, col = map(int, input().split())
    cheezes = [list(map(int, input().split())) for _ in range(row)]
    DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    times = 0
    melt_cheezes = []

    while True:
        # ! 시간 지날 때 마다 visited 초기화 해야함, 0 으로 인해서 녹을 치즈가 생기게 해줘야함!
        visited = [[0] * col for _ in range(row)]

        cnt = bfs(0, 0)
        if cnt == 0:
            break

        melt_cheezes.append(cnt)
        times += 1

    print(times)
    print(melt_cheezes[-1])
