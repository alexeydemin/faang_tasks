from typing import List


class Solution:
    def hIndex(self, c: List[int]) -> int:
        N = len(c)

        if not N:
            return 0
        if N == 1:
            if c[0] == 1:
                return 1
            if c[0] == 0:
                return 0
        if c[0] == c[N-1] == 0:
            return 0

        for i in range(N):
            if c[i] <= N - i - 1 <= c[i + 1]:
                return N - i - 1
        return N if N < c[N - 1] else c[0]


print(Solution().hIndex([0, 1, 3, 5, 6]))  # 3
print(Solution().hIndex([0, 1, 5, 7, 9, 10]))  # 4
print(Solution().hIndex([0, 1, 5, 7, 9]))  # 3
print(Solution().hIndex([1, 1]))  # 1
print(Solution().hIndex([2, 2, 2]))  # 2
print('---------------------------')
print(Solution().hIndex([1, 1, 1, 3]))  # 1
print(Solution().hIndex([100]))  # 1
print(Solution().hIndex([]))  # 0
print(Solution().hIndex([1, 2]))  # 1
print(Solution().hIndex([0, 1, 1]))  # 1
print('---------------------------')
print(Solution().hIndex([0]))  # 1
print(Solution().hIndex([0, 0]))  # 1
