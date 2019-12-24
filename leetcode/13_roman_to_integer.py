class Solution:
    def romanToInt(self, str):
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        i = 0
        while i < len(str):
            if i + 1 < len(str):
                if str[i] == 'I' and str[i + 1] == 'V':
                    res += 4
                    i += 2
                    continue
                if str[i] == 'I' and str[i + 1] == 'X':
                    res += 9
                    i += 2
                    continue
                if str[i] == 'X' and str[i + 1] == 'L':
                    res += 40
                    i += 2
                    continue
                if str[i] == 'X' and str[i + 1] == 'C':
                    res += 90
                    i += 2
                    continue
                if str[i] == 'C' and str[i + 1] == 'D':
                    res += 400
                    i += 2
                    continue
                if str[i] == 'C' and str[i + 1] == 'M':
                    res += 900
                    i += 2
                    continue
            res += dic[str[i]]
            i += 1
        return res


a = Solution.romanToInt(None, 'MCCXLIII')
print('===')
print(a)

# IV = 4MCCXLIII
# IX = 9
# XL
# XC
# CD
# CM
#
