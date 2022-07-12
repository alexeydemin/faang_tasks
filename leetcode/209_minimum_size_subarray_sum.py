from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = sum = 0
        ans = float('inf')
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                # print(left)
                ans = min(ans, r - left + 1)
                sum -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans


print(Solution.minSubArrayLen(None, target=7, nums=[2, 3, 1, 2, 4, 3]))  # 2: [4,3]
print(Solution.minSubArrayLen(None, target=4, nums=[1, 4, 4]))  # 1
print(Solution.minSubArrayLen(None, target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))  # 0
