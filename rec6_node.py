# Counts the number of nodes in a node-chain

import node as n

count = 0
def num_node(nodeChain):

    if nodeChain is None:
        return 0
    else:
        return 1+num_node(nodeChain.get_next())


print(num_node(n.Node(5,n.Node(1,n.Node(3)))))
