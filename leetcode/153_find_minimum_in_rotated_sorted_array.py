from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # def bs(nums, start, end):
        #     mid = (start + end) // 2
        #     # if mid == 0:
        #     #     return min(nums[0], nums[1])
        #     if nums[mid - 1] > nums[mid]:
        #         return nums[mid]
        #     elif nums[0] < nums[mid]:
        #         # we are on the left side
        #         return bs(nums, mid + 1, end)  # looking on the right
        #
        #     else:
        #         # we are on the right side
        #         return bs(nums, start-1, mid)  # looking on the left
        #
        # # if len(nums) == 1:
        # #     return nums[0]
        # if len(nums) == 2:
        #     return min(nums)
        # if nums[0] < nums[-1]:
        #     return nums[0]
        # return bs(nums, 0, len(nums) - 1)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


print(Solution.findMin(None, [4, 5, 6, 7, 8, 9, 0, 1, 2]))
print(Solution.findMin(None, [8, 9, 0, 1, 2, 3, 4, 5, 6, 7]))
print(Solution.findMin(None, [1, 2, 4, 5, 6, 7, 0]))
print(Solution.findMin(None, [4, 5, 6, 7, 0, 1, 2, 3]))
print(Solution.findMin(None, [0, 1, 2, 4, 5, 6, 7]))

print(Solution.findMin(None, nums=[3, 4, 5, 1, 2]))  # 1
print(Solution.findMin(None, [11, 13, 15, 17]))  # 11
print(Solution.findMin(None, [33]))  # 11
print(Solution.findMin(None, [1, 2]))  # 11
print(Solution.findMin(None, [2, 1]))  # 11
print(Solution.findMin(None, [5, 1, 2, 3, 4]))  # 11
