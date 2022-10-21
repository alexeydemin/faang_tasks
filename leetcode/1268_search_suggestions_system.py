from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        print(products)
        str = ''
        res = []
        for i, c in enumerate(searchWord):
            res.append([])
            str += c
            for p in products:
                if p.startswith(str):
                    res[i].append(p)
                if len(res[i]) == 3:
                    break
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
