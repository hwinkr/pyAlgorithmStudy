# -*- coding: utf-8 -*-

def solution(numbers, target):
    
    from collections import deque

    answer = 0
    count = 0 #*  +,- 연산을 할때마다 올라가는 수
    index = 0 #*  numbers를 가리키는 수
    numbers_len = len(numbers)

    queue = deque()
    queue.append(0) # 처음에 0을 넣고 시작한 후 numbers의 수를 bfs를 통해 계속 +,-해준다
    
    for i in range(2**numbers_len-1): # numbers의 마지막 수가 
        v = queue.popleft()
        
        for x in (v+numbers[index], v-numbers[index]):
            queue.append(x)
            
        count += 1
        if (2**(index+1)-1) == count: #* index값을 늘려야 할 때 ex)1,3,7,15...
            index += 1
    
    for i in queue: #* 마지막남은 queue랑 target이랑 비교해서 같으면 answer += 1
        if i == target:
            answer += 1
    
    return answer


numbers = [1,1,1,1,1]
target = 3

print(solution(numbers, target))