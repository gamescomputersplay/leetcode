''' https://leetcode.com/problems/merge-k-sorted-lists/
'''

from classes import linkedlist
from classes.linkedlist import ListNode

class Solution:
    def mergeKLists(self, lists):

        # Sanitation and creating a copy: remove lists with no links
        lists_copy = []
        for a_list in lists:
            if a_list:
                lists_copy.append(a_list)

        # Return None if sanitized list is empty
        if not lists_copy:
            return None

        # Sort the initial lists by value
        lists_copy.sort(key=lambda x: x.val)

        # Convert list into a linked list
        head = ListNode(lists_copy[0])
        current = head
        for another_list in lists_copy[1:]:
            new_link = ListNode(another_list)
            current.next = new_link
            current = new_link

        # These two will be used to construct final sorted linked list
        result_head = None
        result_current = None


        while head is not None:

            # Pop the smallest element (first link of the first list)
            smallest_link = head.val

            # Use it to construct resulting sorted list
            if result_head is None:
                result_head = smallest_link
                result_current = result_head
            else:
                result_current.next = smallest_link
                result_current = smallest_link

            # Replace it with the next link
            if smallest_link.next is not None:
                head.val = smallest_link.next
            # Or, if first linked list ends, use the second link
            else:
                head = head.next

            if head is None:
                break

            if head.next is None:
                continue

            # Move the head to an appropriate place down the list

            # First, find the place
            move_after = head
            move_before = head.next

            while move_before is not None and head.val.val > move_before.val.val:
                move_before = move_before.next
                move_after = move_after.next

            # If head has to be moved after itself,
            # it means nothing has to be moved anywhere
            if head == move_after:
                continue

            # Other wise, do the moving
            # Move head one link
            old_head = head
            head = head.next

            # Move former head into an appropriate place
            move_after.next = old_head
            old_head.next = move_before

        return result_head
    

def main():
    ''' Test the mergeKLists
    '''

    test_cases = [
        [
            linkedlist.create_linked_list([1,4,5]),
            linkedlist.create_linked_list([2,6]),
            linkedlist.create_linked_list([1,3,4]),
        ],

        [
            linkedlist.create_linked_list([1,4,5]),
            linkedlist.create_linked_list([]),
            linkedlist.create_linked_list([1,3,4]),
        ],
         [
            linkedlist.create_linked_list([1,2,3,4,5,6,7,8,9,]),
            linkedlist.create_linked_list([1,2,3,4,5,6,7,8,9,]),
            linkedlist.create_linked_list([1,2,3,4,5,6,7,8,9,]),
        ],
         [
            linkedlist.create_linked_list([1,2,3]),
            linkedlist.create_linked_list([4,5,6]),
            linkedlist.create_linked_list([7,8,9]),
        ],
         [
            linkedlist.create_linked_list([1,2,3, 4, 5]),
        ],
        [],
        [[]],
    ]

    solution = Solution()
    for lists in test_cases:

        print(f"IN: {[str(l) for l in lists]}")
        result = solution.mergeKLists(lists)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()