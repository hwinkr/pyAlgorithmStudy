from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        if x == target_row and y == target_col:
            return rect[x][y]

        for i in range(8):
            nx = x + dir[i][0]
            ny = y + dir[i][1]

            if 0 <= nx < side and 0 <= ny < side:
                if not rect[nx][ny]:
                    rect[nx][ny] = rect[x][y] + 1
                    que.append((nx, ny))


if __name__ == "__main__":
    test_cnt = int(input())
    for _ in range(test_cnt):
        side = int(input())
        # * 체스판을 모두 0으로 초기화 하면 방문처리와 좌표까지 도착하는데 걸린 이동 횟수의 최솟값을 한번에 처리할 수 있다.
        rect = [[0] * side for _ in range(side)]
        dir = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]

        start_row, start_col = map(int, input().split())
        target_row, target_col = map(int, input().split())
        print(bfs(start_row, start_col))
