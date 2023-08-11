''' https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''

from classes import binarytree

class Solution:
    def flatten(self, root):

        def recursive_flatten(node):
            ''' Flattern the tree at "node", return the tail
            (rightmost leaf) of the resulting tree
            '''

            # Flatten leaf is the same leaf
            if node.left is None and node.right is None:
                return node

            # Flatten the right branch
            right_tail = None
            if node.right is not None:
                right_tail = recursive_flatten(node.right)

            # Flatten the left branch
            if node.left is not None:
                left_tail = recursive_flatten(node.left)

                if node.right is not None:
                    left_tail.right = node.right
                    node.right = node.left
                    node.left = None
                else:
                    node.right = node.left
                    node.left = None
                    return left_tail

            return right_tail

        recursive_flatten(root)

        return None

def main():
    ''' Test hasPathSum
    '''
    solution = Solution()

    test_cases = [
        [1,2,5,3,4,None,6],
        [0],
        [],
        [1],
        [2, 1],
        [2, None, 3],
        [2, 1, 3]
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        print(f"IN: {tree}")
        solution.flatten(tree)
        print(f"OUT: {tree}\n")

if __name__ == "__main__":
    main()
