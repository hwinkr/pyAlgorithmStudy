from collections import deque
import sys

input = sys.stdin.readline


def bfs(x):
    virus_cnt = 0
    visited[x] = True

    que = deque()
    que.append(x)

    while que:
        current_virus = que.popleft()

        for computer in graph[current_virus]:
            # * 아직 바이러스에 의해서 감염되지 않은 컴퓨터가 있는 경우에만, virus_cnt + 1 을 해준다
            if not visited[computer]:
                visited[computer] = True
                que.append(computer)
                virus_cnt += 1

    return virus_cnt


if __name__ == "__main__":
    computers = int(input())
    connect_cnt = int(input())
    # * 컴퓨터의 수가 7 개라면, 방문 처리를 하기 위해서 7 + 1 칸의 배열이 필요하다. 인덱스는 0부터 시작하기 떄문에 마지막 7번 컴퓨터를 처리 하려면 크기를 8로 해야한다.
    visited = [False] * (computers + 1)
    graph = [[] for _ in range(computers + 1)]

    for _ in range(connect_cnt):
        a, b = map(int, input().split())
        # * 컴퓨터의 연결 관계를 나타내는 graph 자료구조는 양방향 그래프 이기 때문에, 서로의 정점에 간선을 추가해줘야 한다.
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(1))
