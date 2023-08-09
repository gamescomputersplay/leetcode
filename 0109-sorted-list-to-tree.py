''' https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
'''

from classes import linkedlist
from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def sortedListToBST(self, head):

        def rec_build_tree(list_head, length):

            # Simple ways to build 0-1-2 node trees
            if list_head is None:
                return None

            if length == 1:
                return TreeNode(list_head.val)

            if length == 2:
                root = TreeNode(list_head.val)
                root.right = TreeNode(list_head.next.val)
                return root

            left = list_head

            # Measure the half
            curr = list_head
            for _ in range(length // 2-1):
                curr = curr.next

            # Cut off the right part
            root = curr.next
            curr.next = None

            # Cut off the middle (root)
            right = root.next
            root.next = None

            # Build the tree
            tree = TreeNode(root.val)
            tree.left = rec_build_tree(left, length // 2)
            tree.right = rec_build_tree(right, (length - 1) // 2)

            return tree

        # Measure the length
        total_length = 0
        curr = head
        while curr is not None:
            total_length += 1
            curr = curr.next

        node = rec_build_tree(head, total_length)

        return node

def main():
    ''' Test the reverseBetween
    '''

    test_cases = [
        linkedlist.create_linked_list(list(range(1, i+1))) for i in range(1, 11)
    ]

    solution = Solution()
    for head in test_cases:
        print(f"IN: {head}")
        result = solution.sortedListToBST(head)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()
