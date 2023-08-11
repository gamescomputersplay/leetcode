''' https://leetcode.com/problems/path-sum-ii/
'''

from classes import binarytree

class Solution:
    def pathSum(self, root, targetSum):

        def check_recursively(node, running_sum):

            # None-existing node is not a solution
            # This is so we don't have to check of branch exists
            if node is None:
                return []

            # This is a leaf
            if node.right is None and node.left is None:
                # And the total sum matches: start the list
                if running_sum + node.val == targetSum:
                    return [[node.val]]
                # Or it doesn't: False
                return []

            new_running_sum = running_sum + node.val

            # Combine possible paths with current value
            out = []
            for path in \
               check_recursively(node.left, new_running_sum) + \
               check_recursively(node.right, new_running_sum):
                out.append([node.val] + path)

            return out

        return check_recursively(root, 0)

def main():
    ''' Test hasPathSum
    '''
    solution = Solution()

    test_cases = [
        ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22),
        ([1,2,3], 5),
        ([], 0),
    ]
    for list_tree, targetSum in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.pathSum(tree, targetSum)
        print(f"{tree}, {targetSum}, {result}")

if __name__ == "__main__":
    main()
