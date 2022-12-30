def dfs(i, n, computers, visited):
    visited[i] = 1
    for connect in range(n):
        if connect != i and computers[i][connect] and not visited[connect]:
            dfs(connect, n, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(i, n, computers, visited)
            answer += 1
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))