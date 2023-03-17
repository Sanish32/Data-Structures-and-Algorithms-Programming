#Your task is to count the number of leaves in a binary tree. 
#
#You may assume that the tree has at most 100 nodes.
#

from collections import namedtuple
def count(node):
    if not node:
        return 0
    if node.left==None and node.right==None:
        return 1
    else:
        return count(node.left)+count(node.right)
 
if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 2