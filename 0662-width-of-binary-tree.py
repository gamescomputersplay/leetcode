''' https://leetcode.com/problems/maximum-width-of-binary-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def widthOfBinaryTree(self, root):

        # List representation code with minor changes copied from my binarytree class

        def add_item(array, item, position):
            ''' Add item to the array at the position "position",
            pad non-exiting position before it with None
            '''
            while len(array) < position:
                array.append(None)
            array.append(item)

        list_representation = []

        queue_pointer = 0
        queue = [(root, 0)]

        while len(queue) > queue_pointer:

            item, item_position = queue[queue_pointer]
            add_item(list_representation, item.val, item_position)

            if item.left is not None:
                queue.append((item.left, item_position * 2 + 1))
            if item.right is not None:
                queue.append((item.right, item_position * 2 + 2))

            queue_pointer += 1

        ## End of the code from binarytree class


        # Not go through the list representation and find
        # max distances within level between non-None elements
        max_width = 0
        level_size = 1
        level_start = 0

        while True:

            leftmost = None
            rightmost = None
            reached_end = False

            for i in range(level_size):

                if level_start + i >= len(list_representation):
                    reached_end = True
                    break
                if leftmost is None and list_representation[level_start + i] is not None:
                    leftmost = i
                if list_representation[level_start + i] is not None:
                    rightmost = i
            if rightmost is not None:
                width = rightmost - leftmost + 1
                max_width = max(max_width, width)
            
            # Set start of the level and level size for the next level
            level_start += level_size
            level_size *= 2

            if reached_end:
                return max_width

        # Should not reach this line
        return 0
    

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
        elapsed = time.time() - time
        print(f"{level_order}, {result}, {elapsed}s\n")

if __name__ == "__main__":
    import time
    main()