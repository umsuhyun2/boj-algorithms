import sys
input = sys.stdin.readline

# 이진 탐색 함수
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

# 입력 받기
n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
targets = list(map(int, input().split()))

# 각 수에 대해 이진 탐색 결과 출력
for t in targets:
    print(binary_search(a, t))
