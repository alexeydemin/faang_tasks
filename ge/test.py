from collections import defaultdict


def find_common_ingredients(recipe_1, recipe_2):
    def to_dd(lst):
        d = defaultdict(int)
        for i in lst:
            d[i] += 1
        return d

    re1 = to_dd(recipe_1)
    re2 = to_dd(recipe_2)
    res = []
    for k, v in re1.items():
        if k in re2:
            res.extend([k] * min(re1[k], re2[k]))
    return res


print(find_common_ingredients([1, 1, 1, 2, 3, ], [1, 1, ]))
