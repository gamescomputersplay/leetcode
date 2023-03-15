''' https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s):
        
        stack = []

        brackets = {"(": ")", "[": "]", "{": "}"}

        # Go through all characters in the string
        for char in s:

            # Opening bracket: Add to stack
            if char in brackets.keys():
                stack.append(char)
            
            # Closing bracket and stack is not empty
            elif stack:

                # Pop teh last item in stack.
                # It it does not matches the character - return Invalid
                if brackets[stack.pop()] != char:
                    return False

            # Closing bracket with empty stack: return Invalid
            else:
                return False

        # If stack is not empty in the end: return Invalid
        if stack:
            return False
        
        return True

def main():
    ''' Test isValid
    '''
    solution = Solution()

    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "([])",
        "",
        "([]))",
        "(([])",
        "({[]})",
    ]
    for test_case in test_cases:
        result = solution.isValid(test_case)
        print(test_case, result)

if __name__ == "__main__":
    main()
