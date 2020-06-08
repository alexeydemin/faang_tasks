class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        while k:
            if len(num) == 1:
                return '0'
            for i in range(len(num) - 1):
                    if int(num[i + 1]):
                        if int(num[i]) <= int(num[i + 1]):
                            del num[i]
                            break
                    else:
                        del num[i]
                        break
            k -= 1

        return str(int(''.join(num)))


# print(Solution.removeKdigits(None, "1432219", 3))  # 1219
# print(Solution.removeKdigits(None, '10200', 1)) #200
# print(Solution.removeKdigits(None, '10', 2)) #0
#print(Solution.removeKdigits(None, '9', 1)) #0
#print(Solution.removeKdigits(None, '112', 1)) #11
print(Solution.removeKdigits(None, '5337', 2)) #33
