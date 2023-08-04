# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

import exampletrees as ex


def subst(tnode, t, r):
    '''
    Substitute target value t with replacement value r wherever it appears in the given tree.

    :param tnode: The root node of the tree where the substitution will take place.
    :param t: The target value that needs to be replaced in the tree.
    :param r: The replacement value that will replace occurrences of the target value.
    :return: None
    '''
    if tnode == None:
        return 0
    x = tnode.get_data()
    if x == t:
        x = tnode.set_data(r)
    subst(tnode.get_right(), t, r)
    subst(tnode.get_left(), t, r)


print(subst(ex.xtree, 5, 3))
print(ex.xtree.get_data())
