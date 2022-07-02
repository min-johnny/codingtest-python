n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵 생성 및 초기화
d = [[0] * m for _ in range(n)]
# 현재 위치 방문 처리
d[x][y] = 1

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    # 함수 내에서 전역변수인 direction 사용 명시
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 정면에 가보지 않은 칸이 있다면
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 방문 처리
        d[nx][ny] = 1
        x, y = nx, ny
        turn_time = 0
        count += 1
        continue
    # 정면에 가보지 않은 칸이 없거나 바다라면
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없다면
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        # 없다면 이동 중지
        else:
            break

print(count)
