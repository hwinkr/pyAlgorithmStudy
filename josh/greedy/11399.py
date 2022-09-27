n = int(input())

time = list(map(int,input().split()))

time.sort()

count = 0
star = 0

for b in time:
    count = count + b
    star = star + count

    
print(star)