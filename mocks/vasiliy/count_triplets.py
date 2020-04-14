# You are given an array and you need to find number of tripets of indices
#   such that the elements at those indices are in geometric progression for a
#  given common ratio  and i < j < k.
# Complete the countTriplets function in the editor below. It should return the
#  number of triplets forming a geometric progression for a given  as an
#  integer.
# countTriplets has the following parameter(s):
# arr: an array of integers
# r: an integer, the common ratio
# Return the count of triplets that form a geometric progression.

# r = 2
# arr = [1, 1, 2]  # 2
#
# S
# T
# step1: {1: 1}, {}
# step2: {1: 2}, {}
# step3: {1: 2, 2: 1}, {2: 2}
#
# arr = [1, 2, 2, 4, 1, 2, 4]  # 6
# [1, 2, 4]
# [1, 2, 4]
# [1, 2, 4]
# [1, 2, 4]
# [1, 2, 4]
# [1, 2, 4]
#
# n = len(arr)
#
# 3
# 9
# 27
# 1
# 4
# 16


def countTriplets(arr, r):
    dic_singles = {}
    dic_tuples = {}
    count = 0

    for a in arr:

        t = a // r

        if t in dic_tuples:
            count += 1

        if t in dic_singles:
            dic_tuples[a] = dic_singles[t]

        if a in dic_singles:
            dic_singles[a] += 1
        else:
            dic_singles[a] = 1

        return count