import sys
sys.setrecursionlimit(10000) # 백준에서 임의로 막아놓은 재귀함수의 최댓값(?)을 늘리기 위해

from collections import deque # bfs에서의 큐 사용

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)] # 그래프 초기화
visited_dfs=[False]*(n+1) # 방문한 정점인지 표시(dfs)
visited_bfs=[False]*(n+1) # 방문한 정점인지 표시(bfs)

for _ in range(m): # 그래프 생성
    a,b=map(int,input().split())
    graph[a].append(b) # a에 b 연결
    graph[b].append(a) # b에 a 연결 -> 양방향
    
for j in range(n + 1): # 2차원배열 안의 값들을 정렬
    graph[j].sort()    # 앞 번호부터 탐색하기위해


def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True # (처음)방문한 곳을 True로 바꾸고
    print(v, end=' ') # 출력한다
    
    for i in graph[v]: # v그래프 안에서
        if not visited_dfs[i]: # 방문하지 않은 곳이 있다면
            dfs(graph, i, visited_dfs) # 방문하지 않은 값에 대해 dfs함수를 실행한다


def bfs(graph, start, visited_bfs):
    queue = deque() # 큐 선언
    queue.append(start) # 처음 방문한 곳을 append하고
    visited_bfs[start] = True # True로 바꾼다
    
    while queue: # 큐 안에 값이 없어질 때 까지
        v = queue.popleft() # (편의상)가장 왼쪽을 값 v를 pop하고
        print(v, end=' ') # 출력한다
        
        for i in graph[v]: # v그래프 안에서
            if not visited_bfs[i]: # 방문하지 않은 곳이 있다면
                queue.append(i) # 큐에 append하고
                visited_bfs[i] = True # 방문했다고 바꾼다
                
            
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)