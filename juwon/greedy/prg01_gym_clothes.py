#체육복
def solution(n, lost, reserve):
    
    answer = n - len(lost) # 먼저 전체학생에서 lost학생수를 빼고 빌려줄 수 있는 경우에 +1씩 해줬다
    
    lost.sort()  # n = 5, lost = [4, 2], reserve = [5, 3] 인 경우도 있기 때문에 정렬을 해주어야 한다 
    
    for i in lost[:]: # 처음에 for i in lost: 라고 써서 틀렸다. for문에서 remove를 할 때 조심해야한다는걸 알았다
        if i in reserve:                       # https://devpouch.tistory.com/110 참고
            answer += 1
            reserve.remove(i)       # 여분 체육복이 있는데 잃어버렸을 때인 경우를 제외하는 경우다
            lost.remove(i)          # 이런 사람이 있다면 각 배열에서 지운 후 answer에 +1했다
            
    for j in lost[:]:               # 앞뒤에 빌려줄 사람이 있다면 빌려오고 +1 한 후
        if j - 1 in reserve:        # 빌려준 사람을 reserve리스트에서 제외한다
            answer += 1             
            reserve.remove(j-1)
        elif j + 1 in reserve:
            answer += 1
            reserve.remove(j+1)
        
    return answer

    # for j in lost[:]:
    #     for x in (j-1, j+1):
    #         if x in reserve:
    #             answer += 1
    #             reserve.remove(x)
    # 14번째 줄을 이렇게 바꿀 수 있다고 함 