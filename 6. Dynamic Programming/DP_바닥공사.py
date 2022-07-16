n = int(input())

d = [0] * 1001

# 다이나믹 프로그래밍(bottom up)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2] * 2
    # (i - 1 뒤에  2x1 덮개) + (i - 2 뒤에 1x2 덮개 두 개 & 2x2 덮개)

print(d[n] % 796796)