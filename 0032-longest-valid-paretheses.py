''' https://leetcode.com/problems/longest-valid-parentheses/
'''

class Solution:

    def longestValidParentheses(self, s):

        # Stack to keep track of parentheses in format:
        # [(position: legit length so far), ]
        stack = []

        # How much of legit string we accumulated
        # (in case new "(" starts)
        legit_len_so_far = 0

        # Track max legit string length
        max_legit = 0

        # Go through the string
        for position, char in enumerate(s):

            if char == "(":
                # Add an item, to the stack
                # It means: This is the position of the opening parentheses
                # + this much legit string there was before it
                stack.append((position, legit_len_so_far))
                legit_len_so_far = 0

            elif char == ")" and stack:
                # When a legitimate closing parentheses is found
                legit_start, legit_len_so_far = stack.pop()
                # Legit string is the the part the current parentheses
                # just closed + whatever legit string was before that
                # It will be used for the next opening parentheses
                legit_len_so_far += (position - legit_start + 1)
                # Use it for the max legit string too
                max_legit = max(max_legit, legit_len_so_far)

            else:
                # Illegitimate character. Reset the stack and legit counter
                stack = []
                legit_len_so_far = 0

        return max_legit
                

    def longestValidParentheses_old(self, s):

        valid_parts = []

        # First fill of valid parts" "()" is a basic valid element
        for i in range(len(s) - 1):
            if s[i:i+2] == "()":
                valid_parts.append((i, i+1))

        # Then we keep "merging" and "growing" those valid parts

        # Keep doing it until something happens
        keep_going = True
        while keep_going:
            keep_going = False

            new_valid_parts = []

            while valid_parts:

                start, end = valid_parts.pop()

                # Merging two neighboring valid parts
                if valid_parts and valid_parts[-1][1] + 1 == start:
                    start, _ = valid_parts.pop()
                    keep_going = True

                # Should work in both directions
                # (as list will switch directions every time)
                if valid_parts and valid_parts[-1][0] - 1 == end:
                    _, end = valid_parts.pop()
                    keep_going = True

                # Expanding valid parts
                if start > 0 and end < len(s) - 1 and s[start-1] == "(" and s[end+1] == ")":
                    start, end = start - 1, end + 1
                    keep_going = True
                
                new_valid_parts.append((start, end))

            valid_parts = new_valid_parts

        # Calculate which is the max one in the resulting valid segments
        max_valid = 0
        for start, end in valid_parts:
            max_valid = max(max_valid, end - start + 1)

        return max_valid


def main():
    ''' Test longestValidParentheses
    '''
    solution = Solution()

    test_cases = [
        "(()", # 2
        ")()())", # 4
        "(()()",
        "", # 0
        "(())()()()())(()()()())()(((()))(()()((()()))))",
        "(())()(",
        ")()(((()))(()()((()()))))",
        "(()())",
        "()(()",
        "))((()((()", # 6
    ]
    for string in test_cases:
        result = solution.longestValidParentheses_old(string)
        result2 = solution.longestValidParentheses(string)
        print(string, result, result2)

def time_test(powers):
    solution = Solution()

    for power in range(1, powers + 1):

        length = 2** power
        string = "".join(["(" if random.random() < 0.5 else ")" for _ in range(length)])

        start = time.time()
        result = solution.longestValidParentheses(string)
        elapsed = time.time() - start

        print(f"{length}: {elapsed}")

def random_tests(runs):
    solution = Solution()
    for _ in range(runs):
        string = "".join(["(" if random.random() < 0.5 else ")" for _ in range(random.randint(1, 10))])
        result = solution.longestValidParentheses(string)
        result2 = solution.longestValidParentheses_old(string)
        if result != result2:
            print(f"Error in {string}: {result}, {result2}")
            break
    else:
        print(f"{runs} test okay")

if __name__ == "__main__":
    import random
    import time
    main()
    time_test(20)
    random_tests(100)
