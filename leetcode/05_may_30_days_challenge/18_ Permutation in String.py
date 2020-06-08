from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = Counter(s1)
        s2_cnt = Counter()
        for i in range(len(s2)):
            s2_cnt[s2[i]] += 1
            if i >= len(s1):
                s2_cnt[s2[i - len(s1)]] -= 1
                if s2_cnt[s2[i - len(s1)]] == 0:
                    del s2_cnt[s2[i - len(s1)]]
            if s1_cnt == s2_cnt:
                return True
        return False


print(Solution.checkInclusion(None, "ab", "eidbaooo"))  # True
print(Solution.checkInclusion(None, "ab", "eidboaoo"))  # False
