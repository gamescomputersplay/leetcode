''' https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''

import math

class Solution:
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            if token in ("+", "-", "*", "/"):
                num = stack.pop()

                if token == "+":
                    stack[-1] += num

                elif token == "-":
                    stack[-1] -= num

                elif token == "*":
                    stack[-1] *= num

                elif token == "/":
                    stack[-1] = math.floor(stack[-1] / num) \
                                if stack[-1] / num > 0 \
                                else math.ceil(stack[-1]/ num)
            else:
                stack.append(int(token))

            # print(token, stack)

        return stack[0]

def main():
    ''' Test evalRPN
    '''
    solution = Solution()

    test_cases = [
        ["2","1","+","3","*"], #9
        ["4","13","5","/","+"], #6
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"], #22

    ]
    for tokens in test_cases:
        result = solution.evalRPN(tokens)
        print(tokens, result)


if __name__ == "__main__":
    main()
