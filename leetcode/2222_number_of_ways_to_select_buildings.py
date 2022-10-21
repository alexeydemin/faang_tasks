class Solution:
    def numberOfWays(self, s: str) -> int:
        number_of_zeros = number_of_ones = 0
        for c in s:
            if c == '0':
                number_of_zeros += 1
            else:
                number_of_ones += 1
        res = number_of_zeros_before = number_of_ones_before = 0
        for c in s:
            if c == '0':
                res += number_of_ones * number_of_ones_before
                number_of_zeros_before += 1
                number_of_zeros -= 1
            else:
                res += number_of_zeros * number_of_zeros_before
                number_of_ones_before += 1
                number_of_ones -= 1
        return res


print(Solution.numberOfWays(None, '001101'))  # 6
print(Solution.numberOfWays(None, '11100'))  # 0
