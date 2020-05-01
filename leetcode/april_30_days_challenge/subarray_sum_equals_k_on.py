from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k):
        prevSum = {}
        res = 0
        currsum = 0
        for i in range(0, len(nums)):
            currsum += nums[i]
            if currsum == k:
                res += 1
            if (currsum - k) in prevSum:
                res += prevSum[currsum - k]
            if currsum not in prevSum:
                prevSum[currsum] = 0
            prevSum[currsum] += 1
        return res

r = Solution.subarraySum(None, [7, 5, 3, 8, 1], 8)
print(r)