class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        ans = []
        subarray = []
        sm = 0
        mx = 0
        for i in A:
            if i >= 0:
                subarray.append(i)
                sm += i
                if sm > mx:
                    mx = sm
                    ans = subarray
                if sm == mx and len(ans) < len(subarray):
                    ans = subarray
            else:
                subarray = []
                sm = 0

        return ans


r = Solution.maxset(None, [0, 0, -1, 0])
# r = Solution.maxset(None, [1, 2, 5, -7, 2, 3])
print(r)
