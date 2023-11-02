''' https://leetcode.com/problems/binary-tree-right-side-view/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def rightSideView(self, root):

        def traverse(node, level):
            if len(right_view) < level + 1:
                right_view.append(node.val)
            if node.right:
                traverse(node.right, level + 1)
            if node.left:
                traverse(node.left, level + 1)

        if root is None:
            return []

        right_view = []
        traverse(root, 0)
        return right_view
    
def main():
    ''' Test rightSideView
    '''
    solution = Solution()

    test_cases = [
        [1,2,3,None,5,None,4],
        [1,None,3],
        []

    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.rightSideView(tree)
        print(f"{tree} {result}")

if __name__ == "__main__":
    main()