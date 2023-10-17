''' https://leetcode.com/problems/fraction-to-recurring-decimal/
'''

class Solution:
    def fractionToDecimal(self, numerator, denominator):

        if numerator == 0:
            return "0"
        
        # Calculate the sign, keep only abs value
        sign = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator
                          )
        # Digits will be placed in this list (use a list as
        # we'll need to count/insert/pop items before it's ready)
        result = [sign]

        # Dict with remainders (numenator), that we've already seen
        # Familiar numenator indicates a periodical fraction
        # {remaiinder: position seen at}
        seen = {}

        # Flag to handle the part before decimal point differently
        first = True

        while True:

            digit = numerator // denominator
            result.append(str(digit))

            # Before dicimal point: append ".",
            # don't track seen remainders
            if first:
                result.append(".")
                first = False
            # After decimal point: track remainders
            else:
                seen[numerator] = len(result)

            numerator -= digit * denominator
            numerator *= 10

            # Once familiar remainder is found, calculate "period"
            # Looking at how log ago such reainder was seen
            if numerator in seen:
                period = len(result) - seen[numerator] + 1
                break

        # Periodical fraction - add parentheses
        if result[-1] != "0":
            result.insert(-period, "(")
            result.append(")")

        # Finite fraction, remove trailing 0 and . if neededß
        while result[-1] in ("0", "."):
            result.pop()

        # String from the list
        return "".join(result)

def main():
    ''' Test fractionToDecimal
    '''
    solution = Solution()

    test_cases = [
        (1, 2),
        (2, 1),
        (4, 333),
        (100, 7),
        (0, 3),
        (-50, 8),
    ]
    for numerator, denominator in test_cases:
        result = solution.fractionToDecimal(numerator, denominator)
        print(numerator, denominator, result)

if __name__ == "__main__":
    main()
