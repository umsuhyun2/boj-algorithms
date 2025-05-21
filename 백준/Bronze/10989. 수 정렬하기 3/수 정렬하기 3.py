import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
count = [0] * 10001

for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    for _ in range(count[i]):
        write(str(i) + '\n')