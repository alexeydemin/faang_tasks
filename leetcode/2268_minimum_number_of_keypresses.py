from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str):
        res = 0
        for i, val in enumerate(sorted(Counter(s).values(), reverse=True)):
            if 0 <= i < 9:
                res += val
            elif 9 <= i < 18:
                res += val * 2
            else:
                res += val * 3
        return res


# print(Solution.minimumKeypresses(None, 'abcdefghijkla')) #16
print(Solution.minimumKeypresses(None, 'aaaaaaaabcdefgggghijkllllllllllmmmnoppponono'))  # 51
