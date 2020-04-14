from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0;
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1];
        return maxprofit


# r = Solution.maxProfit(None, [10, 7, 5, 8, 11, 9])
r = Solution.maxProfit(None, [10, 7, 5, 8, 11, 9, 10, 7, 5, 8, 11, 9])

print(r)
