import sys
input = sys.stdin.readline

def merge_sort(arr):
    n = len(arr)
    temp = [0] * n
    count = 0
    size = 1

    while size < n:
        for start in range(0, n, size * 2):
            mid = min(start + size, n)
            end = min(start + size * 2, n)

            i, j = start, mid
            k = start

            while i < mid and j < end:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    count += mid - i  # 역순 쌍 수 만큼 더해줌
                    j += 1
                k += 1

            while i < mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j < end:
                temp[k] = arr[j]
                j += 1
                k += 1

        arr, temp = temp, arr
        size *= 2

    return count

# 입력
n = int(input())
arr = list(map(int, input().split()))

# 결과 출력
print(merge_sort(arr))
