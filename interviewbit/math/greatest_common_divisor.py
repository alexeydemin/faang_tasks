class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        res = []
        for i in range(1, min(A, B)+1):
         #   print(i, A % i, B % i)
            if A % i == 0 and B % i == 0:
                res.append(i)
        #print(res)
        return max(res) if len(res) else max(A,B)

r = Solution.gcd(None, 7, 6)
print(r)
