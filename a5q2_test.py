# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

import exampletrees as ex
import treenode as tn
import a5q2 as main
import provided_treefunctions as check_tree

### Test Case for subst(tnode, t, r)
## First
test_item = 'subst()'
tnode = None
t = 5
r = 999
expected_tree = None
reason = 'Empty binary tree'
result = main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(result):
    print('Test1 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))
## second
test_item = 'subst()'
tnode = tn.Treenode(3)
t = 3
r = 2
expected_tree = tn.Treenode(2)
reason = 'Empty binary tree'
main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))
## third

test_item = 'subst()'
tnode = tn.Treenode(3,tn.Treenode(5,tn.Treenode(9,None)),tn.Treenode(10,tn.Treenode(11,None)))
# print(check_tree.to_string(tnode))
t = 9
r = 0
expected_tree = tn.Treenode(3,tn.Treenode(5,tn.Treenode(0,None)),tn.Treenode(10,tn.Treenode(11,None)))
reason = 'Empty binary tree'
main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))
