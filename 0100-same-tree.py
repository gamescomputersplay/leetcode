''' https://leetcode.com/problems/same-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def isSameTree(self, p, q):

        # Both None: same
        if p is None and q is None:
            return True
        
        # One is None: different
        if p is None or q is None:
            return False
        
        # Value don't match: different
        if p.val != q.val:
            return False
        
        # Finally both branches have to be the same:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    test_tree_a = binarytree.list_2_tree([1, 2, None, 3, 4, None, 5])
    test_tree_b = binarytree.list_2_tree([1, 2, None, 3, 4, None, 5])
    test_tree_c = binarytree.list_2_tree([1, None, 2, None, None, 4, 5])
    solution = Solution()
    print(test_tree_a, test_tree_b, solution.isSameTree(test_tree_a, test_tree_b))
    print(test_tree_b, test_tree_c, solution.isSameTree(test_tree_b, test_tree_c))
