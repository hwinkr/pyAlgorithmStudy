N = int(input())
numbers = list(map(int, input().split()))
max_number = int(input())
numbers = sorted(numbers)

if sum(numbers) <= max_number:
    answer = max(numbers)

left = 0
right = numbers[-1]
answer = 0
while left <= right:
    mid = (left + right) // 2
    total = 0
    for number in numbers:
        if number <= mid:
            total += number
        else:                
            total += mid

    if total <= max_number:
            answer = max(answer, mid)
            left = mid + 1
    else:
            right = mid - 1

print(answer)