# Task 1 Your function takes an array of integers (arr), and an integer (x). You need to find the position in arr that
# splits the array in two, where one side has as many occurrences of x as the other side has occurrences of any number
# but x (there was some additional info about edge cases, but that's the gist of it). So, given an array like this:
# [5, 5, 2, 3, 5, 1, 6] and x being "5", the function should return "4" (Position 4, holding the number "3" above is
# the point where you have 2 5's on the one side, and two "not fives" on the other.


# Divide array

def solution2(x, arr):
    x_count = arr.count(x)
    match = 0
    unmatch = len(arr) - x_count

    if x_count in [len(arr), 0]:
        return -1

    for i, a in enumerate(arr):
        if a == x:
            match+=1
        else:
            unmatch-=1
        if match == unmatch:
            return i+1


test_array = [
    [5, 5, 1, 7, 2, 3, 5],  # X in [0..K-1] == !X in [K..N-1], K == 4
    [1, 15, 5, 51, 4, 7, 9, 1, 3, 4, 5, 8, 9, 6, 3, 5, 4, 7, 6, 5, 5],  # X in [0..K-1] == !X in [K..N-1], K == 4
    [1, 1, 1, 1, 1, 1],  # [0..K-1] is empty
    [5, 5, 5, 5, 5, 5, 5]  # [K..N-1] is empty

]


def solution(X, A):
    x_count = A.count(X)
    if x_count in [0, len(A)]:
        return x_count

    same_count = 0
    diff_count = len(A) - x_count
    index = 0

    while same_count != diff_count and index != len(A) - 1:
        if A[index] == X:
            same_count += 1
        else:
            diff_count -= 1
        index += 1

    return index


for a in test_array:
    print(solution(5, a), solution2(5, a))
