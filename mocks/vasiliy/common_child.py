# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string.
# Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
#
# For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD.
# They can be formed by eliminating either the D or C from both strings.
# Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD != ABDC.

def commonChild(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    arr = [[0 for i in range(l1)] for i in range(l2)]

    # cnt = 0
    for i, a in enumerate(s1):
        for j, b in enumerate(s2):
            if i == 0 and j == 0:
                if a == b:
                    arr[i][j] = 1
            else:
                continue
            if i == 0 and j != 0:
                if a == b:
                    arr[i][j] = 1
            else:
                arr[i][j] = arr[i][j - 1]
            if i != 0 and j == 0:
                if a == b:
                    arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j]
            if i != 0 and j != 0:
                if a == b:
                    arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
    return arr[l1 - 1][l2 - 1]

print(commonChild("harry", "sally"))
print("correct: 2")  # ay
print(commonChild("SHINCHAN", "NOHARAAA"))
print("correct: 3")  # NHA
print(commonChild("AB", "AA"))  # A
print("correct: 1")

# harry
# sally

#   A B C
# A 1 1
# A 1 1
# C     2

#   H A R R Y    S A L L Y
# S 0 0 0 0 0  H 0 0 0 0 0
# A 0 1        A 0 1 1
# L            R
# L            R
# Y            Y

# https://www.hackerrank.com/challenges/common-child/problem
# https://www.geeksforgeeks.org/longest-common-substring-dp-29/
