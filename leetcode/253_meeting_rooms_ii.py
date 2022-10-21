import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])
        for i in intervals[1:]:
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])

        return len(rooms)


print(Solution.minMeetingRooms(None, [[0, 30], [15, 20], [5, 10]]))
