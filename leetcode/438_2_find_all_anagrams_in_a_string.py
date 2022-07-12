from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        buffer, sl, pl, res = defaultdict(int), len(s), len(p), []
        if len(p) > len(s):
            return []

        for i in range(pl):
            buffer[p[i]] += 1

        for i in range(pl - 1):
            if s[i] in buffer:
                buffer[s[i]] -= 1

        for end in range(pl - 1, sl):
            start = end -pl
            if start >= 0 and s[start] in buffer:
                buffer[s[start]] += 1
            if s[end] in buffer:
                buffer[s[end]] -= 1

            if all(v == 0 for v in buffer.values()):
                res.append(start+1)

        return res


print(Solution.findAnagrams(None, 'cbaebabacd', 'abc'))  # [0,6]
print(Solution.findAnagrams(None, 'abab', 'ab'))  # [0,1,2]
#
