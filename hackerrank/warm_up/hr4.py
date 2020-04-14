aa = [[1, 2, 3],
      [4, 5, 6],
      [9, 8, 9]]


def solve(a):
    res = [0, 0]
    for i, line in enumerate(a):
        for j, num in enumerate(line):
            if i == j:
                res[0] += num
            if i == len(line) - j - 1:
                res[1] += num
    return abs(res[0] - res[1])


print (solve(aa))