class Solution:

    def insert(self, intervals, new_interval):
        A = []
        start = False
        ended = False
        ns = new_interval[0]
        ne = new_interval[1]
        if ne <= intervals[0][0]:
            return [new_interval] + intervals
        if intervals[-1][1] <= ns:
            return intervals + [new_interval]

        for i in intervals:
            _is = i[0]
            ie = i[1]
            if start and ne < _is:
                A.append([start, ne])
                ended = True
            if ns < _is < ne < ie:
                if start:
                    A.append([start, ie])
                    start = False
                    ended = True
                else:
                    A.append(i)
            elif _is < ns < ie < ne:
                start = min(ns, _is)
            elif _is <= ns <= ne <= ie:
                continue
            else:
                if ended or start == False:
                    A.append(i)
            if intervals == A:
                return sorted(A + [new_interval])
        return A


# r = Solution.insert(None, [[1, 3], [6, 9]], [2, 5])
# r = Solution.insert(None, [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9])
r = Solution.insert(None, [[1, 2], [8, 10]], [3, 6])
# r = Solution.insert(None, [(6037774, 6198243), (6726550, 7004541), (8842554, 10866536), (11027721, 11341296), (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559), (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 36418956), (37225039, 37785557), (40087908, 41184444), (41922814, 45297414), (48142402, 48244133), (48622983, 50443163), (50898369, 55612831), (57030757, 58120901), (59772759, 59943999), (61141939, 64859907), (65277782, 65296274), (67497842, 68386607), (70414085, 73339545), (73896106, 75605861), (79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097)], (36210193, 61984219))

# ai=Solution()
# [1,5],[6,9]
# [1,2],[3,10],[12,16]
print(r)
