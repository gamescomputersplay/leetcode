''' https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

from classes import linkedlist

class Solution:

    def removeNthFromEnd(self, head, n):

        # One-link list. return None
        # (n is assumed to be always valid)
        if head.next is None:
            return None

        # Count total nodes
        total = 0
        current = head
        while current != None:
            total += 1
            current = current.next

        # Head is to be removed, return second link
        if n == total:
            return head.next

        # Find link before the cut
        before = head
        for _ in range(total-n-1):
            before = before.next

        # Last link to be removed
        if n == 1:
            before.next = None
            return head

        # We need to cut and saw the list
        # The one ofter the cut is 2 links forward
        after = before.next
        after = after.next

        before.next = after

        return head

    def removeNthFromEndOnePass(self, head, n):

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
        #print("OUT:", solution.removeNthFromEndOnePass(list_1, n), "\n")
        print("OUT:", solution.removeNthFromEnd(list_1, n), "\n")

def test_large_list(size):
    ''' Test one large list with timing
    '''
    solution = Solution()
    test_list = linkedlist.create_linked_list([i for i in range(size)])
    the_node = size //2
    start = time.time()
    #solution.removeNthFromEndOnePass(test_list, the_node)
    solution.removeNthFromEnd(test_list, the_node)
    elapsed = time.time() - start
    print(f"{size}: {elapsed}")

def test_speed():
    for power in range(20, 25):
        test_large_list(2** power)


if __name__ == "__main__":
    import time
    #main()
    test_speed()
