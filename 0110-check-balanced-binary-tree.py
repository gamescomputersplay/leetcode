''' https://leetcode.com/problems/balanced-binary-tree/
'''

class Solution:
    def isBalanced(self, root):

        def recursve_check(node):

            if node is None:
                return 0, True

            left_depth, left_balanced = recursve_check(node.left)
            right_depth, right_balanced = recursve_check(node.right)

            return max(left_depth, right_depth) + 1, \
                left_balanced and right_balanced and abs(left_depth - right_depth) < 2


        _, is_balanced = recursve_check(root)

        return is_balanced
