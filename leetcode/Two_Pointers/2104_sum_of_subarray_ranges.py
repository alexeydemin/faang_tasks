from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            mx = mn = nums[i]
            for j in range(i, n):
                mx = max(mx, nums[j])
                mn = min(mn, nums[j])
                res += mx - mn
        return res


# print(Solution.subArrayRanges(None, nums = [1,3,3]))
print(Solution.subArrayRanges(None, nums=[4, -2, -3, 4, 1]))
