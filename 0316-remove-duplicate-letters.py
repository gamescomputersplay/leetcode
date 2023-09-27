''' https://leetcode.com/problems/remove-duplicate-letters/
'''

class Solution:
    def removeDuplicateLetters(self, s):

        # Right-to-left stack
        stack = []

        for ch in s[::-1]:

            if ch not in stack:
                stack.append(ch)
                continue

            if ch >= stack[-1]:
                continue

            stack[stack.index(ch)] = ""
            stack.append(ch)

        return "".join(stack[::-1])

def main():
    ''' Test removeDuplicateLetters
    '''
    solution = Solution()

    test_cases = [
        # "bcabc",
        # "cbacdcbc",
        # "dddeffsbbbbaaebabbsf",
        "abacb",
        # "bcbac", # bac
    ]

    for s in test_cases:
        result = solution.removeDuplicateLetters(s)
        print(s, result)


if __name__ == "__main__":
    main()
        