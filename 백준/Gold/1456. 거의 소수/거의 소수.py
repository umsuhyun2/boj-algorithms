import math
import sys
input = sys.stdin.readline

L, R = map(int, input().split())

max_limit = int(math.sqrt(R)) + 1
prime = [True] * (max_limit + 1)
prime[0] = False
prime[1] = False

for i in range(2, int(max_limit**0.5) + 1):
    if prime[i]:
        for j in range(i*i, max_limit+1, i):
            prime[j] = False

result = 0
for p in range(2, max_limit+1):
    if prime[p]:
        power = p * p
        while power <= R:
            if power >= L:
                result += 1
            power *= p

print(result)
