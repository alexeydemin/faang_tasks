def knight(A, B, C, D, E, F):
    d = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    start = (C, D, 0)
    end = (E, F)
    q = [start]  # queue
    visited = [(start[0], end[0])]
    while len(q):
        cur = q.pop(0)
        if cur[0] == end[0] and cur[1] == end[1]:
            return cur[2]
        for i in range(8):
            x = cur[0] + d[i][0]
            y = cur[1] + d[i][1]
            if 0 <= x <= A and 0 <= y <= B and (x, y) not in visited:
                visited.append((x, y))
                q.append((x, y, cur[2] + 1))
    return -1


r = knight(8, 8, 1, 1, 8, 8)
print(r)
