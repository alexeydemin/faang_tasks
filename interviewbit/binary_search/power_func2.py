class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):

        res = 1 % d  # Cover case d == 1
        print(n, x, d, res)
        while n > 0:
            if n % 2:  # Odd?
                res = (res * x) % d
            x = x ** 2 % d
            n = n // 2
            print(n, x, d, res)
        return res


# print(Solution.pow(None, 71045970, 41535484, 64735492))
print(Solution.pow(None, 3, 3, 5))
