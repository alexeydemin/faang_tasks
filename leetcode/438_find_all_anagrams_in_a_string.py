from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def str_do_dict(st):
            dd = defaultdict(lambda: 0)
            for s in st:
                dd[s] += 1
            return dd

        i = 0
        j = len(p) - 1
        buffer = str_do_dict(p)
        res = []
        while i <= len(s) - len(p) + 1:
            string = s[i:j + 1]
            window_dict = str_do_dict(string)
            if buffer == window_dict:
                res.append(i)
            i += 1
            j += 1

        return res


print(Solution.findAnagrams(None, 'cbaebabacd', 'abc'))  # [0,6]
print(Solution.findAnagrams(None, 'abab', 'ab'))  # [0,1,2]
#
