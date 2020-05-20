class StockSpanner:

    def __init__(self):
        self.total_days = 0
        self.dic = {}
        self.stack = [100, 80, 60, 70, 60, 75]
        self.stack_k = [1, 1, 2, 1, 4]

    def next(self, price: int) -> int:
        if len(self.stack) == 0:
            self.stack.append(price)
            return 1

        k = 0
        i = len(self.stack) - 1
        while i:
            #i -= self.stack_k[i - 1]
            if price >= self.stack[i]:
                k += 1
            else:
                break
            i -= 1

        self.stack.append(price)
        self.stack_k.append(k + 1)

        return k + 1


s = StockSpanner()
# print(s.next(100))  # 1
# print(s.next(80))  # 1
# print(s.next(60))  # 1
# print(s.next(70))  # 2
# print(s.next(60))  # 1
# print(s.next(75))  # 4
print(s.next(85))  # 6

# [100, 80, 60, 70, 60, 75, 85]
