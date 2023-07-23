''' https://leetcode.com/problems/all-possible-full-binary-trees/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:

    def __init__(self):
        self.cache = {}

    def allPossibleFBT(self, n):

        if n in self.cache:
            return self.cache[n]

        # Cases where only 1 option is possible
        if n == 1:
            self.cache[n] =[TreeNode(0)]
            return self.cache[n]
        if n == 3:
            node = TreeNode(0)
            node.left = TreeNode(0)
            node.right = TreeNode(0)
            self.cache[n] = [node]
            return self.cache[n]

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
                    node.left = left_option
                    node.right = right_option
                    result.append(node)

        self.cache[n] = result
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
