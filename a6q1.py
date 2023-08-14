# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

import numpy as np

ls = []


def Conway(fileName):
    count = 0
    global len_vertical, line, y, x

    f = open(fileName, 'r')
    for line in f:
        line = line.rstrip()
        count += 1
        for i in line:
            ls.append(i)

    y = count
    x = len(line)
    arr = np.array(ls).reshape(y, x)
    f.close()
    return arr


print(Conway('input4.txt'))
