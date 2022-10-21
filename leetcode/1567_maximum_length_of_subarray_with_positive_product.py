from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        mx = 0
        first_negative_i = current_negative_i = None
        negative_cnt = null_cnt = 0

        cnt = 0
        if nums[0] == 0:
            del nums[0]
        if nums[-1] == 0:
            del nums[-1]

        n = len(nums)
        for i in range(n):
            cnt += 1
            if nums[i] < 0:
                first_negative_i = first_negative_i if first_negative_i is not None else i
                current_negative_i = i
                negative_cnt += 1
            if nums[i] == 0:
                local_mx = cnt - 1 if negative_cnt % 2 == 0 or current_negative_i is None else cnt - min(
                    cnt - 1 - current_negative_i, first_negative_i) - 2
                mx = max(mx, local_mx)
                first_negative_i = current_negative_i = None
                negative_cnt = 0
                cnt = 0
                null_cnt += 1
        if null_cnt == 0:
            local_mx = n if negative_cnt % 2 == 0 or current_negative_i is None else n - min(n - 1 - current_negative_i,
                                                                                             first_negative_i) - 1
            mx = max(mx, local_mx)
        return mx


# [1, -2, 1, -3, 8 - 4], -5, 0, 3, 5, -1, -2


# print(Solution.getMaxLen(None, nums=[-1, 1, -2, 1, -3, 8, - 4, -5, ]))  # 7
# print(Solution.getMaxLen(None, nums=[1, -2, 1, -3, 8, - 4, -5, 0, 3, 5, -1, -2]))  # 7
# print(Solution.getMaxLen(None, nums=[1, -2, -3, 4]))  # 4
# print(Solution.getMaxLen(None, nums=[0, 1, -2, -3, -4]))  # 3
# print(Solution.getMaxLen(None, nums=[-1, -2, -3, 0, 1]))  # 2
# print(Solution.getMaxLen(None, nums=[1, 2, 3, 5, -6, 4, 0, 10]))  # 4
print(Solution.getMaxLen(None, nums=[1, 2, 3, 5, 6, 4, 0, 10]))  # 8
