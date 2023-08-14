# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

import numpy as np

ls = []

def Conway(filename):
    '''
    this function reads the file and turn data into array
    then calls the another function and passes the array.
    :param filename: name of file
    :return: none
    '''

    f = open(filename, 'r')
    for line in f:
        line = line.rstrip()
        for i in line:
            ls.append(i)

    # print(ls)
    global x
    x = int(m.sqrt(len(ls)))
    arr = np.array(ls).reshape(x, x)
    f.close()
    return arr

