from collections import deque
import sys

input = sys.stdin.readline


def bfs(x):
    que = deque()
    que.append(x)

    while que:
        x = que.popleft()
        if x == goal_height:
            return buttons[x]

        for nx in (x + up, x - down):
            if 1 <= nx <= total_height and not visited[nx]:
                visited[nx] = True
                buttons[nx] = buttons[x] + 1
                que.append(nx)

    return "use the stairs"


if __name__ == "__main__":
    total_height, current_height, goal_height, up, down = map(int, input().split())
    visited = [False] * (total_height + 1)
    buttons = [0] * (total_height + 1)
    print(bfs(current_height))
