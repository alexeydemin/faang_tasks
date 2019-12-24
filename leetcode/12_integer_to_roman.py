class Solution:
    def intToRoman(self, val):
        rom_lst = [
            '', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'
        ]
        rom_lst = {i: rom_lst[i] for i in range(0, len(rom_lst))}
        res = ''
        for i, dig in enumerate(reversed(str(val))):
            entry = rom_lst[int(dig)]
            if i == 1:  # tens
                entry = entry.replace('IX', 'XC').replace('I', 'X').replace('V', 'L')
            if i == 2:  # hundreds
                entry = entry.replace('IX', 'CM').replace('I', 'C').replace('V', 'D')
            if i == 3:  # thousand
                entry = entry.replace('I', 'M')
            res = entry + res
        return res


# MCMXCIV
a = Solution.intToRoman(None, 1000)
print('===')
print(a)
print('MCMXCIV')
# IV = 4
# IX = 9
# XL
# XC
# CD
# CM
#
