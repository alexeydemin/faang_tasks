def move_zeros_to_end(arr):
    p = non_zero_p = 0
    while p < len(arr):
        print(arr, p, non_zero_p)
        if arr[p] != 0:
            arr[p], arr[non_zero_p] = arr[non_zero_p], arr[p]
            non_zero_p += 1
        p += 1

    return arr


arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
print(move_zeros_to_end(arr))  # 1, 10, 2, 8, 3, 0, 0, 0, 6, 4, 0, 5, 7, 0
arr = [0, 1, 2, 0, 0, 3, 4]
# ^
# ^
# print(move_zeros_to_end(arr))  # 1, 10, 2, 8, 3, 0, 0, 0, 6, 4, 0, 5, 7, 0
