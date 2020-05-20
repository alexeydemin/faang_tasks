from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        j = 0
        i = 0
        while i + 1 < len(nums):
            if j:
                del nums[i]
                i -= 1

            if nums[i] == nums[i + 1]:
                j += 1
            else:
                j = 0
            i += 1

        n = len(nums) - 1
        if n and nums[n] == nums[n - 1]:
            del nums[n]
        return nums

#                                    0  1  2  3  4  5  6  7  8  9
# r = Solution.removeDuplicates(None, [0, 0, 1, 1, 1,1, 1,1,1, 2, 2, 3, 3, 4])
r = Solution.removeDuplicates(None, [1, 1, 2, 2, 2, 2, 2])
print(r)

# AN EASY SOLUTION
# i = 0
# while i < len(nums) - 1:
#     if nums[i] == nums[i + 1]:
#         del nums[i]
#     else:
#         i += 1
# return len(nums)
