''' https://leetcode.com/problems/validate-binary-search-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def isValidBST(self, root):

        def rec_validate(node):
            ''' Recursively check on the branches. Return min_value, max_value, is_valid
            '''
            if node.left is None and node.right is None:
                return node.val, node.val, True

            minval, maxval = node.val, node.val

            if node.left is not None:
                lmin, lmax, lval = rec_validate(node.left)
                if not lval or lmax >= node.val:
                    return 0, 0, False
                minval = min(minval, lmin)

            if node.right is not None:
                rmin, rmax, rval = rec_validate(node.right)
                if not rval or rmin <= node.val:
                    return 0, 0, False
                maxval = max(maxval, rmax)

            return minval, maxval, True

        _, _, result = rec_validate(root)
        return result

def main():
    ''' Test isValidBST
    '''
    solution = Solution()

    test_cases = [
        [2,1,3],
        [2, 1, 4, None, None, 3],
        [1],
        [5,1,4,None,None,3,6],

    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.isValidBST(tree)
        print(str(tree)[:50], result)

if __name__ == "__main__":
    main()
