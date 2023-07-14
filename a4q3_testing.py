# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442


import a4q3 as to_string_file
import node as n

test_item = 'to_string()'
data_in = None
expected = 'EMPTY'
reason = 'Empty node chain'

result = to_string_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = n.Node(1)
expected = '[ 1 | / ]'
reason = 'node chain with one node'

result = to_string_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = n.Node(1, n.Node('two', n.Node(3)))
expected = '[ 1 | *-]-->[ two | *-]-->[ 3 | / ]'
reason = 'node chain with three nodes'

result = to_string_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

print('*** testing complete ***')
