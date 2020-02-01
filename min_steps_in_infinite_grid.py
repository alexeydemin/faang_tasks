class Solution:
    def coverPoints(self, A, B):
        s = 0
        for i, a in enumerate(A):
            if i + 1 < len(A):
                s += max(abs(A[i + 1] - A[i]), abs(B[i + 1] - B[i]))
        return s


#r = Solution.coverPoints(None, [0, 1, 1], [0, 1, 2])
r = Solution.coverPoints(None, [1, 7, 7], [2, 8, 8])

print(r)
