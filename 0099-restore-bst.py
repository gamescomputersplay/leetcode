''' https://leetcode.com/problems/recover-binary-search-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def recoverTree(self, root):

        def list_nodes(node):
            ''' Linear representation of the tree, as (node, value)
            '''
            if node is None:
                return []
            return list_nodes(node.left) + [node] + list_nodes(node.right)

        # Generate the list of [node, value]
        nodes = list_nodes(root)


        left, right = None, None

        # Find first left value with a problem
        for i in range(len(nodes)-1):
            if nodes[i].val > nodes[i+1].val:
                left = nodes[i]
                break

        # Find first right value with a problem
        for i in range(len(nodes)-1, 0, -1):
            if nodes[i].val < nodes[i-1].val:
                right = nodes[i]
                break

        if left and right:
            left.val, right.val = right.val, left.val

        return None


def main():
    ''' Test recoverTree
    '''
    solution = Solution()

    test_cases = [
        [2,3,1], #1-3
        [1,3,None,None,2], # 1-3
        [3,1,4,None,None,2], # 2-3
        [5, 10, 8, 2, 4, 7, 9, 1, None, None, None, 6, None, None, 3], # 3-10
        [3,None,2,None,1], # 1-3

    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        print(f"IN: {tree}")
        solution.recoverTree(tree)
        print(f"OUT: {tree}\n")

if __name__ == "__main__":
    main()
