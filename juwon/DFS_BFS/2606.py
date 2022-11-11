# n = int(input())
# pair_num = int(input())

# pair_li = list()

# for _ in range(pair_num):
#     pair = list(map(int, input().split()))
#     pair_li.append(pair)

# for i in range(pair_num):
#     pair_li[i].sort()

# pair_li.sort()
# # print(pair_li)
# result_li = list()
# result_li.append(1)

# for j in pair_li:
#     if j[0] in result_li:
#         # print(j,"if")
#         result_li.append(j[1])
# # print(result_li)
# result_li = list(set(result_li))

# print(len(result_li) - 1)

#Todo 위의 코드로 했는데 오류가 나서 아래 코드로 바꿨다(가져왔다)


n = int(input()) # 컴퓨터 개수
v = int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화
visited = [0]*(n+1) # 방문한 컴퓨터인지 표시

for i in range(v): # 그래프 생성
    a,b = map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
    
def dfs(v):
    visited[v] = 1 # 방문했음을 체크
    for nx in graph[v]: # graph[v]안에 수가
        if visited[nx] == 0: # 방문하지 않으면 
            dfs(nx) # 그 수에대한 dfs함수 실행
dfs(1)

print(sum(visited) - 1)
