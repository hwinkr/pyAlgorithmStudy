K, N = map(int, input().split()) # K:가지고있는 랜선의 개수, N:필요한 랜선의 개수

array = list() # 이미 가지고 있는 랜선의 길이들
for i in range(K):
    string = int(input())
    array.append(string)
    
start = 1 #* start가 0부터 시작하면 zerodivision 에러가 발생
end = max(array)

result = 0
while start <= end: #* 이분 탐색
    total = 0
    mid = (start+end) // 2
    
    for x in array: # 중간값으로 잘랐을 때 나오는 개수 계산
        total += x // mid
    
    if total < N: # 랜선의 개수가 부족한 경우 (왼쪽 부분 탐색)
        end = mid - 1
    else: # 랜선의 개수가 충분한 경우 (오른쪽 부분 탐색)
        result = mid #* 최대한 덜 잘랐을때가 정답이므로 여기서 result값 기록
        start = mid + 1
    
print(result)