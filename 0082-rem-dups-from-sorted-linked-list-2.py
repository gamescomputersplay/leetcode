''' https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
'''

from classes import linkedlist

class Solution:
    def deleteDuplicates(self, head):

        # Do nothing for 0 or 1 length lists
        if head is None or head.next is None:
            return head

        current = head
        prev = None

        # Will use this one in case we need to cut curent head
        new_head = head

        # Remember the duplicate value, so we can remove all such links
        bad_value = None

        while current.next is not None:

            next_node = current.next

            if next_node.val == current.val:
                bad_value = current.val

            # Cut out all the bad values
            if current.val == bad_value:

                while current.val == bad_value:

                    if prev is not None:
                        prev.next = next_node
                    else:
                        new_head = next_node

                    current = next_node
                    if next_node is None:
                        return new_head
                    next_node = current.next

            else:
            # Or progress through the list
                prev = current
                current = next_node

        return new_head

def main():
    ''' Test the deleteDuplicates
    '''

    test_cases = [
        linkedlist.create_linked_list([1, 2, 3, 4]),
        linkedlist.create_linked_list([1, 1, 2, 2, 3, 3, 4, 4]),
        linkedlist.create_linked_list([1, 1, 2, 2, 3, 4, 4]),
        linkedlist.create_linked_list([1, 1, 1, 2, 3, 4]),
        linkedlist.create_linked_list([1, 2, 3, 4, 4, 4]),
        linkedlist.create_linked_list([1, 2, 2, 2, 3, 4]),
        linkedlist.create_linked_list([]),
        linkedlist.create_linked_list([1]),
        linkedlist.create_linked_list([1, 1]),
        linkedlist.create_linked_list([1, 1, 1]),
        linkedlist.create_linked_list([1, 2, 3, 4]),
        linkedlist.create_linked_list([1,2,3,3,4,4,5]),
        ]

    solution = Solution()
    for linked_list in test_cases:
        print(f"IN: {linked_list}")
        result = solution.deleteDuplicates(linked_list)
        print(f"OUT: {result}\n")


if __name__ == "__main__":
    main()
