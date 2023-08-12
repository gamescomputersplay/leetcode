''' https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''

from classes import binarytree

class Solution:
    def sumNumbers(self, root):

        def recursive_count(node, so_far):

            nonlocal total

            so_far *= 10
            so_far += node.val

            if node.left is None and node.right is None:
                total += so_far
                return

            if node.left is not None:
                recursive_count(node.left, so_far)
            if node.right is not None:
                recursive_count(node.right, so_far)

        total = 0
        recursive_count(root, 0)
        return total

def main():
    ''' Test sumNumbers
    '''
    solution = Solution()

    test_cases = [
        [1,2,3],
        [4,9,0,5,1],
        [1],
        [1, 2],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.sumNumbers(tree)
        print(f"{list_tree}, {result}")

if __name__ == "__main__":
    main()
