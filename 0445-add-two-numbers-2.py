''' https://leetcode.com/problems/add-two-numbers-ii/
'''

from classes import linkedlist
from classes.linkedlist import ListNode

class Solution:
    def addTwoNumbers(self, l1, l2):

        def list_to_n(link):
            value = 0
            curr = link
            while curr:
                value *=10
                value += curr.val
                curr = curr.next
            return value

        def n_to_list(n):
            curr = None
            while n > 0:
                new_link = ListNode(n%10)
                new_link.next = curr
                curr = new_link
                n //= 10
            if curr:
                return curr
            return ListNode(0)

        return n_to_list(list_to_n(l1) + list_to_n(l2))

def main():
    ''' Test the addTwoNumbers
    '''

    test_cases = [
        ([7,2,4,3], [5,6,4]),
        ([2,4,3], [5,6,4]),
        ([0],[0]),
        ([9,9,9,9,9,9],[1])
    ]

    solution = Solution()
    for list_1, list_2 in test_cases:
        l1 = linkedlist.create_linked_list(list_1)
        l2 = linkedlist.create_linked_list(list_2)
        print(l1, l2)
        print(solution.addTwoNumbers(l1, l2))


if __name__ == "__main__":
    main()
