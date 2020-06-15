from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        def go(s, e):
            m = (s + e) // 2
            if target == nums[m]:
                return m
            if m + 1 < len(nums) and nums[m] < target < nums[m + 1]:
                return m + 1
            if target > nums[m]:
                return go(m + 1, e)
            if target < nums[m]:
                return go(0, m - 1)

        return go(0, len(nums) - 1)


print(Solution().searchInsert([1, 3, 5, 6], 5))  # 2
print(Solution().searchInsert([1, 3, 5, 6], 2))  # 1
print(Solution().searchInsert([1, 3, 5, 6], 7))  # 4
print(Solution().searchInsert([1, 3, 5, 6], 0))  # 0
print(Solution().searchInsert([1, 3, 5, 6], 4))  # 2
