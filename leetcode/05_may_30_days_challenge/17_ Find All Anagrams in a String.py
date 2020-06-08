from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i_s = []
        counter_p = dict(Counter(p))
        counter_s = Counter()
        for i in range(len(s)):
            counter_s[s[i]] += 1
            if i >= len(p):
                counter_s[s[i - len(p)]] -= 1
                if counter_s[s[i - len(p)]] == 0:
                    del counter_s[s[i - len(p)]]
            if counter_s == counter_p:
                i_s.append(i - len(p) + 1)
        return i_s


print(Solution.findAnagrams(None, "cbaebabacd", "abc"))  # [0, 6]
print(Solution.findAnagrams(None, "abab", "ab"))  # [0,1, 2]
print(Solution.findAnagrams(None, "ababababab", "aab"))  # [0,2,4,6]
