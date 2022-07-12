from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # for i, n in enumerate(nums):
        #     if i - 1 < 0 and nums[i] > nums[i + 1]\
        #             or i + 1 > len(nums) - 1 and nums[i - 1] < nums[i]\
        #             or i - 1 >= 0 and nums[i - 1] < nums[i] > nums[i + 1] and i + 1 <= len(nums) - 1:
        #         return i

        # l, r = nums[0], nums[-1]
        # while l < r:
        #     mid = (l + r) // 2
        #     if (mid + 1) < len(nums) and nums[mid] < nums[mid + 1]:
        #         l = mid + 1
        #     else:
        #         r = mid
        # return l
        if len(nums) == 1:
            return 0

        def peak(nums, start, stop):
            m = (start + stop) // 2
            if (m - 1 < 0 and nums[m] > nums[m + 1]) or (m + 1 > len(nums) - 1 and nums[m - 1] < nums[m]) or nums[
                m - 1] < nums[m] > nums[m + 1]:
                return m
            elif m - 1 >= 0 and nums[m - 1] > nums[m]:
                # print('a')
                return peak(nums, start, m - 1)
            elif m + 1 <= len(nums) - 1 and nums[m] < nums[m + 1]:
                # print('b')
                return peak(nums, m + 1, stop)

        return peak(nums, 0, len(nums) - 1)


print(Solution.findPeakElement(None, [1, 2, 3, 1]))  # 2
print(Solution.findPeakElement(None, [1, 2, 1, 3, 5, 6, 4]))  # 5
print(Solution.findPeakElement(None, [1]))  # 0
print(Solution.findPeakElement(None, [1, 2]))  # 1
print(Solution.findPeakElement(None, [2, 1]))  # 0
