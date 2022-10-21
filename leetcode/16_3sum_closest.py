from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < abs(res - target):
                    res = sum
                if sum > target:
                    right -= 1
                else:
                    left += 1
        return res


#             0 [1] 2 3 4 5 [6], tg=5
#             0 1 1 1

# print(Solution.threeSumClosest(None, [-1, 2, 1, -4], 1)) #2
print(Solution.threeSumClosest(None, [1, 1, 1, 0], -100))  # 2
