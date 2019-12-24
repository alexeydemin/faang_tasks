class Solution:
    def isValid(self, str):
        m = []
        for s in str:
            if s in ['(', '[', '{']:
                m.append(s)
                continue
            if len(m) == 0:
                return False
            else:
                last = m[-1]
            if s == ')' and last == '(' or s == ']' and last == '[' or s == '}' and last == '{':
                m.pop()
            else:
                return False
        if len(m) == 0:
            return True
        else:
            return False


g = Solution.isValid(None, '([])')
print(g)
