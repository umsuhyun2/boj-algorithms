import sys
input = sys.stdin.readline

def can_divide(capacity):
    count = 1  # 블루레이 개수
    current_sum = 0
    for length in lessons:
        if current_sum + length <= capacity:
            current_sum += length
        else:
            count += 1
            current_sum = length
    return count <= M

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

left = max(lessons)  # 최소 블루레이 크기
right = sum(lessons)  # 최대 블루레이 크기

result = right
while left <= right:
    mid = (left + right) // 2
    if can_divide(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
