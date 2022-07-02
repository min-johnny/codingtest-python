n, k = map(int, input().split())
result = 0

while True:
    # N이 K의 배수가 될 때까지 빼기
    target = (n // k) * k
    result += (n-target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) break
    if n < k:
        break
    n //= k
    result += 1

result += (n-1)
print(result)
