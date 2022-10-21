from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        mx = pos = neg = 0
        for num in nums:
            if num == 0:
                pos = neg = 0
            elif num > 0:
                pos += 1
                neg = 0 if neg == 0 else neg + 1
            else:  # num < 0
                new_pos = pos
                pos = 0 if neg == 0 else neg + 1
                neg = new_pos + 1
            mx = max(mx, pos)
        return mx


# num    9    5    8    2    -6    4    -3    0    2    -5    15    10    -7    9    -2
# pos    1    2    3    4     0    1     7    0    1     0    1     2      5    6     5
# neg    0    0    0    0     5    6     2    0    0     2    3     4      3    4     7

# zer ? pos= neg= 0
# pos ? pos++, neg++
# neg ? swap, pos++, neg++

print(Solution.getMaxLen(None, nums=[-1, 1, -2, 1, -3, 8, - 4, -5, ]))  # 7
print(Solution.getMaxLen(None, nums=[1, -2, 1, -3, 8, - 4, -5, 0, 3, 5, -1, -2]))  # 7
print(Solution.getMaxLen(None, nums=[1, -2, -3, 4]))  # 4
print(Solution.getMaxLen(None, nums=[0, 1, -2, -3, -4]))  # 3
print(Solution.getMaxLen(None, nums=[-1, -2, -3, 0, 1]))  # 2
print(Solution.getMaxLen(None, nums=[1, 2, 3, 5, -6, 4, 0, 10]))  # 4
print(Solution.getMaxLen(None, nums=[1, 2, 3, 5, 6, 4, 0, 10]))  # 6
