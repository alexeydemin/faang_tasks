from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m_without_zeros = 1
        zeros_cnt = 0
        for i in nums:
            if i:
                m_without_zeros *= i
            else:
                zeros_cnt += 1
        out = []
        for i in nums:
            if zeros_cnt > 1:
                out.append(0)
            elif zeros_cnt == 1 and i == 0:
                out.append(m_without_zeros)
            elif zeros_cnt == 1 and i:
                out.append(0)
            else:
                out.append(m_without_zeros // i)

        return out


# print(Solution.productExceptSelf(None, [1, 2, 3, 0, 4]))
# print(Solution.productExceptSelf(None, [1,1]))
# print(Solution.productExceptSelf(None, [0,1]))
# print(Solution.productExceptSelf(None, [5,6]))
# print(Solution.productExceptSelf(None, [1,2, 0, 0, 5]))
# print(Solution.productExceptSelf(None, [0, 0, 0]))
print(Solution.productExceptSelf(None, [4, 5, 1, 8, 2, 10, 6]))
