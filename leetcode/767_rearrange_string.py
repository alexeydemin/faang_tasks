class Solution:
    def reorganizeString(self, s: str) -> str:
        st = sorted(sorted(s), key=s.count)
        # print(st)
        # rare --> often
        often = []
        rare = []
        mid = len(s) // 2
        for i in range(len(s)):
            if i < mid:
                rare.append(st[i])
            else:
                often.append(st[i])
        # print(rare)
        # print(often)
        res = ""
        for i in range(mid+1):
            if i < len(often):
                res += often[i]
            if i < len(rare):
                res += rare[i]

        for i in range(1, len(s)):
            if res[i-1] == res[i]:
                return ""
        return res


print(Solution.reorganizeString(None, "aab"))  # "aba"
print(Solution.reorganizeString(None, "aaab"))  # ""
print(Solution.reorganizeString(None, "baaaaccaaaaccc"))  # ""
