# https://www.hackerrank.com/challenges/minimum-time-required/problem
#
# You are planning production for an order.
# You have a number of machines that each have a fixed number of days to produce an item.
# Given that all the machines operate simultaneously,
# determine the minimum number of days to produce the required order.
# For example, you have to produce goal=10 items.
# You have three machines that take [2,3,2] days to produce an item.
# The following is a schedule of items produced:
#
# Day Produced  Total
#  1      0       0
#  2      2       2
#  3      1       3
#  4      2       5
#  6      3       8
#  8      2       10
#
# It takes 8 days to produce 10 items using these machines
# Complete the minTime function below.


arr[1] = 0
arr[2] = 2
arr[3] = 3
arr[4] = 5

10 / ((2 + 3 + 2) / 3)
avg_speed = 3
days / 1
item
number_of_days = number_of_items / (1 / max([2, 2, 3] * len([2, 2, 3]))) = ~10


def minTime(machines, goal):
    machines_num = len(machines)


worst_performance_all = machines_num // max(machines)
best_performance_all = machines_num // min(machines)

min_number_of_days = goal // best_performance_all
max_number_of_days = goal // worst_performance_all

binary(, min_number_of_days + max_number_of_days // 2, min_number_of_days, max_number_of_days)

def binary(arr, goal, start, end)
    items = get_items(cur)


if (items - goal < 1):
    return arr[]
elseif
items - goal > 1:
return binary(arr, goal, start, end)
else:
return binary(arr, goal, start, end)


def get_items(day):
    items = 0;


for m in machines:
    items += day / m
return items


def minTime(machines, goal):
    fastest = min(machines)
    slowest = max(machines)
    lenMachines = len(machines)
    uppBound = slowest * goal / lenMachines
    lowBound = fastest * goal / lenMachines
    while abs(uppBound - lowBound) > 1:
        current = (uppBound + lowBound) / 2


*num = getProducts1(current, machines, goal, fastest, slowest)
if num > goal:
    uppBound = current
elif num < goal:
    lowBound = current
else:
    break

** while getProducts(current, machines) >= goal:
    current -= 1
return current + 1

* def getProducts1(days, machines, goal, fastest, slowest):

**

def getProducts(days, machines):
    total = 0
    for d in machines:
        total += days / d
    return total




