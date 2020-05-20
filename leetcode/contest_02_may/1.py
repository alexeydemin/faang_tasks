from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = []
        for c in candies:
            res.append(c == mx or c + extraCandies >= mx)
        return res


print(Solution.kidsWithCandies(None, [12, 1, 12], 10))
print(Solution.kidsWithCandies(None, [4,2,1,1,2], 1))
print(Solution.kidsWithCandies(None, [2,3,5,1,3,], 3)) #[true,true,true,false,true]
