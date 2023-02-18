''' https://leetcode.com/problems/string-to-integer-atoi/
'''

class Solution:
    def myAtoi(self, s):

        # List of digits
        numbers = "0123456789"
        numbers_value = {numbers[i]: i for i in range(10)}

        # The number we'll return
        the_number = 0

        # What position of the string we are at
        pointer = 0

        # Sign (1 or -1)
        sign = 1

        # Ignoring leading spaces
        while pointer < len(s) and s[pointer] == " ":
            pointer += 1

        # Read the sign
        if pointer < len(s) and s[pointer] == "-":
            sign = -1
        if pointer < len(s) and s[pointer] in ("-", "+"):
            pointer += 1

        # Read the number while there are digits
        while pointer < len(s) and s[pointer] in numbers:

            the_number *= 10
            the_number += numbers_value[s[pointer]]
            pointer += 1

        the_number *= sign

        # Kinda weird to do this check in Python, but okay
        if  the_number < - (2 ** 31):
            return - (2 ** 31)
        if the_number > 2**31 - 1:
            return 2**31 - 1

        return  the_number

def main():
    ''' Test myAtoi
    '''
    solution = Solution()

    test_cases = [
        "42",
        "   -42",
        "4193 with words",
        "0032",
        "abc",
        ""
    ]
    for string in test_cases:
        print(string, solution.myAtoi(string))

if __name__ == "__main__":
    main()
