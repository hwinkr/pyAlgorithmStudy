import sys # 시간초과 해결
input = sys.stdin.readline

N, M = map(int, input().split()) # N:학생 수 M:보석 색상의 수

array = list() # 각각의 보석의 개수들
for i in range(M):
    jewel = int(input())
    array.append(jewel)

start = 1 #* start가 0부터 시작하면 zerodivision 에러가 발생
end = max(array)

result = 0
while start <= end: #* 이분 탐색
    total = 0
    mid = (start+end) // 2
    
    for x in array: # 중간값으로 쪼갰을 때 나오는 값 계산
        if x % mid == 0:
            total += x // mid
        else:
            total += x // mid + 1
        
    if total <= N: # 더 쪼갤 수 있는 경우 (왼쪽 부분 탐색)
        result = mid #* 최대한 많이 쪼개야 정답이므로 여기서 result값 기록
        end = mid - 1
    else: # 충분히 쪼갠 경우 (오른쪽 부분 탐색)
        start = mid + 1
    
print(result)