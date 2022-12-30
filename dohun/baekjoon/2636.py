from collections import deque
import sys
input = sys.stdin.readline

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(q, stack, graph, visited):
    while q:
        i, j = q.popleft()
        for di, dj in DIRECTIONS:
            ni = i + di
            nj = j + dj
            if 0 <= ni < row and 0 <= nj < col and not visited[ni][nj]:
                if not graph[ni][nj]:
                    q.append((ni, nj))
                else:
                    stack.append((ni, nj))
                visited[ni][nj] = 1

def melt(stack, graph):
    for i, j in stack:
        graph[i][j] = 0

if __name__ == "__main__":
    row, col = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0 for _ in range(col)] for _ in range(row)]
    q, stack = deque([(0, 0)]), []
    count = cheez = 0

    while True:
        bfs(q, stack, graph, visited)
        if not stack:
            break
        melt(stack, graph)
        count += 1
        cheez = len(stack)
        q, stack = deque(stack), []
    
    print(count)
    print(cheez)
    