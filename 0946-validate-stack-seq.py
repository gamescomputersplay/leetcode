''' https://leetcode.com/problems/validate-stack-sequences/
'''

class Solution:
    def validateStackSequences(self, pushed, popped):

        # Stack to simulate
        stack = []
        # Use pointer to go through the pop list
        pop_pointer = 0

        for push in pushed:

            # Append stack
            stack.append(push)

            # Keep popping while can
            while stack and stack[-1] == popped[pop_pointer]:
                stack.pop()
                pop_pointer += 1

        # Valid stack pop sequence will result in an empty stack
        return len(stack) == 0


def main():
    ''' Test validateStackSequences
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,4,5], [4,5,3,2,1]),
        ([1,2,3,4,5], [4,3,5,1,2]),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 4, 5, 3, 2, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 4, 5, 2, 3, 6, 7]),
        ([1,0,3,2], [0,1,2,3]),
    ]
    for pushed, popped in test_cases:
        result = solution.validateStackSequences(pushed, popped)
        print(pushed, popped, result)

if __name__ == "__main__":
    main()
