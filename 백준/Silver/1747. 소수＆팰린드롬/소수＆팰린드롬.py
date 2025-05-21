import sys
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

N = int(input())

num = N
while True:
    if is_palindrome(num) and is_prime(num):
        print(num)
        break
    num += 1
