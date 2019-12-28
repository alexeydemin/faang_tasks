x = 0
y = 0

a = [
    # 0    1    2    3
    ["1", "2", "3", "4"],  # 0
    ["5", "6", "7", "8"],  # 1
    ["9", "1", "2", "3"],  # 2
    ["4", "5", "6", "7"],  # 3
    ["8", "9", "1", "0"],  # 4
]
a = [[0]]
_x = len(a[0])
_y = len(a)

is_square = 1
for length in range(1, min(_x - x, _y - y)):
    for i in range(0, length):
        print(i + x, length + y, a[length + y][i + x])
        is_square *= a[length + y][i + x]
    print('----')
    for i in range(0, length + 1):
        print(length + x, i + y, a[i + y][length + x])
        is_square *= a[i + y][length + x]
    print('=================')
