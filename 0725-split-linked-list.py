''' https://leetcode.com/problems/split-linked-list-in-parts/
'''

from classes import linkedlist

class Solution:
    def splitListToParts(self, head, k):

        # Get the length of teh list
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1

        # Size of chunks the list need to be divided into
        chunks = [count // k + 1 if i < count % k else count // k for i in range(k)]
        print(chunks)

        result = []
        curr = head
        for chunk in chunks:

            if chunk == 0:
                result.append(None)
                continue

            result.append(curr)
            for _ in range(chunk - 1):
                curr = curr.next
            next_part = curr.next
            curr.next = None
            curr = next_part

        return result


def main():
    ''' Test the splitListToParts
    '''

    test_cases = [
        (linkedlist.create_linked_list([1,2,3]), 5),
        (linkedlist.create_linked_list(list(range(1, 11))), 3),
        (None, 5)
        ]

    solution = Solution()
    for linked_list, x in test_cases:
        print(f"IN: {linked_list}, {x}")
        result = solution.splitListToParts(linked_list, x)
        print(f"OUT:")
        for item in result:
            print(f"- {item}")


if __name__ == "__main__":
    main()
