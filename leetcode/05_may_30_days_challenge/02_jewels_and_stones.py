class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        se = set()
        cnt = 0
        for j in J:
            se.add(j)
        for s in S:
            if s in se:
                cnt+=1
        return cnt


J = "aA"
S = "aAAbbbb"
print(Solution.numJewelsInStones(None, J, S))
