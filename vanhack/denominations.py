class Currency:
    def __init__(self, denominations):
        self.coins = denominations
        self.min_coins = float('inf')
        self.num = len(self.coins)

    def num_ways(self, amount):
        arr = [[0] * (amount + 1) for x in range(self.num + 1)]
        for i in range(self.num + 1):
            arr[i][0] = 1

        for i in range(1, self.num + 1):
            for j in range(1, amount + 1):
                if self.coins[i - 1] > j:
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - self.coins[i - 1]]

        return arr[self.num][amount]

    def min_change(self, amount):
        self.coins.sort(reverse=True)

        self.count_coins(0, 0, amount)
        return self.min_coins if self.min_coins < float('inf') else -1

    def count_coins(self, start_coin, coin_count, remaining_amount):
        coins = self.coins
        if remaining_amount == 0:
            self.min_coins = min(self.min_coins, coin_count)
            return

        for i in range(start_coin, self.num):
            remaining_coin_allowance = self.min_coins - coin_count
            max_amount_possible = coins[i] * remaining_coin_allowance

            if coins[i] <= remaining_amount < max_amount_possible:
                self.count_coins(i, coin_count + 1, remaining_amount - coins[i])


print('test')
us_cent = Currency([100, 50, 25, 10, 5, 1])
print(us_cent.min_change(194))  # 9
print(us_cent.num_ways(100))  # 293

# import random
# import unittest
#
# class Test(unittest.TestCase):
#     def test_american_coins(self):
#         us_cent = Currency([100, 50, 25, 10, 5, 1])
#         self.assertEqual(293, us_cent.num_ways(100))
#         self.assertEqual(9, us_cent.min_change(194))
