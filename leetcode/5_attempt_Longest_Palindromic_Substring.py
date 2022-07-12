class Solution:

    def longestPalindrome(self, s: str):
        def get_common(a, b):
            ret = ''
            for i in range(len(a)):
                if a[i] == b[i]:
                    ret += a[i]
            return ret
        r = s[::-1]
        max_poly = ''
        n = 2 * len(s)
        for i in range(n):
            sc = s[-n + i:i]
            rc = r[-i:n - i]
            common = get_common(sc, rc)
            print(sc)
            print(rc)
            print()
            if len(max_poly) < len(common):
                max_poly = common
        return max_poly


print(Solution.longestPalindrome(None, 'babad'))
#print(Solution.longestPalindrome(None, 'zkabak0'))
# print(Solution.longestPalindrome(None, '012345'))
#       zkabak0
#       0kabakz