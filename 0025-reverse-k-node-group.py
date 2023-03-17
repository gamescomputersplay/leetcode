''' https://leetcode.com/problems/reverse-nodes-in-k-group/
'''

from classes import linkedlist

class Solution:
    def reverseKGroup(self, head, k):
        return None

def main():
    ''' Test the reverseKGroup
    '''

    test_cases = [
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 1),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 2),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 3),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 4),
        (linkedlist.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 5),
        (None, 4),
        (linkedlist.create_linked_list([1]), 4),
    ]

    solution = Solution()
    for nodelist, k in test_cases:
        print(f"IN: {nodelist}, {k}")
        result = solution.reverseKGroup(nodelist, k)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()