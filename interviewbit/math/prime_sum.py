import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        for a in range(1, A):
            print(a, A - a, Solution.is_prime(None, a), Solution.is_prime(None, A - a))
            if Solution.is_prime(None, a) and Solution.is_prime(None, A - a):
                return [a, A - a]

    def is_prime(self, a):
        for i in range(2, round(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True


r = Solution.primesum(None, 18)
print(r)
