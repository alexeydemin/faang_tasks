class Solution:
    def decodeString(self, s: str) -> str:
        return self.go(s)

    def go(self, s):
        digits = ''
        st = ''
        stack = []
        for c in s:
            if c.isdigit():
                digits += c
            else:
                st += c
                if c == '[':
                    stack.append(c)
                elif c == ']':
                    stack.pop()
                    if not len(stack):
                        return str(int(digits if digits else 1) * self.go(st[1:-1]))


# print(Solution().decodeString('3[a]2[bc]'))  # aaabcbc
print(Solution().decodeString("3[a2[c]]"))  # accaccacc
# Solution().decodeString("2[abc]3[cd]ef")  # abcabccdcdcdef
