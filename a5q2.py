# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

import exampletrees as ex
import treenode
import provided_treefunctions as q


def subst(tnode, t, r):
    '''
    Substitute target value t with replacement value r wherever it appears in the given tree.

    :param tnode: The root node of the tree where the substitution will take place.
    :param t: The target value that needs to be replaced in the tree.
    :param r: The replacement value that will replace occurrences of the target value.
    :return: None
    '''
    if tnode == None:
        return None
    x = tnode.get_data()
    if x == t:
        x = tnode.set_data(r)
    subst(tnode.get_right(), t, r)
    subst(tnode.get_left(), t, r)


def copy(tnode):
    '''
        Create an exact copy of the given tree, with completely new treenodes, but
        exactly the same data values, in exactly the same places.

        If tnode is None, return None. If tnode is not None, return a reference to the new tree.

        :param tnode: The root node of the tree to be copied.
        :return: A reference to the new tree or None if the original tree is None.
        '''
    nnode = treenode.Treenode
    if tnode == None:
        return None
    nnode = treenode.Treenode(tnode.get_data())
    nnode.set_left(copy(tnode.get_left()))
    nnode.set_right(copy(tnode.get_right()))
    return nnode


print(q.is_leaf(copy(ex.xtree)) == q.is_leaf(ex.xtree))
print(q.to_string(copy(ex.xtree), level=3) == q.to_string(ex.xtree, level=3))
print(q.to_string(copy(ex.xtree), level=1))
print(q.to_string(ex.xtree, level=1))
# print(ex.xtree)
