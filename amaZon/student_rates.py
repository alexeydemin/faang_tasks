def findImbalance(rank):
    if len(rank) == 1:
        return 0
    if len(rank) == 2:
        return 1 if abs(rank[0] - rank[1]) > 1 else 0

    rank.sort()
    res = 0

    def count_imb(r):
        cnt = 0
        for i in range(1, len(r)):
            if r[i] - r[i - 1] > 1:
                cnt += 1
        return cnt

    for group_len in range(2, len(rank) + 1):
        i = 0
        while group_len + i <= len(rank):
            res += count_imb(rank[i:group_len + i])
            i += 1

    return res


print(findImbalance([7, 1, 3, 2]))
print(findImbalance([4, 4, 1, 3, 2]))
print(findImbalance([15, 34, 18, 9, 54, 3, 6]))
print(findImbalance([2, 1, 2]))

# [1 2 3 5]
# 3 5
# 2 3 5
# 1 2 3 5
# = 3
