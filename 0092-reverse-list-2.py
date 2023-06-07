''' https://leetcode.com/problems/reverse-linked-list-ii/
'''

from classes import linkedlist

class Solution:
    def reverseBetween(self, head, left, right):

        def reverse_from_head(head, to_reverse):
            ''' Given linked list head, reverse "to_reverse" first links
            '''
            # Old head will be the tail of the reverse part
            reverse_tail = head

            # We'll be switching connection of curr->next pair
            curr = head
            next = head.next

            for _ in range(to_reverse):
                # First, store whatever comes after NEXT
                after_reverse = next.next

                # Do the switch
                next.next = curr

                # Move to the next pair
                curr = next
                next = after_reverse
            # Connect tail to the remainder of the list
            reverse_tail.next = after_reverse

            # Return last link of the reversed pair (it is curr now)
            return curr

        if left == right:
            return head

        # If reverse part starts from the start
        if left == 1:
            return reverse_from_head(head, right - 1)

        # Otherwise, go to the reverse place, and reverse there
        curr = head
        for _ in range(left - 2):
            curr = curr.next
        curr.next = reverse_from_head(curr.next, right - left)

        return head

def main():
    ''' Test the reverseBetween
    '''

    test_cases = [
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 3, 6),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 1, 1),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 1, 2),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 1, 3),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 1, 6),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 1, 7),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 1, 8),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 6, 8),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 4, 5),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5]), 2, 4),
        (linkedlist.create_linked_list([1]), 1, 1),
        (linkedlist.create_linked_list([1, 2]), 1, 2),
    ]

    solution = Solution()
    for head, left, right in test_cases:
        print(f"IN: {head}, {left}, {right}")
        result = solution.reverseBetween(head, left, right)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()
