class Solution:
    def minSwaps(self, s: str) -> int:
        def count_swaps(s, ch):
            num_swaps = 0
            for i, c in enumerate(s):
                if c == ch and i % 2 == 0:
                    num_swaps += 1
            return num_swaps

        num_zeros = num_ones = 0
        for c in s:
            if c == '0':
                num_zeros += 1
            else:
                num_ones += 1
        # print(num_zeros, num_ones)
        if abs(num_zeros - num_ones) > 1:
            return -1
        if num_zeros > num_ones:  # 0....
            return count_swaps(s, '1')
        elif num_zeros < num_ones:
            return count_swaps(s, '0')  # 1.....
        else:
            return min(count_swaps(s, '1'), count_swaps(s, '0'))


print(Solution.minSwaps(None, "111000"))  # 1
print(Solution.minSwaps(None, "010"))  # 0
print(Solution.minSwaps(None, "1110"))  # -1
