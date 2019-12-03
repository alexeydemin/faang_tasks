def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_h = 0
    oranges_h = 0
    for apple in apples:
        if s <= apple + a <= t:
            apples_h += 1
    for orange in oranges:
        if s <= orange + b <= t:
            oranges_h += 1
    return [apples_h, oranges_h]

print countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

