class Solution:
    def seats(self, A):
        longest = Solution.getLongest(None, A)
        longest_start = longest[1]
        longest_end = longest[2]
        res = 0
        for i, s in enumerate(list(A)):
            if s == 'x':
                if i < longest_start:
                    res += longest_start - i - 1
                    longest_start -= 1
                if i > longest_end:
                    res += i - longest_end - 1
                    longest_end += 1
        return res % 10000003

    def getLongest(self, A):
        longest_len = 0
        longest_start = 0
        longest_end = 0

        local_len = 0
        local_start = 0
        for i, s in enumerate(list(A)):
            if s == 'x':
                if local_len == 0:
                    local_start = i
                local_len += 1
                if local_len > longest_len:
                    longest_len = local_len
                    longest_start = local_start
                    longest_end = longest_start + longest_len - 1
            else:
                local_len = 0
        return [longest_len, longest_start, longest_end]


# .x.x.x..x
# 012345678
# ....x..xx...x..
# 012345678901234
# ....x..xx...xxx
# 012345678901234

r = Solution.seats(None, '....x..xx...x..')
print(r)
