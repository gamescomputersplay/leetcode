''' https://leetcode.com/problems/linked-list-cycle/
'''

class Solution:
    def hasCycle(self, head):

        seen = set()

        while head is not None:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
