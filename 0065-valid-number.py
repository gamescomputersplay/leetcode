''' https://leetcode.com/problems/valid-number/
'''

class Solution:
    def isNumber(self, s):

        pointer = 0
        at_least_one_N = False
        valid_E = True
        length = len(s)
        numbers = "1234567890"

        for element in "-N.Ne-M":
            # N for a number that can be empty
            # M for a number that cannot be empty

            if pointer == length:
                break

            if element == "N":
                while pointer < length and s[pointer] in numbers:
                    pointer += 1
                    at_least_one_N = True
            
            elif element == "-":
                if s[pointer] in ("-", "+"):
                    pointer += 1

            elif element == "e":
                if s[pointer] in ("e", "E"):
                    pointer += 1
                    valid_E = False
                else:
                    break
            
            elif element == ".":
                if s[pointer] == ".":
                    pointer += 1

            elif element == "M":
                if pointer < length and s[pointer] not in numbers:
                    return False
                while pointer < length and s[pointer] in numbers:
                    pointer += 1
                    valid_E = True

        if not at_least_one_N or pointer != len(s) or not valid_E:
            return False

        return True

    def isNumber_old(self, s):

        def is_float(s):

            if "." in s and len(s) > 1:
                integral, fractional = s.split(".")
                if integral in ("", "-", "+") and fractional in ("", "-", "+"):
                    return False
                return is_int(integral, allow_empty=True, allow_only_sign=True) and \
                       is_int(fractional, allow_sign=False, allow_empty=True)
            return is_int(s)

        def is_int(s, allow_sign=True, allow_empty=False, allow_only_sign=False):
            ''' Valid int '''
            if allow_empty and s == "":
                return True
            if allow_only_sign and s in ("-", "+"):
                return True
            for pos, char in enumerate(s):
                if allow_sign and pos == 0 and char in ("-", "+"):
                    continue
                if char not in "0123456789":
                    return False
            # three last exceptions that are not valid ints
            return s not in ("", "+", "-")

        # To ignore "E" and "e" distinction
        s = s.upper()

        if s.count(".") > 1 or s.count("E") > 1:
            return False

        if "E" in s:

            coefficient, exponent = s.split("E")
            return is_float(coefficient) and is_int(exponent)

        return is_float(s)

def main(verbose=True):
    ''' Test isNumber
    '''
    solution = Solution()

    test_cases = [ 
        "-1.5e-3",
       "", "0", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", # Valid
       "e", ".", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "11.2.3", "11e22ee33e3", ".+", "+." # Non valid
    ]

    for s in test_cases:
        result = solution.isNumber(s)
        if verbose:
            print(s, result)

def test_timing(runs=10000):
    start = time.time()
    for _ in range(runs):
        main(verbose=False)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    test_timing()
