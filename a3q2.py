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
        NOTE: THIS VERSION OF THE FUNCTION IS KNOWN TO BE BROKEN!!!
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
    else:
        # walk along the chain
        walker = node_chain
        value = walker.get_data()
        # print the data
        result = '[ {} |'.format(str(value))
        while walker is not None:
            walker = walker.get_next()
            if walker is not None:
                value = walker.get_data()
                # represent the next with an arrow-like figure
                result += ' *-]-->[ {} |'.format(str(value))

        # at the end of the chain, use '/'
        result += ' / ]'

    return result

