''' https://leetcode.com/problems/swap-nodes-in-pairs/
'''

from classes import linkedlist

class Solution:
    def swapPairs(self, head):

        # Do nothing with 0 or 1 links
        if head is None or head.next is None:
            return head

        # Running end of the restructured list
        previous = None

        # We'll break out when encounter None as .next
        while True:

            # left and right are links to be swopped
            # It means left and right BEFORE the swap

            # Initiation for the first link
            if previous is None:
                left = head
            # For all other links
            else:
                left = previous.next
                # Links ended, out
                if left is None:
                    return new_head
                
            right = left.next
            # Links ended and the last one is an odd one anyway, out
            if right is None:
                return new_head

            # THE SWAP
            left.next, right.next = right.next, left

            # Initial setup for processed part
            if previous is None:
                previous = right
                new_head = right
            # Attaching the swapped links to the already processed part
            else:
                previous.next = right

            # Resetting "previous" for the next cycle
            previous = left


def main():
    ''' Test the swapPairs
    '''

    test_cases = [
        linkedlist.create_linked_list([1, 2, 3, 4, 5]),
        linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]),
        None,
        linkedlist.create_linked_list([1]),
    ]

    solution = Solution()
    for nodelist in test_cases:
        print(f"IN: {nodelist}")
        result = solution.swapPairs(nodelist)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()