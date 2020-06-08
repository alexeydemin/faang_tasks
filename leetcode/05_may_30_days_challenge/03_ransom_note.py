class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for a in magazine:
            if a in dic:
                dic[a]+=1
            else:
                dic[a] = 1
        for b in ransomNote:
            if b in dic:
                dic[b] -=1
                if not dic[b]:
                    del dic[b]
            else:
                return False
        return True

print(Solution.canConstruct(None, "aa", "aab"))