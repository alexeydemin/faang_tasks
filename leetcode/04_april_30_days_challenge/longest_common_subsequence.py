class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        res = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    continue
                if text1[i-1] == text2[j-1]:
                    res[i][j] = res[i-1][j-1] + 1
                else:
                    res[i][j] = max(res[i][j-1],res[i-1][j])
        return res[m][n]


print(Solution.longestCommonSubsequence(None, 'abcde', 'ace'))  # 3
# print(Solution.longestCommonSubsequence(None, 'abc', 'abc'))   #3
# print(Solution.longestCommonSubsequence(None, 'abc', 'def'))   #0
