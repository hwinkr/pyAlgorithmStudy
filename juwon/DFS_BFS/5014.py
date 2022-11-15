from collections import deque # bfs에서의 큐 사용

def bfs():
    queue = deque()
    queue.append(S)
    visited[S] = 0
    
    while queue:
        v = queue.popleft()
        
        if v == G:
            return visited[v]

        for i in (v+U, v-D):
            if 0 < i <= F and visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)
                
    return "use the stairs"
                
F, S, G, U, D = map(int, input().split())
visited = [-1] * (F + 1)

print(bfs())

#? visited를 -1이 아닌 0으로 초기화하면 66%까지 가다가 틀린 코드가 된다 왜일까??
#? 39번째 줄에 visited[S]를 1로 바꾸고 마지막 elif프린트에서 1을 빼주면 된다고 한다
#! 내 코드의반례?  ) 10 10 1 0 1
#* 0으로 초기화 하면 위의 반례를 실행했을때 i값이 v+U가 먼저 나오는데 그때의 i값은 10이다
#* 10층은 if문에 만족하니 visited[10]이 1이된다
#* 10층에서 10층을 가는데 버튼을 1번 눌러야되는 오류가 발생한 것이다
#* 한층씩 +1값이 누적되어서 나오기때문에
#* 결과적으로 답인 9가 출력되지 않고 10이 출력된다
from collections import deque # bfs에서의 큐 사용

# def bfs():
#     queue = deque()
#     queue.append(S)
    
#     while queue:
#         v = queue.popleft()

#         for i in (v+U, v-D):
#             if 0 < i <= F and not visited[i]:
#                 visited[i] = visited[v] + 1
#                 queue.append(i)
                
# F, S, G, U, D = map(int, input().split())
# visited = [0] * (F + 1)
# bfs()

# if S == G:
#     print(0)
# elif visited[G] > 0:
#     print(visited[G])
# else:
#     print("use the stairs")
    
    
#! visited를 0으로 초기화해도 맞는 코드    
# from collections import deque # bfs에서의 큐 사용

# def bfs():
#     queue = deque()
#     queue.append(S)
#     visited[S] = 1
    
#     while queue:
#         v = queue.popleft()

#         for i in (v+U, v-D):
#             if 0 < i <= F and not visited[i]:
#                 visited[i] = visited[v] + 1
#                 queue.append(i)
                
# F, S, G, U, D = map(int, input().split())
# visited = [0] * (F + 1)
# bfs()

# if S == G:
#     print(0)
# elif visited[G] > 0:
#     print(visited[G]-1)
# else:
#     print("use the stairs")