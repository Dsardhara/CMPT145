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


def diff_sum_preorder(tnode):
    '''
    Perform a modified preorder traversal of the binary tree, alternately finding the difference and summation
    of values. The value returned will be of the pattern X - Y + Z.
    :param tnode: The root node of the binary tree.
    :return: sum of this X - Y + Z.
    '''

    if tnode is None:
        return 0

    val = tnode.get_data()
    l = diff_sum_preorder(tnode.get_left())
    r = diff_sum_preorder(tnode.get_right())
    sum = val - l + r
    return sum


def diff_sum_inorder(tnode):
    '''
        Perform a modified inorder traversal of the binary tree, alternately finding the difference and summation
        of values. The value returned will be of the pattern X - Y + Z
        :param tnode: The root node of the binary tree for which to perform the traversal.
        :return: final result of X - Y + Z.
        '''

    if tnode is None:
        return 0

    l = diff_sum_inorder(tnode.get_left())
    value = tnode.get_data()
    r = diff_sum_inorder(tnode.get_right())
    total = r - l + value
    return total


def diff_sum_postorder(tnode):
    '''
    Perform a modified postorder traversal of the binary tree, alternately finding the difference and summation
    of values. The value returned will be of the pattern X - Y + Z
    :param tnode: The root node of the binary tree for which to perform the traversal.
    :return: The result of the traversal in the form X - Y + Z.
    '''

    if tnode is None:
        return 0

    x = tnode.get_data()
    y = diff_sum_inorder(tnode.get_right())
    z = diff_sum_inorder(tnode.get_left())

    # Alternating subtraction and addition
    if tnode.get_left() is None:
        return x - y
    elif tnode.get_right() is None:
        return x + z
    else:
        return x - y + z
