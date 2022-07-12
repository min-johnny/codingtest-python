n, m = map(int, input().split())
array = list(map(int, input().split()))

# 이진탐색을 위한 시작과 끝 지정
start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        # 잘랐을 때의 떡 길이 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 자르기(왼쪽 탐색)
    # m 보다는 무조건 크거나 같아야 함!
    if total < m:
        end = mid - 1
    # 떡의 양이 많을 경우 덜 자르기(오른쪽 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록
        start = mid + 1

print(result)
