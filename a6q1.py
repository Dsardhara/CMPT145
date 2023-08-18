# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

import numpy as np


def Conway(fileName, repetation=3):
    '''
    read the file and turns into array.
    :param fileName: file name
    :param repetation: which indicate how many time it iterate code,by default is 3
    :return: None
    '''
    global line, y, x, f_name, flag, main_repetation, arr
    ls = []
    main_repetation = repetation
    f_name = fileName.removesuffix('.txt')

    count = 0
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



def checkNeighbour(arr1, repetation):
    '''
    this function count the number of alive neighbours for each cell.
    and makes an array out of it.
    then passes this count array to next function.
    :param arr1: original array
    :param repetation:which indicate how many time it iterate code
    :return: None
    '''
    lifeCount = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            aCount = 0
            # top
            if arr1[i - 1][j] == '*'  and i > 0:
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
    '''
    this function count the how many zombie cell are around each cell
    and turn into an array
    :param arr2: original aray
    :return: array of zombie count
    '''
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
    '''
    addes living and zombie cells as provided conditions.
    along with it adds the elements to new list
    and print the array in consol.
    :param original_arr: original array from file
    :param list_arr: living neighbour around eac cell
    :param repetation: which indicate how many time it iterate code
    :return: None
    '''
    last_ls = []
    call_zombie = zombie_neighbour(original_arr)
    for i in range(len(original_arr)):
        for j in range(len(original_arr[i])):
            living_count = list_arr[i][j] + call_zombie[i][j]
            if living_count < 2 or living_count > 3:
                last_ls.append('-')
            elif (living_count == 2 or living_count == 3) and original_arr[i][j] == '*' and call_zombie[i][j] > 0:
                last_ls.append('Z')
            elif original_arr[i][j] == '*':
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
    '''
    this function open file with name and repetation count and write the data into the file.
    :param final: it is a last output
    :return: None
    '''
    latest_file = f'{f_name}' + "_" + f'{main_repetation}' + "steps.txt"
    f = open(latest_file, "w+")
    for row in final:
        for person in row:
            person = str(person)
            f.write(person)
        f.write('\n')
    f.close()
    print("Program Success...")


# Conway('input4.txt')