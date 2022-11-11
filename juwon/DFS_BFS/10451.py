def dfs(v):
    visited[v] = 1
    next = permutation[v] # 다음에 방문할 위치
    
    if not visited[next]: # if visited[next] == 0 이랑 같은 문장
        dfs(next)


T = int(input())

for _ in range(T):
    
    N = int(input())
    permutation = [0] + list(map(int, input().split())) # 앞에 '[0] +'를 해줘야 편한 계산 가능
    visited = [0]*(N+1)

    result = 0
    for i in range(1,N+1): # 차례대로 방문안한곳 방문
        if visited[i] == 0:
            dfs(i)
            result += 1 # 한번 망문이 끝나면 result에 +1
            
    print(result)

    
    