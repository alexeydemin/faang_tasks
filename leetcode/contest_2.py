class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dic = {}
        sm = 0
        res = 0
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                sm += 1
            dic[i] = sm
            if i >= k:
                res = max(res, dic[i] - dic[i - k])
            else:
                res = max(res, dic[i])
        return res


print(Solution.maxVowels(None, 'abciiidef', 3))
print(Solution.maxVowels(None, s="aeiou", k=2))
print(Solution.maxVowels(None, s="leetcode", k=3))
print(Solution.maxVowels(None, s="rhythms", k=4))
print(Solution.maxVowels(None, s="tryhard", k=4))
print(Solution.maxVowels(None, s="ibpbhixfiouhdljnjfflpapptrxgcomvnb", k=33))

# ibpbhixfiouhdljnjfflpapptrxgcomvnb