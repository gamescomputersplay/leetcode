''' https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root):
        
        def recursive_zigzag(node):
    
            if node.left is not None:
                left_zigzag = max(1 + recursive_zigzag(node.left)[1], recursive_zigzag(node.left)[0])
            else:
                left_zigzag = 0

            if node.right is not None:
                right_zigzag = max(1 + recursive_zigzag(node.right)[0], recursive_zigzag(node.right)[1])
            else:
                right_zigzag = 0

            return left_zigzag, right_zigzag

        return max(recursive_zigzag(root))


### Failed case
# [6,9,7,3,null,2,8,5,8,9,7,3,9,9,4,2,10,null,5,4,3,10,10,9,4,1,2,null,null,6,5,null,null,null,null,9,null,9,6,5,null,5,null,null,7,7,4,null,1,null,null,3,7,null,9,null,null,null,null,null,null,null,null,9,9,null,null,null,7,null,null,null,null,null,null,null,null,null,6,8,7,null,null,null,3,10,null,null,null,null,null,1,null,1,2]
