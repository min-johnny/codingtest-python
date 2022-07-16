n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

# 다이나믹 프로그래밍(bottom up)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:        # d[j - array[i]]가 10001이더라도 아래의 min 함수는 항상 d[j]의 값을 반환하기에 없어도 됨
            d[j] = min(d[j - array[i]] + 1, d[j])

if d[m] == 10001:
    print(-1)
else:
    print(d[m])