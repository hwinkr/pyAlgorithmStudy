n = int(input())
li = list()

for _ in range(n):
    time = list(map(int, input().split()))
    li.append(time)                 # 끝나는 시간이 빠른 순으로 정렬해야 가능한 많은 회의를 할 수 있음
                                    # 그러고 나서 시작하는 시간이 빠른 순으로 정렬     
li.sort(key=lambda x: (x[1], x[0])) # key=lambda 참고 
                                    # x[1]을 기준으로 먼저 오름차순 정렬후 x[0]을 기준으로 오름차순 정렬
count = 1
 
a = 0            
for i in range(1,n): # 1부터인 이유 ex) 1 1, 1 1, 1 2 같을때 총 회의시간은 3이지만 처음 1 1이중복이 되서 4가 출력됨
    if li[a][1] <= li[i][0]: # 전 회의의 끝나는 시간보다 다음 회의 시작하는 시간이 이르면 넘어감
        count = count + 1
        a = i
            
print(count)