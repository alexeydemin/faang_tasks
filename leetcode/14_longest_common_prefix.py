from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        max_len = min(len(x) for x in strs)
        for i in range(max_len):
            pref = strs[0][i]
            for word in strs:
                if pref != word[i]:
                    return res
            res += pref
        return res


g = Solution.longestCommonPrefix(None, ["flower", "flow", "flowght"])  # fl
print(g)
