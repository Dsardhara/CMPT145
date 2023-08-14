# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

import numpy as np

ls = []


def Conway(fileName):
    global len_vertical, line, y, x, f_name
    f_name = fileName
    count = 0

    f = open(fileName, 'r')
    for line in f:
        line = line.rstrip()
        count += 1
        for i in line:
            ls.append(i)

    y = count
    x = len(line)
    arr = np.array(ls).reshape(y, x)
    print(arr)
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
    count_arr = np.array(lifeCount).reshape(y, x)
    # print(count_arr)
    return game_Of_Life(arr1, count_arr)


def game_Of_Life(original_arr, list_arr):
    last_ls = []
    file = open(f'{f_name}' + '3' + '_updated.txt', 'w+')
    for i in range(len(original_arr)):
        for j in range(len(original_arr[i])):
            if list_arr[i][j] < 2 or list_arr[i][j] > 3:
                file.write('-')
                last_ls.append('-')
            elif (list_arr[i][j] == 2 or list_arr[i][j] == 3) and original_arr[i][j] == '*':
                file.write('*')
                last_ls.append('*')
            elif list_arr[i][j] == 3:
                file.write('*')
                last_ls.append('*')
            else:
                file.write('-')
                last_ls.append('-')
    file.close()

# Conway('input5.txt')
