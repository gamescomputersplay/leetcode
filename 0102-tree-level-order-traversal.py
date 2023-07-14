''' https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def levelOrder(self, root):

        levels = []
        
        def recursive_level(node, level):

            if node is None:
                return 

            if len(levels) < level + 1:
                levels.append([])
            
            levels[level].append(node.val)

            if node.left:
                recursive_level(node.left, level+1)
            if node.right:
                recursive_level(node.right, level+1)

        recursive_level(root, 0)

        return levels

def main():
    ''' Test levelOrder
    '''
    solution = Solution()

    test_cases = [
        [3,9,20,None,None,15,7],
        [1],
        [],
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.levelOrder(tree)
        print(f"{tree} {result}")

if __name__ == "__main__":
    main()
