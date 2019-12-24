class Solution:
    def threeSum(self, nums):
        lis = []
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i != j:
                    lis.append( (a, b, a + b, i, j) )
        x = set()
        for l, val in enumerate(nums):
            for k, tup in enumerate(lis):
                if val + tup[2] == 0 and l != tup[3] and l!=tup[4] :
                    z = (tup[0], tup[1], val)
                    tpl = tuple(sorted(z))
                    x.add(tpl)
        ret = []
        for el in x:
            ll = list(el)
            ret.append(ll)
        return ret
g = Solution.threeSum(None, [-1, 0, 1, 2, -1, -4])
print(g)

