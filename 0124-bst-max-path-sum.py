''' https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def maxPathSum(self, root):


        def recursive_find_max(node):
            ''' For this node, return two results
            - Max of a chain that you can connect further to its parent
            - Max of a chain that you can't connect anywhere
            '''

            # Use -inf so it would work with max()
            if node is None:
                return float("-inf"), float("-inf")
            # For a leaft if iw a max that you can connect to a parent
            if node.left is None and node.right is None:
                return node.val, float("-inf")

            # Get this paraneters for childrend
            max_with_left_node, max_without_left_node = recursive_find_max(node.left)
            max_with_right_node, max_without_right_node = recursive_find_max(node.right)

            # Chains that you can connect are: left + node, right + node, just node
            max_with_node = max([max_with_left_node + node.val,
                                 max_with_right_node + node.val,
                                 node.val])
            # Chains that you can't connect further: all previous chains that you can't connect,
            # left, right, left + node + right
            max_without_node = max([max_without_left_node, max_without_right_node,
                                    max_with_left_node, max_with_right_node,
                                    max_with_left_node + max_with_right_node + node.val])

            return max_with_node, max_without_node

        max_with_node, max_without_node = recursive_find_max(root)
        return max(max_with_node, max_without_node)

def main():
    ''' Test maxPathSum
    '''
    solution = Solution()

    test_cases = [
        [1,2,3],
        [-10,9,20,None,None,15,7],
        [1],
        [-3],
        [-2,1],
        [1,-2,-3,1,3,-2,None,-1], #3
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.maxPathSum(tree)
        print(f"{tree}, {result}")

if __name__ == "__main__":
    main()
