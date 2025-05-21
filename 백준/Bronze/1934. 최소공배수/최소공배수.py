import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    g = gcd(A, B)
    print(A * B // g)
