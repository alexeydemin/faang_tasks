from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int):
        n = len(nums)
       
        for i in range(n):
            print(nums[i])
        return 00
            


print(Solution.numberOfSubarrays(None, nums=[1, 1, 2, 1, 1], k=3))  # 2
# print(Solution.numberOfSubarrays(None, nums=[2, 4, 6], k=1))  # 0
# print(Solution.numberOfSubarrays(None, nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))  # 16
