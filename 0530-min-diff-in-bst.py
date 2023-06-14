''' https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def getMinimumDifference(self, root):


        def recurse(node):
            ''' Return Min Value, Max Value, Min diff so far
            '''

            # End of recursion, return self value and no difference
            if node.left is None and node.right is None:
                return node.val, node.val, float("inf")
            
            # Result placeholders
            minval, maxval, mindiff = float("inf"), float("-inf"), float("inf")

            # For either non-None branches
            for branch in [node.left, node.right]:
                if branch is None:
                    continue

                # Get min, max, diff
                branch_min, branch_max, branch_diff = recurse(branch)

                # Keep track of min amd max in all lower branches
                minval = min(minval, branch_min)
                maxval = max(maxval, branch_max)

                # Keep track of all possible min differences
                # That was either seen blow
                mindiff = min(mindiff, branch_diff)
                # Or between current node and branch'es edge
                mindiff = min(mindiff, abs(node.val - branch_min))
                mindiff = min(mindiff, abs(node.val - branch_max))

            return min(minval, node.val), max(maxval, node.val), mindiff

        _, _, result = recurse(root)

        return result

def main():
    ''' Test getMinimumDifference
    '''
    solution = Solution()

    test_cases = [
        [4,2,6,1,3], # 1
        [1,0,48,None,None,12,49], #1
        [100,10,1000,1,97, 101, 2000], # 1

    ]
    for list_tree in test_cases:
        root = binarytree.level_order_2_tree(list_tree)
        result = solution.getMinimumDifference(root)
        print(str(root)[:50], result)

if __name__ == "__main__":
    main()
