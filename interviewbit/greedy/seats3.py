import statistics

class Solution:
    def seats(self, A):
        # get current seats indexes
        seats = []
        for i, a in enumerate(A):
            if a == 'x':
                seats.append(i)

        # get median
        n = len(seats)
        if n == 0:
            return 0
        else:
            med = int(statistics.median(seats))


        # get future seats indexes
        future = range(
            med - n // 2 + (0 if n%2 else 1),
            med + n // 2 + 1
        )

        # count hops
        hops = 0
        for i, a in enumerate(seats):
            hops += abs(seats[i] - future[i])

        return hops


# .x.x.x..x
# 012345678
# ....x..xx...x..
# 012345678901234
# ....x..xx...xxx
# 012345678901234

# r = Solution.seats(None, '.x.x.x...x')
#r = Solution.seats(None, '....x..xx...x..')
r = Solution.seats(None, '.xxx')
print(r)
