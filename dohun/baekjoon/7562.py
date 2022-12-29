from collections import deque
import sys
input = sys.stdin.readline

DIRECTIONS = [(1, -2), (1, 2), (2, -1), (2, 1), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]
INF = 10 ** 8

def solve():
    n = int(input())
    start_i, start_j = map(int, input().split())
    target_i, target_j = map(int, input().split())

    board = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([(start_i, start_j)])
    board[start_i][start_j] = 0

    while q:
        i, j = q.popleft()

        if i == target_i and j == target_j:
            break

        for di, dj in DIRECTIONS:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and not board[ni][nj]:
                board[ni][nj] = board[i][j] + 1
                q.append((ni, nj))
    print(board[target_i][target_j])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()