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
        return "EMPTY"
    else:
        value = node_chain.get_data()
        walker = node_chain.get_next()
        if walker is None:
            return '[ {} | / ]'.format(str(value))
        else:
            result = to_string(walker)
            return '[ {} | *-]-->{}'.format(str(value),result)


def copy(node_chain):
    if node_chain is None:
        return "Empty"
    value = node_chain.get_data()
    walker = node_chain.get_next()

    copy_node = n.Node(value)
    copy_node.set_next(copy(walker))
    return copy_node

def replace(node_chain, target, replacement):
    """
        Purpose:
            Replaces each occurrence of the target value with the replacement
        Pre-conditions:
            :param node_chain: a node-chain, possibly empty
            :param target: a value that might appear in the node chain
            :param replacement: the value to replace the target
        Post-conditions:
            Each occurrence of the target value in the chain is replaced with
            the replacement value.
        Return:
            None
        """
    if node_chain is None:
        return 0
    else:
        walker = node_chain
        value_of_node = walker.get_data()
        if value_of_node == target:
            walker.set_data(replacement)
        return replace(walker.get_next(), target, replacement)
