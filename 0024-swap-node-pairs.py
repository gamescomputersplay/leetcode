''' https://leetcode.com/problems/swap-nodes-in-pairs/
'''

from classes import linkedlist

class Solution:
    def swapPairs(self, head):
        return None

def main():
    ''' Test the swapPairs
    '''

    test_cases = [
        linkedlist.create_linked_list([1, 2, 3, 4, 5, 6]),
        None,
        linkedlist.create_linked_list([1]),
    ]

    solution = Solution()
    for nodelist in test_cases:
        print(f"IN: {nodelist}")
        result = solution.swapPairs(nodelist)
        print(f"OUT: {result}\n")

if __name__ == "__main__":
    main()