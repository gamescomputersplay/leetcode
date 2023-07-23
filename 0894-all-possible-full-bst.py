''' https://leetcode.com/problems/all-possible-full-binary-trees/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def copy(self, node):
        ''' Copy a BST
        '''
        if node is None:
            return None
        node_copy = TreeNode(0)
        node_copy.left = self.copy(node.left)
        node_copy.right = self.copy(node.right)
        return node_copy

    def allPossibleFBT(self, n):

        # Cases where only 1 option is possible
        if n == 1:
            return [TreeNode(0)]
        if n == 3:
            node = TreeNode(0)
            node.left = TreeNode(0)
            node.right = TreeNode(0)
            return [node]

        # If n == 5+, go through ways to distribute
        # those pairs of nodes among 2 children nodes
        result = []
        for n_left in range(1, n, 2):

            n_right = n - 1 - n_left

            left_options = self.allPossibleFBT(n_left)
            right_options = self.allPossibleFBT(n_right)

            for left_option in left_options:
                for right_option in right_options:

                    node = TreeNode(0)
                    node.left = self.copy(left_option)
                    node.right = self.copy(right_option)
                    result.append(node)

        return result

def main():
    ''' Test allPossibleFBT
    '''
    solution = Solution()

    test_cases = [
        1, 3, 5, 7
    ]
    for n in test_cases:
        result = solution.allPossibleFBT(n)
        print(n)
        for tree in result:
            print("    ", tree)

if __name__ == "__main__":
    main()
