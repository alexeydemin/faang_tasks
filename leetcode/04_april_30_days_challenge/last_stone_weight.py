class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort(reverse=True)
            weight = stones[0] - stones[1]
            stones = stones[2:]
            if weight:
                 stones+= [weight]
        return stones[0] if len(stones) else 0


print(Solution.lastStoneWeight(None, [2, 7, 4, 1, 8, 1]))
