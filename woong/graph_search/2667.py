from collections import deque
import sys

input = sys.stdin.readline


def bfs(i, j):
    house_cnt = 1
    graph[i][j] = 0
    que = deque()
    que.append((i, j))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    house_cnt += 1
                    graph[nx][ny] = 0
                    que.append((nx, ny))

    return house_cnt


if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().rstrip())) for _ in range(n)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    group_cnt = 0
    house_cnt_list = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                group_cnt += 1
                house_cnt_list.append(bfs(i, j))

    house_cnt_list.sort()
    print(group_cnt)
    for house_cnt in house_cnt_list:
        print(house_cnt)
