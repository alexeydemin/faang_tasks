from collections import defaultdict


class Solution:
    def longestDupSubstring(self, s: str):
        lst = []
        dic = {}
        for i, c in enumerate(s):
            if c in lst:
                dic[c] = 1
            lst.append(c)

            for k in range(i):
                ch = lst[-i - 1] + c
                if ch in lst:
                    dic[ch] = 1
                lst.append(ch)
        return max(dic, key=lambda x: len(x))



print(Solution().longestDupSubstring('banana'))
#print(Solution().longestDupSubstring('abcde'))
# print(Solution().longestDupSubstring('banana'))
# print(Solution().longestDupSubstring('abcabcd'))
