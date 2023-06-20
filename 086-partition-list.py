''' https://leetcode.com/problems/partition-list/
'''

from classes import linkedlist

class Solution:
    def partition(self, head, x):
        if head is None or head.next is None:
            return head

        less_head, less_tail, more_head, more_tail = None, None, None, None

        curr = head
        while curr is not None:

            if curr.val < x:
                if less_head is None:
                    less_head = curr
                    less_tail = curr
                else:
                    less_tail.next = curr
                    less_tail = curr
            else:
                if more_head is None:
                    more_head = curr
                    more_tail = curr
                else:
                    more_tail.next = curr
                    more_tail = curr

            next = curr.next
            curr.next = None
            curr = next

        if more_head is not None and less_tail is not None:
            less_tail.next = more_head

        if less_head is not None:
            return less_head

        return more_head

def main():
    ''' Test the partition
    '''

    test_cases = [
        (linkedlist.create_linked_list([1,4,3,2,5,2]), 3),
        (linkedlist.create_linked_list([2, 1]), 1),
        (linkedlist.create_linked_list([2, 1]), 2),
        (linkedlist.create_linked_list([]), 2),

        ]

    solution = Solution()
    for linked_list, x in test_cases:
        print(f"IN: {linked_list}, {x}")
        result = solution.partition(linked_list, x)
        print(f"OUT: {result}\n")


if __name__ == "__main__":
    main()
