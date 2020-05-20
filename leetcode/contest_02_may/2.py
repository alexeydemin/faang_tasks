class Solution:
    def maxDiff(self, num: int) -> int:
        st = str(num)
        if len(st) == 1:
            return 8

        first_num = num
        for i in range(len(st)):
            if st[i] != '9':
                first_num = int(st.replace(st[i], '9'))
                break

        second_num = num
        for i in range(len(st)):
            r = '0' if i and st[i] != st[0] else '1'
            if st[i] != r:
                second_num = int(st.replace(st[i], r))
                break
        print(first_num, second_num, first_num - second_num)
        return first_num - second_num


# Solution.maxDiff(None, 555)  # 888
# Solution.maxDiff(None, 9)  # 8
# Solution.maxDiff(None, 123456)  # 820000
# Solution.maxDiff(None, 10000)  # 80000
# Solution.maxDiff(None, 9288)  # 8700
print(Solution.maxDiff(None, 1101057))  # 8808050
