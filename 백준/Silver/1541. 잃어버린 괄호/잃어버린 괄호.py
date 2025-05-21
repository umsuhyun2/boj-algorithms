expr = input().strip()

# '-' 기준으로 나눔
parts = expr.split('-')

# 첫 번째 덩어리는 무조건 더하기
total = sum(map(int, parts[0].split('+')))

# 나머지는 괄호로 묶어서 다 빼기
for part in parts[1:]:
    total -= sum(map(int, part.split('+')))

print(total)