''' https://leetcode.com/problems/minimum-depth-of-binary-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def minDepth(self, root):

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

def main():
    ''' Test recoverTree
    '''
    solution = Solution()

    test_cases = [
        [3,9,20,None,None,15,7],
        [2,None,3,None,4,None,5,None,6],
        [],
        [1,2],
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.minDepth(tree)
        print(f"{tree}, {result}")

if __name__ == "__main__":
    main()
