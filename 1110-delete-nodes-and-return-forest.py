'''https://leetcode.com/problems/delete-nodes-and-return-forest/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def delNodes(self, root, to_delete):

        def process_tree(node):
            if node is None:
                return None

            # Node itself is to be deleted
            if node.val in to_delete:
                to_process.append(node.left)
                to_process.append(node.right)
                return None

            # Left child to be deleted
            if node.left is not None and node.left.val in to_delete:
                    to_process.append(node.left)
                    node.left = None
            else:
                 process_tree(node.left)

            # Right child to be deleted
            if node.right is not None and node.right.val in to_delete:
                    to_process.append(node.right)
                    node.right = None
            else:
                 process_tree(node.right)

            return node
        
        # Stack of trees to process
        to_process = [root,]

        # resulting forest
        forest = []

        while to_process:
            current_tree = to_process.pop()
            current_tree = process_tree(current_tree)
            if current_tree is not None:
                forest.append(current_tree)

        return forest
        
def main():
    ''' Test delNodes
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,4,5,6,7], [3,5]),
        ([1,2,4,None,3], [3]),
    ]
    for list_tree, to_delete in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        print(tree)
        result = solution.delNodes(tree, to_delete)
        result_str = ", ".join([str(r) for r in result])
        print(f"{to_delete}, {result_str}\n")

if __name__ == "__main__":
    main()
