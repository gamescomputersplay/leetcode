''' https://leetcode.com/problems/sort-list/
'''

# They didn't say I can't use built-in sort, did they

from classes import linkedlist

class Solution:
    def sortList(self, head):

        if head is None:
            return head

        array = []

        # Put it all in an array
        while head:
            array.append(head)
            head = head.next

        # Sort
        array.sort(key = lambda x: x.val)

        # Put together again
        for n, link in enumerate(array[:-1]):
            link.next = array[n + 1]
        array[-1].next = None

        return array[0]

def main():
    ''' Test the insertionSortList
    '''

    test_cases = [
        [4,2,1,3],
        [-1,5,3,4,0],
        [],
        [1],
    ]

    solution = Solution()
    for test_list_data in test_cases:
        list_in = linkedlist.create_linked_list(test_list_data)
        print(f"IN: {list_in}")
        list_out = solution.sortList(list_in)
        print(f"OUT: {list_out}\n")

if __name__ == "__main__":
    main()
