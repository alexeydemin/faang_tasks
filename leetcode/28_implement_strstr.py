class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, h in enumerate(haystack):
            if needle == haystack[i:i + len(needle)]:
                return i
        return -1


r = Solution.strStr(None, 'hello', 'll')  # 2
print(r)
# r = Solution.strStr(None, 'aaaaa', 'bba')  #-1
