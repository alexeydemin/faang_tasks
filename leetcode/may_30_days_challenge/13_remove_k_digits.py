class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # dic = {}
        # for i, el in enumerate(list(num)):
        #     if el in dic:
        #         dic[el].append(i)
        #     else:
        #         dic[el] =[i]
        # dic[max(dic)][0]
        # print(dic)
        # print()
        #for i in range(k):
        #    for d in dic:
        for i in range(9):
            for n in list(num):
                if n == 9:








        return None
print(Solution.removeKdigits(None, "1432219", 3))  # 1219
# print(Solution.removeKdigits(None, '10200', 1)) #200
# print(Solution.removeKdigits(None, '10', 2)) #0
