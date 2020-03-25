def count_div(A, B, K):
    '''
    Returns the number of integers within the range [A..B] that are divisible by K.
    Used generators to save memory on large amounts of data.
    Args:
      - A: is an integer within the range [0..2,000,000,000]
      - B: is an integer within the range [0..2,000,000,000] and A <= B
      - K: is an integer within the range [1..2,000,000,000]
    '''
    b = B // K
    a = (A - 1) // K if A > 0 else 0
    if A == 0:
        b += 1
    return b - a


print(count_div(2, 8, 2))
