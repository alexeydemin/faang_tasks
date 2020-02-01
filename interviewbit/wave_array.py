class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A = sorted(A)
        r = []
        for i in range(0, len(A), 2):
            if i+1 < len(A):
                r.append(A[i + 1])
            r.append(A[i])

        return r


#r = Solution.wave(None, [1, 2, 3, 4, 5, 6])
r = Solution.wave(None, [1])
# 214365
print(r)
