import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
print(arr[k-1])  # 인덱스는 0부터 시작하므로 k-1번째
