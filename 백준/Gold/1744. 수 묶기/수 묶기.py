import sys

input = sys.stdin.readline

n = int(input())
plus = []
minus = []
one = 0
zero = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num == 1:
        one += 1
    elif num == 0:
        zero += 1
    else:
        minus.append(num)

# 양수는 큰 수부터 곱해야 이득
plus.sort(reverse=True)

# 음수는 작은 수부터 곱해야 이득 (ex. -5 * -4 = 20)
minus.sort()

result = 0

# 양수 처리
for i in range(0, len(plus), 2):
    if i + 1 < len(plus):
        result += plus[i] * plus[i + 1]
    else:
        result += plus[i]

# 음수 처리
for i in range(0, len(minus), 2):
    if i + 1 < len(minus):
        result += minus[i] * minus[i + 1]
    else:
        if zero > 0:
            zero -= 1  # 0과 곱해서 없앰
        else:
            result += minus[i]

# 1은 더함
result += one

print(result)
