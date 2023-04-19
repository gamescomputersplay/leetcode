''' https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def longestZigZag(self, root):
        
        longest_zigzag = 0

        def recursive_zigzag(node):

            nonlocal longest_zigzag
    
            if node.left is not None:
                left_zigzag = 1 + recursive_zigzag(node.left)[1]
            else:
                left_zigzag = 0

            if node.right is not None:
                right_zigzag = 1 + recursive_zigzag(node.right)[0]
            else:
                right_zigzag = 0

            longest_zigzag = max(longest_zigzag, max(left_zigzag, right_zigzag))

            return left_zigzag, right_zigzag

        recursive_zigzag(root)
        return longest_zigzag

def main():
    ''' Test longestZigZag
    '''
    solution = Solution()

    test_cases = [
        [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1], #3
        [1,1,1,None,1,None,None,1,1,None,1], #4
        [1], #0
        [6,9,7,3,None,2,8,5,8,9,7,3,9,9,4,2,10,None,5,4,3,10,10,9,4,1,2,None,None,6,5,None,None,None,None,9,None,9,6,5,None,5,None,None,7,7,4,None,1,None,None,3,7,None,9,None,None,None,None,None,None,None,None,9,9,None,None,None,7,None,None,None,None,None,None,None,None,None,6,8,7,None,None,None,3,10,None,None,None,None,None,1,None,1,2],
    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.longestZigZag(tree)
        print(str(tree)[:50], result)

if __name__ == "__main__":
    main()


