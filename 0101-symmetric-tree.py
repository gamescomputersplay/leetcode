''' https://leetcode.com/problems/symmetric-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def isSymmetric(self, root):

        def are_symmetric(node1, node2):
            # Both Nones are symmetric
            if node1 is None and node2 is None:
                return True
            # Only one None is not
            if node1 is None or node2 is None:
                return False
            # Different values are not symmetric
            if node1.val != node2.val:
                return False

            # Not let's check the symmetry of their children
            # They has to be crross-symmetrical
            if are_symmetric(node1.left, node2.right) and \
               are_symmetric(node1.right, node2.left):
                return True
            return False

        return are_symmetric(root.left, root.right)

def main():
    ''' Test isSymmetric
    '''
    solution = Solution()

    test_cases = [
        [1,2,2,3,4,4,3],
        [1,2,2,None,3,None,3],
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.isSymmetric(tree)
        print(f"{tree} {result}")

if __name__ == "__main__":
    main()
