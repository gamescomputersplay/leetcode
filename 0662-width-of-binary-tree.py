''' https://leetcode.com/problems/maximum-width-of-binary-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def widthOfBinaryTree(self, root):

        # Variables to queue nodes and detect their position in the list representation
        queue_pointer = 0
        queue = [(root, 0)]

        # Variables to track level size, width etc
        max_width = 0
        level_size = 1
        level_start = 0
        leftmost = None
        rightmost = None

        while len(queue) > queue_pointer:

            item, position = queue[queue_pointer]

            # Detect width
            # Reset variables for the next level
            if position >= level_start + level_size:

                # Calculate width and maxwidth for this level
                width = rightmost - leftmost + 1
                max_width = max(max_width, width)

                leftmost = None
                rightmost = None

                # Set data for the next level
                level_start += level_size
                level_size *= 2

            
            # Track left and right
            if leftmost is None:
                leftmost = position
            rightmost = position

            # Append to a queue
            if item.left is not None:
                queue.append((item.left, position * 2 + 1))
            if item.right is not None:
                queue.append((item.right, position * 2 + 2))

            queue_pointer += 1


        # Check width for the last time
        width = rightmost - leftmost + 1
        max_width = max(max_width, width)

        return max_width
    

def main():
    ''' Test widthOfBinaryTree
    '''
    solution = Solution()

    test_cases = [
        [1,3,2,5,3, None,9], #4
        [1,3,2,5, None, None,9,6, None,7], #7
        [1,3,2,5], #2
        [1],
        [0,0,0, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None, None,0,0, None],
    ]
    for level_order in test_cases:
        root = binarytree.level_order_2_tree(level_order)
        start = time.time()
        result = solution.widthOfBinaryTree(root)
        elapsed = time.time() - start
        print(f"{level_order}, {result}, {elapsed}s\n")

if __name__ == "__main__":
    import time
    main()