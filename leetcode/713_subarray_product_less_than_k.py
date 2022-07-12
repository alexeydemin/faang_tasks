from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        res = 0
        for n in nums:
            if n < k:
                res += 1
        for i in range(ln):
            s = nums[i]
            for j in range(i + 1, ln):
                s = s * nums[j]
                if s < k:
                    res += 1
                    # print(s)
                else:
                    break
        return res


print(Solution.numSubarrayProductLessThanK(None, nums=[10, 5, 2, 6], k=100))  # 8
print(Solution.numSubarrayProductLessThanK(None, nums=[1, 1, 1], k=100))  # 6
print(Solution.numSubarrayProductLessThanK(None, nums=[1, 2, 3, 6], k=0))  # 0
