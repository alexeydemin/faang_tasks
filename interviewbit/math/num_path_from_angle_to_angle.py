class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    #
    k = 0

    def uniquePaths(self, A, B):
        Solution.getNum(self, (0, 0), (A - 1, B - 1))
        return Solution.k

    def getNum(self, cur, end, s=0):
        # print(cur, s)

        if cur[0] == end[0] and cur[1] == end[1]:
            Solution.k += 1
            # print ('return', Solution.k)

        if cur[0] < end[0]:
            Solution.getNum(self, (cur[0] + 1, cur[1]), end)
        if cur[1] < end[1]:
            Solution.getNum(self, (cur[0], cur[1] + 1), end)


r = Solution.uniquePaths(None, 15, 9)
print(r)
