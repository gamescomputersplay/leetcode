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


    def sortList_merge(self, head):

        def get_length(node):

            count = 0
            curr = node
            while curr:
                curr = curr.next
                count += 1
            return count

        def split_list(node, length):

            list1 = node

            curr = node
            for _ in range(length // 2 - 1):
                curr = curr.next

            list2 = curr.next
            curr.next = None

            return list1, list2

        def merge(list1, list2):

            head = None

            while list1 or list2:

                # Get the next smallest link
                if list1 is None:
                    next_link = list2
                    list2 = list2.next
                elif list2 is None:
                    next_link = list1
                    list1 = list1.next
                elif list1.val < list2.val:
                    next_link = list1
                    list1 = list1.next
                else:
                    next_link = list2
                    list2 = list2.next

                # Attach smallest link to whatever we have
                next_link.next = None

                if head is None:
                    head = next_link
                    tail = next_link
                else:
                    tail.next = next_link
                    tail = next_link

            return head

        def mergesort(node):

            length = get_length(node)

            # End the recursion with 1-nod elist
            if length == 1:
                return node

            # Split list in 2
            list1, list2 = split_list(node, length)

            list1 = mergesort(list1)
            list2 = mergesort(list2)

            return merge(list1, list2)

        if head is None:
            return head
        return mergesort(head)


def main():
    ''' Test the insertionSortList
    '''

    test_cases = [
        [4, 2, 3, 1],
        [-1,5,3,4,0],
        [],
        [1],
        [2, 1]
    ]

    solution = Solution()
    for test_list_data in test_cases:
        list_in = linkedlist.create_linked_list(test_list_data)
        print(f"IN: {list_in}")
        list_out = solution.sortList(list_in)
        print(f"OUT: {list_out}\n")

if __name__ == "__main__":
    main()
