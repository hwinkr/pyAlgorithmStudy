f,s,g,u,d = map(int, input().split())
matrix = [0] * (f + 1) 

def bfs(start):
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n == g :
            return matrix[n]
        for c in (n-d, n+u):
            if 0<c<=f and not matrix[c] and c != start:
                matrix[c] = matrix[n]+1
                queue.append(c)
    return "use the stairs"

print(bfs(s))