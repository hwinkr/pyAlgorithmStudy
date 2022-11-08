from collections import deque


def solution(maps):

    n, m = len(maps), len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    que = deque()
    que.append((0, 0))
    maps[0][0] = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # * maps[ny][ny] == 1 인 경우만 que 에 추가해준다.
            # * 경로가 여러개여서 같은 위치를 여러번 반복해서 방문할 수 있는 경우가 생기는데 더 빠른 경로로 이동했을때의 이동횟수가 먼저 기록되기 떄문에, 재방문 하게되는 문제를 같이 해결할 수 있다.
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                que.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

    answer = maps[n - 1][m - 1]
    # * 파이썬의 3항 연산자, 알아두면 좋다.
    return -1 if answer == 1 else answer
