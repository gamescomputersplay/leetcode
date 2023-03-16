''' https://leetcode.com/problems/merge-k-sorted-lists/
'''

from classes import linkedlist
from classes.linkedlist import ListNode

class Solution:
    def mergeKLists(self, lists):

        # Sanitation: remove lists with no links
        for i in range(len(lists)):
            if not lists[i]:
                del lists[i]

        # Return None if input list is empty
        if not lists:
            return None

        # Sort the initial lists by value
        lists.sort(key=lambda x: x.val)

        # Convert list into a linked list
        head = ListNode(lists[0])
        current = head
        for another_list in lists[1:]:
            new_link = ListNode(another_list)
            current.next = new_link
            current = new_link

        print(head)

        result = None


        while head is not None:
            print(head)

            # Pop the smallest element (first link of the first list)
            smallest_link = head.val
            print(smallest_link.val)

            # Replace it with the next link
            if smallest_link.next is not None:
                head.val = smallest_link.next
            # Or, if first linked list ends, use the second link
            else:
                head = head.next

            # Move the head to an appropriate place down the list

        return result
    

def main():
    ''' Test the mergeKLists
    '''

    test_cases = [
        [
            linkedlist.create_linked_list([1,4,5]),
            linkedlist.create_linked_list([2,6]),
            linkedlist.create_linked_list([1,3,4]),
        ],
        #[],
        #[[]],
    ]

    solution = Solution()
    for lists in test_cases:

        print(f"IN: {[str(l) for l in lists]}")
        result = solution.mergeKLists(lists)
        print(f"OUT:{result}\n")

if __name__ == "__main__":
    main()