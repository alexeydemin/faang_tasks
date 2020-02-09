#!/bin/python

import os
import sys
import math
#
# Complete the gradingStudents function below.
#

def myRound(n, base = 5):
    return int(base * math.ceil(float(n) / base))


def gradingStudents(grades):
    list = []
    for grade in grades:
        if grade < 38:
            list.append(grade)
        else:
            if abs(myRound(grade)-grade) < 3:
                list.append(myRound(grade))
            else:
                list.append(grade)
    return list

grades = [73, 67, 38, 33]
#75 67 40 33

print gradingStudents(grades)
