class Solution:
    def decodeString(self, s: str) -> str:
        res = di = st = ''
        open = 0
        for a in s:
            if a.isdigit():
                if open:
                    st += a
                else:
                    di += a
            elif a.isalpha():
                if open:
                    st += a
                else:
                    res += a
            elif a == '[':
                if open:
                    st += a
                open += 1
            elif a == ']':
                if open == 1:
                    res += int(di) * self.decodeString(st)
                    st = di = ''
                else:
                    st += a
                open -= 1
        return res


print(Solution().decodeString('3[a]2[bc]') == 'aaabcbc')  #
print(Solution().decodeString("3[a2[c]]") == 'accaccacc')
print(Solution().decodeString("2[abc]3[cd]ef") == 'abcabccdcdcdef')  #
