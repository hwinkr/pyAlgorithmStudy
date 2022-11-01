from collections import deque
import sys

input = sys.stdin.readline


def dfs(x):
    print(x, end=" ")
    visited[x] = True

    for connect_vertex in graph[x]:
        if not visited[connect_vertex]:
            dfs(connect_vertex)


def bfs(x):
    que = deque()
    que.append(x)
    visited[x] = True

    while que:
        x = que.popleft()
        print(x, end=" ")

        for connect_vertex in graph[x]:
            if not visited[connect_vertex]:
                visited[connect_vertex] = True
                que.append(connect_vertex)


if __name__ == "__main__":
    vertex_cnt, edge_cnt, start_num = map(int, input().split())
    graph = [[] for _ in range(vertex_cnt + 1)]
    for _ in range(edge_cnt):
        # * 양방향 그래프이기 떄문에 서로의 정점에 간선을 추가해준다.
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # * 방문할 수 있는 정점이 여러개인 경우, 작은 번호부터 방문하기 위해서 만들어준 리스트를 오름차순으로 미리 정렬 해둔다.
    for connect_list in graph:
        connect_list.sort()
    # * dfs, bfs 탐색에 사용할 visited 배열을 각각 만들어주는것도 좋지만, 하나의 visited 배열로 탐색이 끝나면 다시 visited 배열을 모두 False로 다시 초기화 해주면 메모리 사용을 더 줄일수 있다.
    visited = [False] * (vertex_cnt + 1)
    dfs(start_num)
    visited = [False] * (vertex_cnt + 1)
    print()
    bfs(start_num)
