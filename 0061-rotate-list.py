''' https://leetcode.com/problems/rotate-list/
'''

from classes import linkedlist
from classes.linkedlist import ListNode

class Solution:
    def rotateRight(self, head, k):

        # Sanitize the input
        if head is None:
            return None
        if k == 0:
            return head

        # Count all nodes, get the tail
        current = head
        node_counter = 1
        while current.next != None:
            current = current.next
            node_counter += 1
        tail = current

        # Calculate location of the cut point
        cut_point = (node_counter - k - 1) % node_counter 
        #print(current, node_counter, cut_point)

        # If the cut is supposed to be after the last link - 
        # no cutting needed
        if cut_point == node_counter - 1:
            return head

        # Go to that point
        current = head
        for _ in range(cut_point):
            current = current.next

        #print("cut at", current, current.next)

        # Do the cut and sew old tail to old head
        new_head = current.next
        current.next = None
        tail.next = head

        return new_head

def main():
    ''' Test rotateRight
    '''
    solution = Solution()

    test_cases = [
        (linkedlist.create_linked_list([1,2,3,4,5]), 2),
        (linkedlist.create_linked_list([0,1,2]), 4),
        (linkedlist.create_linked_list([]), 4),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5]), 0),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5]), 1),
        (linkedlist.create_linked_list([1]), 0),
        (linkedlist.create_linked_list([1]), 1),
        (linkedlist.create_linked_list([1, 2]), 1),
        (linkedlist.create_linked_list([1, 2]), 2),
        (linkedlist.create_linked_list([1, 2, 3, 4]), 4),
    ]
    for head, k in test_cases:
        print(f"IN: {head}, {k}")
        result = solution.rotateRight(head, k)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()
