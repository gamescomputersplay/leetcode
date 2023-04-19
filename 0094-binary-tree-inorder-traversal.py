''' https://leetcode.com/problems/binary-tree-inorder-traversal/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def inorderTraversal(self, root):

        if root is None:
            return []

        result = self.inorderTraversal(root.left) + \
                 [root.val] + \
                 self.inorderTraversal(root.right)

        return result


def main():
    ''' Test inorderTraversal
    '''
    solution = Solution()

    test_cases = [
        [1,None,2,3],
        [],
        [1],
        [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1],
        [1,1,1,None,1,None,None,1,1,None,1],
        [6,9,7,3,None,2,8,5,8,9,7,3,9,9,4,2,10,None,5,4,3,10,10,9,4,1,2,None,None,6,5,None,None,None,None,9,None,9,6,5,None,5,None,None,7,7,4,None,1,None,None,3,7,None,9,None,None,None,None,None,None,None,None,9,9,None,None,None,7,None,None,None,None,None,None,None,None,None,6,8,7,None,None,None,3,10,None,None,None,None,None,1,None,1,2],
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.inorderTraversal(tree)
        print(str(tree)[:50], result)

if __name__ == "__main__":
    main()
