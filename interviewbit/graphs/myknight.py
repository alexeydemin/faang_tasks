def knight(A, B, C, D, E, F):
    d = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    start = (C - 1, D - 1, 0)
    end = (E - 1, F - 1)
    q = [start]  # queue
    visited = [[0] * B for _ in range(A)]
    visited[start[0]][start[1]] = 1
    while len(q):
        cur = q.pop(0)
        if cur[0] == end[0] and cur[1] == end[1]:
            return cur[2]
        for i in range(8):
            x = cur[0] + d[i][0]
            y = cur[1] + d[i][1]

            if 0 <= x <= A - 1 and 0 <= y <= B - 1 and not visited[x][y]:
                visited[x][y] = 1
                q.append((x, y, cur[2] + 1))
    return -1


r = knight(8, 8, 1, 1, 8, 8)
#r = knight(4, 7, 2, 6, 2, 4)
print(r)
