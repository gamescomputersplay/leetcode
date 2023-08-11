''' https://leetcode.com/problems/path-sum/
'''

from classes import binarytree

class Solution:
    def hasPathSum(self, root, targetSum):

        def check_recursively(node, running_sum):

            # None-existing node is not a solution
            # This is so we don;t have to check of branch exists
            if node is None:
                return False

            # This is a leaf
            if node.right is None and node.left is None:
                # And the total sum matches: True
                if running_sum + node.val == targetSum:
                    return True
                # Or it doesn't: False
                return False

            new_running_sum = running_sum + node.val

            # Return True if either of children return True
            return check_recursively(node.left, new_running_sum) or \
                   check_recursively(node.right, new_running_sum)

        return check_recursively(root, 0)

def main():
    ''' Test hasPathSum
    '''
    solution = Solution()

    test_cases = [
        ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22),
        ([1,2,3], 5),
        ([], 0),
    ]
    for list_tree, targetSum in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.hasPathSum(tree, targetSum)
        print(f"{tree}, {targetSum}, {result}")

if __name__ == "__main__":
    main()
