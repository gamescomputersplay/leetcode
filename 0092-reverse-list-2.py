''' https://leetcode.com/problems/reverse-linked-list-ii/
'''

from classes import linkedlist

class Solution:
    def reverseBetween(self, head, left, right):

        if left == right:
            return head


        return head

def main():
    ''' Test the reverseBetween
    '''

    test_cases = [
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 3, 6),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 1, 3),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 6, 8),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 4, 5),
        #(linkedlist.create_linked_list([1, 2, 3, 4, 5]), 2, 4),
        #(linkedlist.create_linked_list([1]), 1, 1),
        #(linkedlist.create_linked_list([1, 2]), 1, 2),
    ]

    solution = Solution()
    for head, left, right in test_cases:
        print(f"IN: {head}, {left}, {right}")
        result = solution.reverseBetween(head, left, right)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()
