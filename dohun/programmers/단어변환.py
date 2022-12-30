answer = 50

def diff(a, b):
    count = 0
    for a_c, b_c in zip(a, b):
        if a_c != b_c:
            count += 1
    return count


def dfs(target, words, i, visited, count, stack):
    if target == words[i]:
        global answer
        answer = min(answer, len(stack))
        return

    for j in range(len(words)):
        if i != j and not visited[j] and diff(words[i], words[j]) == 1:
            visited[i] = 1
            dfs(target, words, j, visited, count + 1, stack + [words[j]])
            visited[i] = 0

def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]

    if target not in words:
        return 0

    for i in range(len(words)):
        if diff(begin, words[i]) == 1:
            visited[i] = 1
            dfs(target, words, i, visited, 0, [words[i]])
            visited[i] = 0

    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))