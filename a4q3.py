# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442

import node as n

def to_string(node_chain):
    """
        Purpose:
            Create a string representation of the node chain.  E.g.,
            [ 1 | *-]n.Node(1)-->[ 2 | *-]-->[ 3 | / ]
        Pre-conditions:
            :param node_chain:  A node-chain, possibly empty (None)
        Post_conditions:
            None
        Return: A string representation of the nodes.
        """
    if node_chain is None:
        return "Empty"
    else:
        value = node_chain.get_data()
        walker = node_chain.get_next()
        if walker is None:
            return '[ {} | / ]'.format(str(value))
        else:
            result = to_string(walker)
            return '[ {} | *-]-->{}'.format(str(value),result)


print(to_string( n.Node(1, n.Node('two', n.Node(3)))))
