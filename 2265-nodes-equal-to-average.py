''' https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def averageOfSubtree(self, root):

        def traverse(node):

            nonlocal count_nodes

            if node.left is None and node.right is None:
                count_nodes += 1
                return node.val, 1

            sum_val = node.val
            sum_count = 1
            for child in (node.left, node.right):
                if child is None:
                    continue
                child_val, child_count = traverse(child)
                sum_val += child_val
                sum_count += child_count

            if sum_val // sum_count == node.val:
                count_nodes += 1

            return sum_val, sum_count

        count_nodes = 0
        traverse(root)

        return count_nodes

def main():
    ''' Test averageOfSubtree
    '''
    solution = Solution()

    test_cases = [
        [4,8,5,0,1,None,6],
        [1],

    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.averageOfSubtree(tree)
        print(f"{tree} {result}")

if __name__ == "__main__":
    main()
