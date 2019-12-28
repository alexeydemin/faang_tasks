class Solution:
    @staticmethod
    def bio_hazard(self, n, allergic, poisonous):
        count = 0
        a = []
        for i in range(1, n + 1):
            print('---step #' + str(i) + '---')
            k = []
            for elem in a:
                elem_with_i = elem + [i]
                k.append(elem_with_i)
            a = [*a, *k]
            a.append([i])
            print(a)
            print('---endstep ---')

        return a


res = Solution.bio_hazard(None, 5, [], [])
# print(res)
