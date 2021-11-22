class Solution:

    def __init__(self):
        self.max_poly = ''
        self.stri = ''

    def check_poly_x(self, a, b, poly):

        if a - 1 >= 0 and b + 1 < len(self.stri) and self.stri[a - 1] == self.stri[b + 1]:
            poly = self.stri[a - 1] + poly + self.stri[b + 1]
            # print(poly)
            if len(poly) > len(self.max_poly):
                self.max_poly = poly
                # print(poly)
            self.check_poly_x(self, a - 1, b + 1, poly)

    def check_poly_xx(self, a, b, poly):
        if b + 1 < len(self.stri) and self.stri[a] == self.stri[b + 1]:
            poly = self.stri[a] + poly + self.stri[b + 1]
            if len(poly) > len(self.max_poly):
                self.max_poly = poly
                # print(poly)
            self.check_poly_xx(self, a - 1, b + 2, poly)

    def longestPalindrome(self, s: str):
        self.stri = s
        self.max_poly = ''
        if len(s) == 0:
            return ''
        for i in range(len(s)):
            # print(i)
            self.check_poly_x(self, i, i, s[i])
            self.check_poly_xx(self, i, i, '')
            # if i < len(self.stri) - 1:
            #    self.check_poly(Solution, i, i + 1, self.stri[i] + self.stri[i + 1])

        return self.max_poly or s[0]


#print(Solution.longestPalindrome(Solution, '0ababab'))
print(Solution.longestPalindrome(Solution, '"aacabdkacaa"'))
# print(Solution.longestPalindrome(Solution, 'cbbd'))
#print(Solution.longestPalindrome(Solution, 'aab'))
# print(Solution.longestPalindrome(Solution, 'jjjjjjjszaba0askdjkkabakmm'))
# print(Solution.longestPalindrome(None, '012345'))
#       zkabak0
#       0kabakz
