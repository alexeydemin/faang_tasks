from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sep = self.find_gap(nums, 0, len(nums) - 1)
        if not sep:
            sep = 0
        arr = nums[sep:] + nums[:sep]
        pos = self.find(arr, target, 0, len(nums) - 1)
        # print(sep, pos)

        if pos == -1:
            return pos

        len1 = sep
        len2 = len(nums) - len1

        if pos >= len2:
            res = pos - len2
        else:
            res = pos + len1
        return res

    def find(self, nums, target, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        if target < nums[middle]:
            return self.find(nums, target, start, middle - 1)
        if target > nums[middle]:
            return self.find(nums, target, middle + 1, end)

    def find_gap(self, nums, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if nums[middle - 1] > nums[middle]:
            return middle
        if nums[middle] < nums[len(nums) - 1]:
            return self.find_gap(nums, start, middle - 1)
        if nums[middle] > nums[len(nums) - 1]:
            return self.find_gap(nums, middle + 1, end)


s = Solution()
# print(s.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
# 0  1   2   3  4  5
# print(s.search([12, 20, 60, 5, 8, 9], 60))  # 2
# print(s.search([12, 20, 60, 5, 8, 9], 12))  # 0
# print(s.search([12, 20, 60, 5, 8, 9], 8))  # 4
print(s.search([12, 20, 60, 5, 8, 9], 9))  # 5
#print(s.search([3, 5, 1], 3))  # 0
