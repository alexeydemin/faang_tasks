def commonChild(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    arr = [[0 for i in range(l1)] for i in range(l2)]

    cnt = 0
    for i, a in enumerate(s1):
        for j, b in enumerate(s2):
            arr[i][j] = cnt
            if a == b:
                arr[i][j] += 1

    max = float('-inf')

    for line in enumerate(arr):
        for el in line:
            if el > max:
                max = el
    return max

print(commonChild("harry", "sally"))
print("correct: 2")  # ay
print(commonChild("SHINCHAN", "NOHARAAA"))
print("correct: 3")  # NHA
print(commonChild("AB", "AA"))  # A
print("correct: 1")
