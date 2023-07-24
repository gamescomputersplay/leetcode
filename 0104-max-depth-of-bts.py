''' https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def maxDepth(self, root):

        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

def main():
    ''' Test maxDepth
    '''
    solution = Solution()

    test_cases = [
        [3,9,20,None,None,15,7], #3
        [1,None,2], #2
        [1], #1
        [], #0
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.maxDepth(tree)
        print(f"{tree} {result}")

if __name__ == "__main__":
    main()
