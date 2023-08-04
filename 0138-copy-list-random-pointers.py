''' https://leetcode.com/problems/copy-list-with-random-pointer/
'''


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):

        # Edge case: no links
        if head is None:
            return None

        # This dict will keep connections {original link: copied link}
        old_new = {}

        # Start copying with the head
        new_head = Node(head.val)
        new_tail = new_head

        # Starty keeping {old: new} connections
        old_new[head] = new_head

        # Do it for the whole list
        curr = head.next
        while curr is not None:
            new_tail.next = Node(curr.val)
            new_tail = new_tail.next
            old_new[curr] = new_tail
            curr = curr.next

        # Go through the list again and set the links to random nodes
        # using old:new data
        curr = head
        new_curr = new_head
        while curr is not None:
            if curr.random is not None:
                new_curr.random = old_new[curr.random]
            curr = curr.next
            new_curr = new_curr.next

        return new_head
