class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        s = 0
        for i, a in enumerate(A):
            for b in A[i + 1:]:
                s += Solution.f(None, a, b)
        return 2 * s

    def f(self, x, y):
        ans = 0
        for i in range(31, -1, -1):
            b1 = x >> i & 1
            b2 = y >> i & 1
            ans += not (b1 == b2)
        return ans


A = [2, 4, 6]
#A = [1, 2, 3, 4, 5]
r = Solution.hammingDistance(None, A)
print(r)
