''' https://leetcode.com/problems/binary-tree-postorder-traversal/
'''

# Very similar to 0144

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def postorderTraversal(self, root):

        def recursive_preorder(node):

            if node is None:
                return

            if node.left:
                recursive_preorder(node.left)
            if node.right:
                recursive_preorder(node.right)

            result.append(node.val)

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
        result = solution.postorderTraversal(tree)
        print(f"{tree} {result}")

if __name__ == "__main__":
    main()
