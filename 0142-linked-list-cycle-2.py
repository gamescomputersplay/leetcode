''' https://leetcode.com/problems/linked-list-cycle-ii/
'''

class Solution:
    def detectCycle(self, head):

        seen = set()

        while head is not None:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None
