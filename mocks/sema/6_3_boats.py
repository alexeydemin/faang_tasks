def numberOfBoats(weights, capacity):
    boats = 0
    weights.sort(reverse=True)
    j = len(weights) - 1
    for i in range(len(weights)):
        if weights[i] + weights[j] <= capacity:
            j -= 1
        boats += 1
        if i >= j:
            return boats


print(numberOfBoats([9], 100))  # 3
print(numberOfBoats([87, 10, 90, 54, 38, 9], 100))  # 3
print(numberOfBoats([87, 10, 90, 99, 54, 38, 9], 100))  # 4
