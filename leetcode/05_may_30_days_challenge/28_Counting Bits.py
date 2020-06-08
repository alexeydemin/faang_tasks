from typing import List


class Solution:
    def countBits1(self, num: int) -> List[int]:
        ret = []
        for i in range(num+1):
            print(list(map(int, bin(i)[2:])))
            ret += [sum(map(int, bin(i)[2:]))]
        return ret
        # for i in [num]:
        #     print(i)
    def countBits(self, num):
        res = [0]
        i = 0
        while len(res) <= num:
            print(i, res)
            i += 1
            res += [i+1 for i in res]
        return res[:num+1]


print(Solution.countBits(None, 100))
