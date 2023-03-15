''' https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

from classes import linkedlist

class Solution:
    def removeNthFromEnd(self, head, n):

        # One-link list. return None
        # (n is assumed to be always valid)
        if head.next is None:
            return None

        # Make a list of all nodes
        nodelist = []
        current = head
        while current != None:
            nodelist.append(current)
            current = current.next

        # Head is to be removed, return second link
        if n == len(nodelist):
            return nodelist[1]

        # Tail is to be removed, remove last link
        if n == 1:
            nodelist[-2].next = None
            return head

        # Otherwise saw together parts left and right of the removed link
        nodelist[-n-1].next = nodelist[-n+1]
        return head

def main():
    ''' Test the twoSum
    '''

    test_cases = [
        (linkedlist.create_linked_list([2, 4, 3]), 2), # 2-3
        (linkedlist.create_linked_list([1]), 1), # []
        (linkedlist.create_linked_list([1, 2, 3, 4, 5]), 1), # 1-2-3-5
        (linkedlist.create_linked_list([1, 2, 3, 4, 5]), 2), # 1-2-3-5
        (linkedlist.create_linked_list([1, 2, 3, 4, 5]), 5), # 1-2-3-5

    ]

    solution = Solution()
    for list_1, n in test_cases:
        print("IN:", list_1, n)
        print("OUT:", solution.removeNthFromEnd(list_1, n), "\n")


if __name__ == "__main__":
    main()
