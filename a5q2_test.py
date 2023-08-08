# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

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
reason = 'single node tree value replaced target value '
main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))
## third

test_item = 'subst()'
tnode = tn.Treenode(3, tn.Treenode(5, tn.Treenode(9, None)), tn.Treenode(10, tn.Treenode(11, None)))
t = 9
r = 0
expected_tree = tn.Treenode(3, tn.Treenode(5, tn.Treenode(0, None)), tn.Treenode(10, tn.Treenode(11, None)))
reason = 'more than one node targeted value changed'
main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

### Test Case for copy(tnode)
## First
test_item = 'copy()'
tnode = None
expected_tree = None
reason = 'Empty binary tree'
result = main.copy(tnode)

if check_tree.to_string(expected_tree) != check_tree.to_string(result):
    print('Test1 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

## second
test_item = 'copy()'
tnode = tn.Treenode(3)
expected_tree = tn.Treenode(3)
reason = 'tree with single node'
main.copy(tnode)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

## third
test_item = 'tree with more than one node'
tnode = tn.Treenode(3, tn.Treenode(5, tn.Treenode(9, None)), tn.Treenode(10, tn.Treenode(11, None)))
expected_tree = tn.Treenode(3, tn.Treenode(5, tn.Treenode(9, None)), tn.Treenode(10, tn.Treenode(11, None)))
reason = 'tree with more than node'
main.copy(tnode)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

### Test Case for diff_sum_preorder(tnode)
# First
test_item = 'diff_sum_preorder()'
tnode = None
expected_tree = None
reason = 'Empty binary tree'
main.diff_sum_preorder(tnode)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test1 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

## second
test_item = 'diff_sum_preorder()'
tnode = tn.Treenode(3)
expected_tree = 3
reason = 'tree with single node'
result = main.diff_sum_preorder(tnode)

if expected_tree != result:
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

## third
test_item = 'diff_sum_preorder()'
tnode = tn.Treenode(5,tn.Treenode(2,tn.Treenode(1,None,None),
                                     tn.Treenode(1,tn.Treenode(0,None,None),
                                                 tn.Treenode(1,None,None))),
                         tn.Treenode(3,tn.Treenode(1,tn.Treenode(0,None,None),
                                                 tn.Treenode(1,None,None)),
                                     tn.Treenode(2,tn.Treenode(1,None,None),
                                                 tn.Treenode(1,tn.Treenode(0,None,None),
                                                             tn.Treenode(1,None,None)))))
expected_tree =6
reason = 'tree with more than one node'
result = main.diff_sum_preorder(tnode)
if expected_tree != result:
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))


### Test Case for diff_sum_inorder(tnode)
## First

test_item = 'diff_sum_inorder()'
tnode = None
expected_tree = 0
reason = 'tree with empty node'
result = main.diff_sum_inorder(tnode)

if expected_tree != result:
    print('Test1  failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

## second

test_item = 'diff_sum_inorder()'
tnode = tn.Treenode(3)
expected_tree = 3
reason = 'tree with single node'
result = main.diff_sum_inorder(tnode)

if expected_tree != result:
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))



### Test Case for diff_sum_postorder(tnode)
## First

test_item = 'diff_sum_postorder()'
tnode = None
expected_tree = 0
reason = 'tree with empty node'
result = main.diff_sum_postorder(tnode)

if expected_tree != result:
    print('Test1  failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

## second
test_item = 'diff_sum_postorder()'
tnode = tn.Treenode(3)
expected_tree = 3
reason = 'tree with single node'
result = main.diff_sum_postorder(tnode)

if expected_tree != result:
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

## third
test_item = 'diff_sum_postorder()'
tnode = tn.Treenode(5,tn.Treenode(2,tn.Treenode(1,None,None),
                                     tn.Treenode(1,tn.Treenode(0,None,None),
                                                 tn.Treenode(1,None,None))),
                         tn.Treenode(3,tn.Treenode(1,tn.Treenode(0,None,None),
                                                 tn.Treenode(1,None,None)),
                                     tn.Treenode(2,tn.Treenode(1,None,None),
                                                 tn.Treenode(1,tn.Treenode(0,None,None),
                                                             tn.Treenode(1,None,None)))))
expected_tree =4
reason = 'tree with more than one node'
result = main.diff_sum_postorder(tnode)
if expected_tree != result:
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))
