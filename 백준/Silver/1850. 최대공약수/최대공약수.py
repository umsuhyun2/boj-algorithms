def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B = map(int, input().split())
g = gcd(A, B)
print('1' * g)
