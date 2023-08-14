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
    print('arr1',arr)
    f.close()
    checkNeighbour(arr)


def checkNeighbour(arr1):
    lifeCount = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            aCount = 0
            # top
            if arr1[i - 1][j] == '*' and i > 0:
                aCount += 1
            # left
            if arr1[i][j - 1] == '*' and j > 0:
                aCount += 1
            # bottom
            try:
                if arr1[i + 1][j] == '*' and i < y - 1:
                    aCount += 1
            except IndexError:
                pass
            # right
            try:
                if arr1[i][j + 1] == '*' and j < x - 1:
                    aCount += 1
            except IndexError:
                pass
            # top-left
            try:
                if arr1[i - 1][j - 1] == '*' and i > 0 and j > 0:
                    aCount += 1
            except IndexError:
                pass
            # bottom-left
            try:
                if arr1[i + 1][j - 1] == '*' and i < y - 1 and j > 0:
                    aCount += 1
            except IndexError:
                pass
            # top_right
            try:
                if arr1[i - 1][j + 1] == '*' and i > 0 and j < x - 1:
                    aCount += 1
            except IndexError:
                pass
            # bottom-right
            try:
                if arr1[i + 1][j + 1] == '*' and i < y - 1 and j < x - 1:
                    aCount += 1
            except IndexError:
                pass
            lifeCount.append(aCount)
    count_arr = np.array(lifeCount).reshape(y,x)
    return count_arr



Conway('input4.txt')