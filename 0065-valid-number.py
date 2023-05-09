''' https://leetcode.com/problems/valid-number/
'''

class Solution:
    def isNumber(self, s):

        def is_float(s):
            return False
        
        def is_int(s):
            for pos, char in enumerate(s):
                if pos == 0 and char in ("-", "+"):
                    continue
                if char not in "0123456789":
                    return False
            return True

        # To ignore "E" and "e" distinction
        s = s.upper()

        if "E" in s:

            coefficient, exponent = s.split("E")
            return is_float(coefficient) and is_int(exponent)

        return is_float(s)

def main():
    ''' Test isNumber
    '''
    solution = Solution()

    test_cases = [ 
       "0", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", # Valid
       "e", ".", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", # Non valid
    ]

    for s in test_cases:
        result = solution.isNumber(s)
        print(s, result)

if __name__ == "__main__":
    main()
