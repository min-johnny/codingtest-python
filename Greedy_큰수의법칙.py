# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 오름차순으로 정렬
first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 횟수
count = m//(k+1)*k+m % (k+1)

result = 0
result += first*count
result += second*(m-count)

print(result)
