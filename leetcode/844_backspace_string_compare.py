class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        si = len(s) - 1
        ti = len(t) - 1

        while si >= 0 or ti >= 0:
            skips = skipt = 0
            while si >= 0:
                if s[si] == '#':
                    skips += 1
                    si -= 1
                elif skips > 0:
                    skips -= 1
                    si -= 1
                else:
                    break
            while ti >= 0:
                if t[ti] == '#':
                    skipt += 1
                    ti -= 1
                elif skipt > 0:
                    skipt -= 1
                    ti -= 1
                else:
                    break
            if (si >= 0) != (ti >= 0):
                return False
            if (si >= 0) and ti >= 0 and s[si] != t[ti]:
                return False
            si -= 1
            ti -= 1
        return True


print(Solution.backspaceCompare(None, s="ab#c", t="ad#c"))  # true
# print(Solution.backspaceCompare(None, s="ab##", t="c#d#"))  # true
# print(Solution.backspaceCompare(None, s="a#c", t="b"))  # false
