from collections import deque
import sys

input = sys.stdin.readline

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(que, cheezes, graph, visited):
    while que:
        x, y = que.popleft()
        for dx, dy in DIRECTIONS:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    que.append((nx, ny))
                else:
                    graph[nx][ny] = 0
                    cheezes.append((nx, ny))

                visited[nx][ny] = True


if __name__ == "__main__":
    row, col = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(row)]
    visited = [[False for _ in range(col)] for _ in range(row)]
    time, count = 0, 0
    que, cheezes = deque([(0, 0)]), []

    while True:
        bfs(que, cheezes, graph, visited)
        if not cheezes:
            break
        time += 1
        count = len(cheezes)
        que, cheezes = deque(cheezes), []

    print(time)
    print(count)
