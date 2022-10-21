import bisect
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        for i, c in enumerate(s):
            if c == '|':
                candles.append(i)
        # print(candles)
        res = []
        for start, end in queries:
            left_candle_i = bisect.bisect_left(candles, start)
            right_candle_i = bisect.bisect(candles, end) - 1
            # print(left_candle_i)
            # print(right_candle_i)
            if left_candle_i < right_candle_i:
                res.append(candles[right_candle_i] - candles[left_candle_i] - (right_candle_i - left_candle_i))
            else:
                res.append(0)
        return res


# _                                          0123456789
print(Solution.platesBetweenCandles(None, s="||**||**|*", queries=[[3, 8]]))  # [2]
print(Solution.platesBetweenCandles(None, s="**|**|***|", queries=[[2, 5], [5, 9]]))  # [2,3]
print(Solution.platesBetweenCandles(None, s="***|**|*****|**||**|*", queries=[[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))  # [9,0,0,0,0]
