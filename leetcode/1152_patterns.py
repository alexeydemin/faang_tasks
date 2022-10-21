from typing import List
from itertools import combinations
from collections import defaultdict


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        tuples = sorted(zip(username, timestamp, website), key=lambda x: (x[1], [0]))
        users = defaultdict(list)
        # {'james': ['home', 'cart', 'maps', 'home'], 'joe': ['home', 'about', 'career'], 'mary': ['home', 'about', 'career']})
        for u, t, w in tuples:
            users[u].append(w)
        res = defaultdict(int)  # {(['home', 'about', 'career']) : 2,  ('home', 'cart', 'maps'): 1 ... '}
        for u, websites in users.items():
            for combination in set(combinations(websites, 3)):
                res[combination] += 1

        print(res)
        return list(sorted(res, key=lambda x: (res[x], x))[0])


a = Solution.mostVisitedPattern(None, username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary",
                                                "mary"],
                                timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about",
                                         "career"]
                                )

b = Solution.mostVisitedPattern(None, username=["ua", "ua", "ua", "ub", "ub", "ub"], timestamp=[1, 2, 3, 4, 5, 6],
                                website=["a", "b", "c", "a", "b", "a"]
                                )
print(b)
# ["home", "about", "career"]
