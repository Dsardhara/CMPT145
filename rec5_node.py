#  Displays the data values stored in a node-chain

import node as n
def dis_value(nodeChain):
    if nodeChain is None:
        return 'Empty'
    else:
        walker =nodeChain
        value= walker.get_data()
        result = '[ {} |'.format(str(value))
        # print(result)
        walker=nodeChain.get_next()
        value = walker.get_data()
        result += ' *-]-->[ {} | / ]'.format(str(value))
        # print(value)
        print(result)
        return dis_value(walker)
dis_value(n.Node(1, n.Node('two', n.Node(3))))