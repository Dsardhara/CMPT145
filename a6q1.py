# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

import numpy as np

ls = []


def Conway(fileName, repetation=3):
    global len_vertical, line, y, x, f_name, flag, main_repetation, arr
    main_repetation = repetation
    f_name = fileName.removesuffix('.txt')

    count = 0

    # Ask User for console outputs
    user = input("To see the results in the console press Y or press N otherwise: ")
    if user == 'y' or user == 'Y':
        flag = True
    else:
        flag = False

    f = open(fileName, 'r')
    for line in f:
        line = line.rstrip()
        count += 1
        for i in line:
            ls.append(i)

    y = count
    x = len(line)
    arr = np.array(ls).reshape(y, x)
    # print('original array:\n', arr)
    f.close()
    checkNeighbour(arr, repetation)
    zombie_neighbour(arr)


def checkNeighbour(arr1, repetation):
    lifeCount = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            aCount = 0
            # top
            if (arr1[i - 1][j] == '*' or arr1[i - 1][j] == 'Z') and i > 0:
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
    if repetation <= 0:
        write_file(arr1)
    else:
        repetation -= 1
        game_Of_Life(arr1, count_arr, repetation)


def zombie_neighbour(arr2):
    zombie_list = []

    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            zombies_increment = 0

            # Top
            if arr2[i - 1][j] == 'Z' and i > 0:
                zombies_increment += 1

            # Top-Left
            try:
                if arr2[i - 1][j - 1] == 'Z' and i > 0 and j > 0:
                    zombies_increment += 1
            except IndexError:
                pass

            # Left
            if arr2[i][j - 1] == 'Z' and j > 0:
                zombies_increment += 1

            # Bottom-Left
            try:
                if arr2[i + 1][j - 1] == 'Z' and i < y - 1 and j > 0:
                    zombies_increment += 1
            except IndexError:
                pass

            # Bottom
            try:
                if arr2[i + 1][j] == 'Z' and i < y - 1:
                    zombies_increment += 1
            except IndexError:
                pass

            # Bottom-Right
            try:
                if arr2[i + 1][j + 1] == 'Z' and i < y - 1 and j < x - 1:
                    zombies_increment += 1
            except IndexError:
                pass

            # Right
            try:
                if arr2[i][j + 1] == 'Z' and j < x - 1:
                    zombies_increment += 1
            except IndexError:
                pass

            # Top-Right
            try:
                if arr2[i - 1][j + 1] == 'Z' and i > 0 and j < x - 1:
                    zombies_increment += 1
            except IndexError:
                pass
            zombie_list.append(zombies_increment)
    zombie_arr = np.array(zombie_list).reshape(y, x)
    return zombie_arr


def game_Of_Life(original_arr, list_arr, repetation):
    last_ls = []
    call_zombie = zombie_neighbour(original_arr)
    for i in range(len(original_arr)):
        for j in range(len(original_arr[i])):
            living_count = list_arr[i][j] + call_zombie[i][j]
            if living_count < 2 or living_count > 3:
                last_ls.append('-')
            elif (living_count == 2 or living_count == 3) and original_arr[i][j] == '*' and call_zombie[i][j] > 0:
                last_ls.append('Z')
            elif (living_count == 2 or living_count == 3) and original_arr[i][j] == '*':
                last_ls.append('*')
            elif original_arr[i][j] == 'Z':
                last_ls.append('Z')
            elif living_count == 3:
                last_ls.append('Z')
            else:
                last_ls.append('-')
    last_arr = np.array(last_ls).reshape(y, x)
    # print('one step forward:\n', last_arr)

    if flag == True:
        print("\nIteration -", main_repetation - repetation)
        for row in last_arr:
            for person in row:
                print(person, end='')
            print()
    checkNeighbour(last_arr, repetation)


def write_file(final):
    latest_file = f'{f_name}' + "_" + f'{main_repetation}' + "steps.txt"
    f = open(latest_file, "w+")
    for row in final:
        for person in row:
            person = str(person)
            f.write(person)
        f.write('\n')
    f.close()
    print("Program Success...")


Conway('input5.txt')
