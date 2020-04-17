from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        ln = len(nums)
        answer.append(1)
        for i in range(1, ln):
            answer.append(nums[i - 1] * answer[i-1])
        r = 1
        for i in reversed(range(ln)):
            answer[i] *= r
            r *= nums[i]

        return answer


# print(Solution.productExceptSelf(None, [1, 2, 3, 0, 4]))
# print(Solution.productExceptSelf(None, [1,1]))
# print(Solution.productExceptSelf(None, [0,1]))
# print(Solution.productExceptSelf(None, [5,6]))
# print(Solution.productExceptSelf(None, [1,2, 0, 0, 5]))
# print(Solution.productExceptSelf(None, [0, 0, 0]))
print(Solution.productExceptSelf(None, [4, 5, 1, 8, 2, 10, 6]))
