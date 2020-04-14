# Task 3 For this one the description was straight forward, but the implementation kicked my butt.
# "You have an infinite chessboard, and a knight. The knight starts at [0, 0] and can move
# [like a knight moves, skipped for brevity]. Given two coordinates on the board, return the least amount of moves the
# knight has to make to get to that position". I only had 50min when I started on this one, but even that wasn't enough
# for me to get even close to a solution. I tried like 10 different things that didn't work, deleted them, started over, etc;
# and at the end I had pretty much nothing.

import sys

sys.setrecursionlimit(9500)

end = (5, 5)
k = 0
visited = []


def jump(x=0, y=0):
    global k

    print(k, x, y)

    if x == end[0] and y == end[1]:
        return
    k += 1

    for pos in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2,), (-2, -1), (-2, 1), (-1, 2)]:
        if 0 < x + pos[0] < 8 and 0 < y + pos[1] < 8 and (x + pos[0], x + pos[1]) not in visited:
            visited.append((x + pos[0], x + pos[1]))
            jump(x + pos[0], y + pos[1])


jump()
print(k)
