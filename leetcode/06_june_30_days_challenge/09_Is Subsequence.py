import numpy as np


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for c in s:
            i = t.find(c, start)
            if i == -1:
                return False
            start = i + 1
        return True


print(Solution().isSubsequence(s="abc", t="ahbgdc"))  # True
print(Solution().isSubsequence(s="bb", t="ahbgdc"))  # True
