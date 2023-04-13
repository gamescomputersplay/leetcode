''' https://leetcode.com/problems/same-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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

# No testing for this one