''' https://leetcode.com/problems/find-largest-value-in-each-tree-row/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def largestValues(self, root):

        def get_largest_val_rec(node):

            if node.left is None and node.right is None:
                return [node.val]

            largest_left = [] if node.left is None else get_largest_val_rec(node.left)
            largest_right = [] if node.right is None else get_largest_val_rec(node.right)

            largest = [node.val]
            for i in range(min(len(largest_left), len(largest_right))):

                largest.append(max(
                    largest_left[i], largest_right[i]
                ))

            if len(largest_left) < len(largest_right):
                largest.extend(largest_right[len(largest_left):])
            if len(largest_left) > len(largest_right):
                largest.extend(largest_left[len(largest_right):])

            return largest

        if root is None:
            return []

        return get_largest_val_rec(root)

def main():
    ''' Test largestValues
    '''
    solution = Solution()

    test_cases = [
        [1,3,2,5,3,None,9],
        [1,2,3],
        [1],
        None

    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.largestValues(tree)
        print(f"{tree} {result}")

if __name__ == "__main__":
    main()