import bisect
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix = ''
        i = 0
        res = []
        for ch in searchWord:
            prefix += ch
            i = bisect.bisect_left(products, prefix, i)
            step = []
            for prod in products[i:i+3]:
                if prod.startswith(prefix):
                    step = products[i:i + 3]
            res.append(step)
        return res


print(Solution.suggestedProducts(None, products=[
    "mobile",
    "mouse",
    "moneypot",
    "monitor",
    "mousepad"
],
                                 searchWord="mouse"))

# ["mobile", "moneypot", "monitor"],
# ["mobile", "moneypot", "monitor"],
# ["mouse", "mousepad"],
# ["mouse", "mousepad"],
# ["mouse", "mousepad"]
# ]
2
