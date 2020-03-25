def binary_gap(N):

    '''
    A binary gap within a positive integer N is any maximal
    sequence of consecutive zeros that is surrounded by ones
    at both ends in the binary representation of N.
    Args:
      - N: integer within the range [1..2,147,483,647]
    '''
    k = 0
    max = 0
    for a in str(int(str(N)[::-1])):
        if a == '0':
            k+=1
            if k > max:
                max = k
        else:
            k = 0
    return max

r = binary_gap('10001000')
print(r)