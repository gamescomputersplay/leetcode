''' https://leetcode.com/problems/merge-k-sorted-lists/
'''

from classes import linkedlist

class Solution:
    def mergeKLists(self, lists):
        return []
    

def main():
    ''' Test the mergeKLists
    '''

    test_cases = [
        [
            linkedlist.create_linked_list([1,4,5]),
            linkedlist.create_linked_list([1,3,4]),
            linkedlist.create_linked_list([2,6])
        ],
        [],
        [[]],
    ]

    solution = Solution()
    for lists in test_cases:
        print(f"IN: {[str(l) for l in lists]}\nOUT:{solution.mergeKLists(lists)}\n")


if __name__ == "__main__":
    main()