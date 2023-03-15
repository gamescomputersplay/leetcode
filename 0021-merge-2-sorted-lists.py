''' https://leetcode.com/problems/merge-two-sorted-lists/
'''

from classes import linkedlist

class Solution:
    def mergeTwoLists(self, list1, list2):

        def add_link(pointer):
            nonlocal current, head
            if head is None:
                head = pointer
            else:
                current.next = pointer
            current = pointer
            pointer = pointer.next
            return pointer

        pointer_1 = list1
        pointer_2 = list2
        head = None
        current = None

        while pointer_1 is not None or pointer_2 is not None:

            if pointer_1 is None:
                pointer_2 = add_link(pointer_2)
            elif pointer_2 is None:
                pointer_1 = add_link(pointer_1)
            elif pointer_1.val < pointer_2.val:
                pointer_1 = add_link(pointer_1)
            else:
                pointer_2 = add_link(pointer_2)

        return head

def main():
    ''' Test the mergeTwoLists
    '''

    test_cases = [
        (linkedlist.create_linked_list([2, 4, 5]), linkedlist.create_linked_list([1, 3, 6])), # 
        (linkedlist.create_linked_list([]), linkedlist.create_linked_list([])), # 0
        (linkedlist.create_linked_list([1]), linkedlist.create_linked_list([])), # 0
        (linkedlist.create_linked_list([9, 9, 9, 9, 9, 9, 9]), linkedlist.create_linked_list([9, 9, 9, 9])), # 10009998
    ]

    solution = Solution()
    for list_1, list_2 in test_cases:
        print(list_1, list_2)
        print(solution.mergeTwoLists(list_1, list_2), "\n")


if __name__ == "__main__":
    main()