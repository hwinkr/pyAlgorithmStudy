N, M = map(int, input().split()) # N:나무의 수, M:나무의 길이
array = list(map(int, input().split())) # 주어진 개별 나무들의 길이

start = 0
end = max(array)

result = 0
while start <= end: #* 이분탐색
    total = 0
    mid = (start+end) // 2
        
    for x in array: # 잘랐을 때에 남은 나무의 길이 계산
        if x > mid:
            total += x - mid
    
    if total < M: # 나무 길이가 부족한 경우 (왼쪽부분 탐색)
        end = mid - 1
    else: # 나무길이가 충분한 경우 (오른쪽 부분 탐색)
        result = mid #* 최대한 덜 잘랐을 때가 정답이므로 여기서 result값 기록
        start = mid + 1

print(result)