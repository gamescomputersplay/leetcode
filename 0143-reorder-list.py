''' https://leetcode.com/problems/reorder-list/
'''

from classes import linkedlist

class Solution:
    def reorderList(self, head):

        # Nothing to do with 0 or 1 links
        if head is None or head.next is None or head.next.next is None:
            return head

        # Count nodes
        curr = head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1            

        # Find the middle
        curr = head
        for _ in range(count // 2 - 1):
            curr = curr.next
        mid = curr.next
        curr.next = None

        # Reverse the second part
        curr = mid
        tail = None
        while curr is not None:
            rev = curr
            curr = curr.next
            rev.next = tail
            tail = rev

        # Combine 2 lists: head and rev
        curr1, curr2 = head.next, rev
        last = head

        while curr1 is not None or curr2 is not None:
            if curr2 is not None:
                last.next = curr2
                last = last.next
                curr2 = curr2.next
            if curr1 is not None:
                last.next = curr1
                last = last.next
                curr1 = curr1.next

        return None

def main():
    ''' Test the reorderList
    '''

    test_cases = [
        list(range(1, i)) for i in range(2, 10)
    ]

    solution = Solution()
    for test_list_data in test_cases:
        root = linkedlist.create_linked_list(test_list_data)
        print(f"IN: {root}")
        solution.reorderList(root)
        print(f"OUT: {root}\n")

if __name__ == "__main__":
    main()
