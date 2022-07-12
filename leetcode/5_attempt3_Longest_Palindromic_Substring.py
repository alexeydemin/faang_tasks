class Solution:
    def longestPalindrome(self, s: str):
        max_poly = ''

        def check_poly_x(a, b, poly):
            nonlocal max_poly
            if a - 1 >= 0 and b + 1 < len(s) and s[a - 1] == s[b + 1]:
                poly = s[a - 1] + poly + s[b + 1]
                if len(poly) > len(max_poly):
                    max_poly = poly
                check_poly_x(a - 1, b + 1, poly)

        def check_poly_xx(a, b, poly):
            nonlocal max_poly
            if a >= 0 and b < len(s) and s[a] == s[b]:
                poly = s[a] + poly + s[b]
                if len(poly) > len(max_poly):
                    max_poly = poly
                check_poly_xx(a - 1, b + 1, poly)

        if len(s) == 0:
            return ''
        for i in range(len(s)):
            check_poly_x(i, i, s[i])
            check_poly_xx(i, i+1, '')

        return max_poly or s[0]


# print(Solution.longestPalindrome(None, "bb"))
# print(Solution.longestPalindrome(None, "aacabdkacaa"))
print(Solution.longestPalindrome(None, 'babad'))
# print(Solution.longestPalindrome(None, '"aacabdkacaa"'))
# print(Solution.longestPalindrome(None, 'zkabak0'))
# print(Solution.longestPalindrome(None, '012345'))
#       zkabak0
#       0kabakz
