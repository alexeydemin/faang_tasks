from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        res = ''
        for a in Counter(s).most_common():
            res += a[0]*a[1]
        return res




print(Solution.frequencySort(None, "tree")) #"eert"
#print(Solution.frequencySort(None, "cccaaa")) #"cccaaa"
#print(Solution.frequencySort(None, "Aabb")) #"bbAa"


