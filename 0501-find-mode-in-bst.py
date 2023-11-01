''' https://leetcode.com/problems/find-mode-in-binary-search-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def findMode(self, root):


        def traverse(node):
            ''' Traverse the tree
            '''
            if node == None:
                return
            counts[node.val] = counts.get(node.val, 0) + 1
            traverse(node.left)
            traverse(node.right)

        counts = {}
        traverse(root)

        count_to_keep = max(counts.values())
        modes = [val for val, count in counts.items() if count == count_to_keep]

        return modes

def main():
    ''' Test findMode
    '''
    solution = Solution()

    test_cases = [
        [46,31,46,10,36,None,49,8,24,34,42,48,None,4,9,14,25,31,36,41,43,46,None,0,6,None,None,11,20,None,28,None,34,None,None,36,None,None,44,None,None,None,1,5,7,None,12,19,21,25,29,32,None,None,38,None,None,None,3,None,None,None,None,None,14,18,None,None,22,None,27,None,None,None,None,None,39,2,None,None,None,14,None,None,23,None,None,None,41,None,None,None,16,None,None,None,None,None,17],
        [1, 1, 1, 1, 1, 1, 1],
        [5, 5, 5, 1, 3, 7, 7, 1, 1, 3, 3],
        [1,None,2,2],
        [0],

    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.findMode(tree)
        print(f"{tree} {result}")

if __name__ == "__main__":
    main()
