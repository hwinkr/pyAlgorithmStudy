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
    # * 공백이 없는 상태로 입력을 받는다면 rstrip 를 사용해야 한다. 이 함수는 문자열의 공백을 제거해준다
    graph = [list(map(int, input().rstrip())) for _ in range(n)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    group_cnt = 0
    house_cnt_list = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                # * 하나의 단지에 속하는 집을 발견하면 bfs 탐색을 시작해준다.
                # * 개인적인 생각 : dfs 는 재귀함수를 계속 호출하기 떄문에 return 값을 처리하기 힘들다, 탐색만 하는 경우가 아닌 함수가 어떤 값을 반환해줘야 하는 경우라면 bfs 를 사용하는 것이 더 편함
                group_cnt += 1
                house_cnt_list.append(bfs(i, j))

    house_cnt_list.sort()
    print(group_cnt)
    for house_cnt in house_cnt_list:
        print(house_cnt)
