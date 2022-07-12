from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, val in enumerate(nums):
            start, end = i + 1, len(nums) - 1
            while start < end:
                sum = val + nums[start] + nums[end]
                if sum == 0:
                    if [val, nums[start], nums[end]] not in res:
                        res.append([val, nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif sum < 0:
                    start += 1
                elif sum > 0:
                    end -= 1
        return res


print(Solution.threeSum(None, nums=[-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
# -4, -1, -1, 0, 1, 2
