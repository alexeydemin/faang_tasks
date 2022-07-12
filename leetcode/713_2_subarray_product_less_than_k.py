from typing import List

# right - left + 1 - window size is equal to number of contiguous arrays
# e.g. [[[1]], [[2]]] = 3, [[[1] [[2]] [3]]] =

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


print(Solution.numSubarrayProductLessThanK(None, nums=[10, 5, 2, 6], k=100))  # 8
print(Solution.numSubarrayProductLessThanK(None, nums=[1, 1, 1], k=100))  # 6
print(Solution.numSubarrayProductLessThanK(None, nums=[1, 2, 3, 6], k=0))  # 0
