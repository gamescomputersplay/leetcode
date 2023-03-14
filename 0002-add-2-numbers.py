''' https://leetcode.com/problems/add-two-numbers/
'''

from classes import linkedlist

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def pop_link(link):
            ''' Return value and next link.
            0 and the same link, if it is the last one
            '''
            if link:
                return link.val, link.next
            return 0, link

        # Initialize:
        # First: link we'll return in the end
        # Previous: link ready to be extended
        # Carry: 1 if previous sum > 9
        first, previous, carry = None, None, 0

        # Go through 2 pointers until both have ended
        while l1 or l2:

            # Pop the values  from each
            value_1, l1 = pop_link(l1)
            value_2, l2 = pop_link(l2)

            # Calculate value and carry for the current digit
            current_sum = value_1 + value_2 + carry
            current_value, carry = current_sum % 10, current_sum // 10

            # Create a new link with that value
            current = linkedlist.ListNode(current_value)

            # Remember the first link - we'll need to return it
            if first is None:
                first = current
            # Otherwise, connect  to the previous link
            else:
                previous.next = current

            # Current link now ready to accept links
            previous = current

        #  If after going through all digit there is still carry
        # Add last digit "1"
        if carry == 1:
            previous.next = linkedlist.ListNode(1)

        return first

def main():
    ''' Test the twoSum
    '''

    test_cases = [
        (linkedlist.create_linked_list([2, 4, 3]), linkedlist.create_linked_list([5, 6, 4])), # 708
        (linkedlist.create_linked_list([0]), linkedlist.create_linked_list([0])), # 0
        (linkedlist.create_linked_list([9, 9, 9, 9, 9, 9, 9]), linkedlist.create_linked_list([9, 9, 9, 9])), # 10009998
    ]

    solution = Solution()
    for list_1, list_2 in test_cases:
        print(list_1, list_2)
        print(solution.addTwoNumbers(list_1, list_2))


if __name__ == "__main__":
    main()
