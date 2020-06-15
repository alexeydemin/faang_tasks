from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = {0: 0, 1: 0, 2: 0}
        for a in nums:
            n[a] += 1
        for i, _ in enumerate(nums):
            if i < n[0]:
                nums[i] = 0
            elif i >= n[1] + n[0]:
                nums[i] = 2
            else:
                nums[i] = 1
        return nums


print(Solution().sortColors([0, 0, 1, 1, 2, 2]))  # [2, 0, 2, 1, 1, 0]
