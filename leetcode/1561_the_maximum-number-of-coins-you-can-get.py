from typing import List


class Solution:
    def maxCoins(self, piles: List[int]):
        piles.sort(reverse=True)
        res = 0
        while piles:
            del piles[0]  # Alice
            res += piles.pop(0)  # Me
            del piles[-1]  # Bob
        return res


print(Solution.maxCoins(None, piles=[2, 4, 1, 2, 7, 8]))  # 9
print(Solution.maxCoins(None, piles=[2, 4, 5]))  # 4
print(Solution.maxCoins(None, piles=[9, 8, 7, 6, 5, 1, 2, 3, 4]))  # 18

# [9,8,7,6,5,4,3,2,1]
# [9, 8, 1,    7, 6, 5,    4, 3, 2] = 8+7+3 = 18
