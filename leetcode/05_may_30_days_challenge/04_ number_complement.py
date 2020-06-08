class Solution:
    def findComplement(self, num: int):
        s = bin(num)[2:]
        res = ''
        for i in s:
            res += str(abs(int(i) - 1))
        return int(res, 2)


print(Solution.findComplement(None, 5))
