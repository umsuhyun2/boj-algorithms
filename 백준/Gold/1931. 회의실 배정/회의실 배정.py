def sort_key(meeting):
    return (meeting[1], meeting[0])  # 끝나는 시간 기준, 같으면 시작 시간 기준

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=sort_key)

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)