''' https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''

# Can I just do regular traversal (as in #102) and reverse the result?

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def preorderTraversal(self, root):

        def recursive_preorder(node):

            if node is None:
                return

            result.append(node.val)

            if node.left:
                recursive_preorder(node.left)
            if node.right:
                recursive_preorder(node.right)

        result = []
        recursive_preorder(root)
        return result

def main():
    ''' Test preorderTraversal
    '''
    solution = Solution()

    test_cases = [
        [3,9,20,1,2,15,7],
        [1],
        [],
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.preorderTraversal(tree)
        print(f"{tree} {result}")

if __name__ == "__main__":
    main()
