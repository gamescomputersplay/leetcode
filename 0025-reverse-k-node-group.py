''' https://leetcode.com/problems/reverse-nodes-in-k-group/
'''

from classes import linkedlist

class Solution:
    def reverseKGroup(self, head, k):

        # No action needed with k==1 or 1-link list
        if k == 1 or head.next is None:
            return head

        previous = None
        current = head

        # Need to initiate here in case there will be no reversals
        new_head = head

        while True:

            # Place k links in a buffer
            buffer = []
            for _ in range(k):

                # If there are not enough links to place in a buffer,
                # no reversal needed, return whatever we have so far
                if current is None:
                    return new_head

                buffer.append(current)
                current = current.next

            # Remember where to start from next time
            next_link = current

            # Build the revered part from the buffer
            reversed_part = buffer.pop()
            current = reversed_part
            while buffer:
                link = buffer.pop()
                current.next = link
                current = link

            # Connect last link of the reversed part to
            # the link we have to start with the next time
            current.next = next_link

            # If this is the first time: initiate new head (link to return)
            # and previous (last link to connect future reversed parts to)
            if previous is None:
                new_head = reversed_part

            # Otherwise just connect reversed part to the previously done parts
            else:
                previous.next = reversed_part

            # Set previous and current for the next cycle
            previous = current

            # Next link to start from is now the current link
            current = next_link


def main():
    ''' Test the reverseKGroup
    '''

    test_cases = [
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 1),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 2),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 3),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 4),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 5),
        (linkedlist.create_linked_list([1]), 4),
        (linkedlist.create_linked_list([1, 2]), 4),
        (linkedlist.create_linked_list([1, 2]), 2),
    ]

    solution = Solution()
    for nodelist, k in test_cases:
        print(f"IN: {nodelist}, {k}")
        result = solution.reverseKGroup(nodelist, k)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()