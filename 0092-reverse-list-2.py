''' https://leetcode.com/problems/reverse-linked-list-ii/
'''

from classes import linkedlist

class Solution:
    def reverseBetween(self, head, left, right):

        if left == right:
            return head

        # count to reserse point
        curr = head
        for _ in range(left - 2):
            curr = curr.next

        last_before_reverse = curr
        prev = last_before_reverse.next
        reverse_tail = prev
        last_before_reverse.next = None
        curr = prev.next

        # Do the reverse
        for _ in range(right - left):
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        last_before_reverse.next = prev
        reverse_tail.next = curr

        return head

def main():
    ''' Test the reverseBetween
    '''

    test_cases = [
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 3, 6),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 2, 3),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5]), 2, 4),
        (linkedlist.create_linked_list([1]), 1, 1),
        #(linkedlist.create_linked_list([1, 2]), 1, 2),
    ]

    solution = Solution()
    for head, left, right in test_cases:
        print(f"IN: {head}, {left}, {right}")
        result = solution.reverseBetween(head, left, right)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()
