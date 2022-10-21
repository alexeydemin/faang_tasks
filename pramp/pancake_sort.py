def pancake_sort(arr):
    def flip(arr, k):
        return arr[k - 1::-1] + a[k:]

    return flip(arr, 3)


a = [1, 5, 4, 3, 2]
23451
# a = [1, 2, 3, 4, 5]

print(pancake_sort(a))  # [1, 2, 3, 4, 5]
