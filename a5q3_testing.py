# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

import a5q3 as file
from treenode import Treenode

# Test cases for ordered() function

test_item = 'ordered()'
tnode = None
expected = True
reason = 'Empty Tree'
result = file.ordered(tnode)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

test_item = 'ordered()'
tnode = Treenode(3)
expected = True
reason = 'Single Tree node'
result = file.ordered(tnode)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

test_item = 'ordered()'
tnode = Treenode(4,
                   Treenode(2, Treenode(1), Treenode(3)),
                   Treenode(6, Treenode(5), Treenode(7)))
expected = True
reason = 'Perfect ordered Tree'
result = file.ordered(tnode)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

test_item = 'ordered()'
tnode = Treenode(4,
                   Treenode(6, Treenode(5), Treenode(7)),
                   Treenode(2, Treenode(1), Treenode(3)))
expected = False
reason = 'non-ordered Tree from level-1'
result = file.ordered(tnode)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

test_item = 'ordered()'
tnode = Treenode(4,
                   Treenode(2, None, Treenode(6)),
                   Treenode(5, Treenode(3), None))
expected = False
reason = 'non-ordered Tree in level-2'
result = file.ordered(tnode)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

print('*** testing complete ***')