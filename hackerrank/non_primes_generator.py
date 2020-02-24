import math


def manipulate_generator(generator, n):
    ka = 0
    for i in generator:
        if ka < n: #and (is_nonprime(i) or i == 1):
            yield i
            ka+=1


def is_nonprime(x):
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            return True
        i += 1
    return False


def positive_integers_generator():
    n = 1
    while True:
        yield n
#        if x is not None:
#            n = x
#        else:
        n += 1



k = int(input())
g = positive_integers_generator()
for a in manipulate_generator(g, k):
    print(a)