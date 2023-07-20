''' https://leetcode.com/problems/insertion-sort-list/
'''

from classes import linkedlist

class Solution:
    def insertionSortList(self, head):

        # Split into done and to_go
        done = head
        to_go = head.next
        head.next = None

        while to_go:

            # Unlink a link to be sorted
            to_sort = to_go
            to_go = to_go.next
            to_sort.next = None

            # to_sort is the smallest: replacing the first element
            if to_sort.val <= done.val:
                to_sort.next = done
                done = to_sort
                continue

            # find a link, after which to_sort should be placed
            curr = done
            while curr.next and curr.next.val < to_sort.val:
                curr = curr.next
            # Insert to_sort
            to_sort.next = curr.next
            curr.next = to_sort

        return done

def main():
    ''' Test the insertionSortList
    '''

    test_cases = [
        [4,2,1,3],
        [-1,5,3,4,0],
        [1],
        [2, 1, 3, 1],
        [1, 2, 3, 4],
    ]

    solution = Solution()
    for test_list_data in test_cases:
        list_in = linkedlist.create_linked_list(test_list_data)
        print(f"IN: {list_in}")
        list_out = solution.insertionSortList(list_in)
        print(f"OUT: {list_out}\n")

if __name__ == "__main__":
    main()