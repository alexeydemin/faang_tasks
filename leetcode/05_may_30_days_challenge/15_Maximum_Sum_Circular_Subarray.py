from typing import List


class Solution:
    def _maxSubarraySumCircular(self, A: List[int]) -> int:
        all_max = float('-inf')
        B = A + A
        sm = 0
        mx = float('-inf')
        sums = {}
        for i in range(len(B)):
            sm = max(sm, 0)
            sm += B[i]
            sums[i] = sm
            if i >= len(A):
                sm = sm - sums[i]
            mx = max(sm, mx)
        print(sums)
        return mx
    def maxSubarraySumCircular(self, A: List[int]) -> int:
         sm = mx = 0



# [5, -3, 5, 5, -3, 5]
#  0   1  2  3  4  5


#print(Solution.maxSubarraySumCircular(None, [1, -2, 3, -2]))  # 3
print(Solution.maxSubarraySumCircular(None, [5, -3, 5]))  # 10
#print(Solution.maxSubarraySumCircular(None, [3, -1, 2, -1]))  # 4
#print(Solution.maxSubarraySumCircular(None, [3, -2, 2, -3]))  # 3
#print(Solution.maxSubarraySumCircular(None, [-2, -3, -1]))  # -1
#print(Solution.maxSubarraySumCircular(None, [2, -1, 4]))  # 6
#print(Solution.maxSubarraySumCircular(None, [-2, -1, -3, 4, -1, 2, 1, -5, 4]))  # 6
