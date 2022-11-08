def dfs(x, y): # 08번과 거의 동일한 dfs함수
    if x <= -1 or x >= T or y <= -1 or y >= T:
        return False
    
    if graph[x][y] == 1: 
        graph[x][y] = index # graph안의 수를 한번의 dfs를 다 돌면 바꿈
        dfs(x-1, y) 
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True 
    
    return False

T = int(input())

graph = [] # 그래프 초기화

for i in range(T): # 그래프 입력
    graph.append(list(map(int, input())))
    
result = 0 # 총 단지수의 개수
index = 2 # 그래프에서 dfs 다 돌면 그래프의 1값을 새로운(+1)index값으로 바꿈
for i in range(T):
    for j in range(T):
        if dfs(i, j) == True:
            result += 1
            index += 1 
            
print(result) # 총 단지수의 개수
# print(graph)

index_count = 2 # 그래프 안에서 단지의 숫자와 비교할 정수
num_list = [] # 단지내 집의 수를 저장할 리스트

for num_count in range(result): 
    num = 0 # 단지가 바뀔 때 마다 0으로 초기화
    for n in range(T):
        for m in range(T):
            if graph[n][m] == index_count:
                num += 1
    num_list.append(num)
    index_count += 1

num_list.sort() # 오름차순으로 정렬

for a in range(result):
    print(num_list[a])