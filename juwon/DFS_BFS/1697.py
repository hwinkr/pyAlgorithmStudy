from collections import deque 

def bfs():
    queue = deque() 
    queue.append(N) # N을 큐에 넣고 
    
    while queue: # 큐가 없어질 동안
        v = queue.popleft() # pop한 것을 v에 저장하고
        
        if v == K: # K값과 같아지면 끝
            print(hide[v])
            break
        
        for i in (v-1, v+1, v*2): # i = v-1, v+1, v*2 값을 가지게 된다 (ex: 4 6 10)
            if 0 <= i <= MAX and not hide[i]: # hide값이 0이라면 실행
                hide[i] = hide[v] + 1 # 그 이전 hide값에 비해 1초가 늘어남(ex: 5-0초, 4,6,10-1초, 9,11,20-3초...)
                queue.append(i) # (ex: queue에 4,6,10값을 append)

MAX = 10 ** 5 # 시간초과가 나지 않도록?
hide = [0] * (MAX+1) # 얼마나 움직였는지 알기 위해

N, K = map(int, input().split())
bfs()