class StockSpanner:

    def __init__(self):
        self.stack = []  # [100, 80, 60, 70, 60, 75]
        self.stack_k = []

    def next(self, price: int) -> int:
        i = len(self.stack) - 1
        while i >= 0 and price >= self.stack[i]:
            i -= self.stack_k[i]

        self.stack.append(price)
        self.stack_k.append(len(self.stack) - 1 - i)

        return len(self.stack) - 1 - i


s = StockSpanner()
print(s.next(100))  # 1
print(s.next(80))  # 1
print(s.next(60))  # 1
print(s.next(70))  # 2
print(s.next(60))  # 1
print(s.next(75))  # 4
print(s.next(85))  # 6

# print(s.next(31))  # 1
# print(s.next(41))  # 1
# print(s.next(48))  # 2
# print(s.next(59))  # 3
# print(s.next(79))  # 4

# [100, 80, 60, 70, 60, 75, 85]
