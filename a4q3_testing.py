# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442


import a4q3 as node_operation
import node as n

test_item = 'to_string()'
data_in = None
expected = 'EMPTY'
reason = 'Empty node chain'

result = node_operation.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

data_in = n.Node(1)
expected = '[ 1 | / ]'
reason = 'node chain with one node'

result = node_operation.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

data_in = n.Node(1, n.Node('two', n.Node(3)))
expected = '[ 1 | *-]-->[ two | *-]-->[ 3 | / ]'
reason = 'node chain with three nodes'

result = node_operation.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

# unit test case for copy() function
test_item = 'copy()'
data_in = None
expected = None
reason = 'Empty node chain'

result = node_operation.copy(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

data_in = n.Node(1)
expected = '[ 1 | / ]'
reason = 'node chain with one node'
result = node_operation.to_string(node_operation.copy(data_in))
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

data_in = n.Node(1, n.Node('two', n.Node(3)))
expected = '[ 1 | *-]-->[ two | *-]-->[ 3 | / ]'
reason = 'node chain with three nodes'

result = node_operation.to_string(node_operation.copy(data_in))
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

#### UNIT TEST CASE: replace() ####
test_item = "replace()"

chain_in = None
target_in = 1
repl_in = 0
expected_str = "EMPTY"
reason = 'empty node chain'

node_operation.replace(chain_in, target_in, repl_in)
result_str = node_operation.to_string(chain_in)
if result_str != expected_str:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, expected_str, reason))

chain_in = n.Node(1)
target_in = 1
repl_in = 0
expected_str = "[ 0 | / ]"
reason = 'node chain with one node, target replaced'

node_operation.replace(chain_in, target_in, repl_in)
result_str = node_operation.to_string(chain_in)
if result_str != expected_str:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, expected_str, reason))

chain_in = n.Node(1, n.Node(2))
target_in = 1
repl_in = 10
expected_str = "[ 10 | *-]-->[ 2 | / ]"
reason = 'node chain with two nodes, target present first'

node_operation.replace(chain_in, target_in, repl_in)
result_str = node_operation.to_string(chain_in)
if result_str != expected_str:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, expected_str, reason))

print('*** testing complete ***')
