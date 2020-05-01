class Solution:
    def backspaceCompare(self, S, T):
        return self.clean(S) == self.clean(T)

    def clean(self, s):
        s = list(s)
        erase = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                erase += 1
                del s[i]
            elif erase > 0:
                erase -= 1
                del s[i]
            i -= 1
        return str(s)


s = Solution()
# print(s.clean('ab#c'))
# print(s.clean(''))
print(s.backspaceCompare(S="ab#c", T="ad#c"))
print(s.backspaceCompare(S="ab##", T="c#d#"))
print(s.backspaceCompare(S="ab#c", T="ad#c"))
print(s.backspaceCompare(S="a#c", T="b"))
