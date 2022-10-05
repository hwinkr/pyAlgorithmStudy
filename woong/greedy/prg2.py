def solution(name):
    answer = 0
    move_min = len(name) - 1
    cnt_lst = [min(abs(ord('A') - ord(i)), abs(ord('Z') + 1 - ord(i)))
               for i in name]
    answer += sum(cnt_lst)

    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        move_min = min(move_min, 2 * i + len(name) -
                       next, 2 * (len(name) - next) + i)
    return answer + move_min
