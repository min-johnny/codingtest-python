input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1

steps = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
count = 0

for step in steps:
    r = row + step[0]
    c = column + step[1]
    if 8 >= r > 0 and 8 >= c > 0:
        count += 1

print(count)
