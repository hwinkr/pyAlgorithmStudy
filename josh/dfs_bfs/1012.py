T = int(input())        # 테스트 케이스 입력
# 상하좌우 확인을 위해 dx, dy 생성
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# dfs 정의
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < N and 0 <= w < M and matrix[q][w] == 1:
                matrix[q][w] = 0
                queue.append([q, w])

# 행렬 만들기
for i in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for i in range(N)]
    cnt = 0
    # 배추 위치에 1 표시
    for j in range(K):
        a, b = map(int, input().split())
        matrix[b][a] = 1
    # 배추 그룹 수 세기
    for q in range(N):
        for w in range(M):
            if matrix[q][w] == 1:
                bfs(q, w)
                matrix[q][w] = 0
                cnt += 1
    print(cnt)