''' https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from classes import binarytree
from classes.binarytree import TreeNode

class Node(TreeNode):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
      
class Solution:
    def connect(self, root):

        if root is None:
            return None

        last_link=[]

        def recursive(node, level):

            if len(last_link) < level + 1:
                last_link.append(None)

            if last_link[level] is not None:
                last_link[level].next = node
            last_link[level] = node

            if node.left is not None:
                recursive(node.left, level + 1)
                recursive(node.right, level + 1)

        recursive(root, 0)

        return root
    
def main():
    ''' Test connect
    '''
    solution = Solution()

    test_cases = [
        [1,2,3,4,5,6,7],
        [],
        [1]
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.connect(tree)
        print(f"{tree}, {result}")

if __name__ == "__main__":
    main()