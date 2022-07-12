# 이진 탐색 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# N 입력
n = int(input())
array = list(map(int, input().split()))
# 이진 탐색 위해 정렬
array.sort()
# M 입력
m = int(input())
x = list(map(int, input().split()))



for i in x:
    result = binary_search(array, i, 0, n - 1)
    if  result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')