# Tree:
#           1
#       /      \
#      2        3
#     / \      / \
#    4   5    6   7
#            /     \
#           8       9

#   Target Node: 9
#   Output: 7, 3, 1

#   Target Node: 5
#   Output: 2, 1

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def getAncestorNodes(rootNode, targetNode):
    def helper(currNode):
        if currNode is None:
            return False

        if currNode is targetNode:
            return True

        didFindLeft = helper(currNode.left)
        didFindRight = helper(currNode.right)

        if didFindLeft or didFindRight:
            print(f"{currNode.value}, ", end =" ")

        return didFindLeft or didFindRight
    helper(rootNode)
    print("")


node9 = Node(9)
node8 = Node(8)
node5 = Node(5)
node4 = Node(4)
node7 = Node(7, right=node9)
node6 = Node(6, left=node8)
node2 = Node(2, left=node4, right=node5)
node3 = Node(3, left=node6, right=node7)
node1 = Node(1, left=node2, right=node3)

getAncestorNodes(node1, node5)

getAncestorNodes(node1, node9)