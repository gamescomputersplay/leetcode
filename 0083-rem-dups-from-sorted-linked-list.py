''' https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''

from classes import linkedlist

class Solution:
    def deleteDuplicates(self, head):

        # Do nothing for 0 or 1 length lists
        if head is None or head.next is None:
            return head

        current = head
        while current.next is not None:

            next_node = current.next

            # Either cut out the next node
            if next_node.val == current.val:
                current.next = next_node.next
            # Or progress through the list
            else:
                current = next_node

        return head

def main():
    ''' Test the deleteDuplicates
    '''

    test_cases = [
        linkedlist.create_linked_list([1, 2, 3, 4]),
        linkedlist.create_linked_list([1, 1, 1, 2, 3, 4]),
        linkedlist.create_linked_list([1, 2, 3, 4, 4, 4]),
        linkedlist.create_linked_list([1, 2, 2, 2, 3, 4]),
        linkedlist.create_linked_list([]),
        linkedlist.create_linked_list([1]),
        linkedlist.create_linked_list([1, 1]),
        linkedlist.create_linked_list([1, 1, 1]),
        linkedlist.create_linked_list([1, 2, 3, 4]),
        ]

    solution = Solution()
    for linked_list in test_cases:
        print(f"IN: {linked_list}")
        solution.deleteDuplicates(linked_list)
        print(f"OUT: {linked_list}\n")


if __name__ == "__main__":
    main()
