"""
Your task is to count the number of nodes on a given level of a binary tree. 

The root is at level 1, its children are at level 2, etc.. 

You may assume that the tree has at most 100 nodes.
"""

from collections import namedtuple
 
def count(node, level):
    if not node:
        return 0
    if level==1:
        return 1
    return count(node.left,level-1)+count(node.right,level-1)
   
if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree,1)) # 1
    print(count(tree,2)) # 1
    print(count(tree,3)) # 2
    print(count(tree,4)) # 0