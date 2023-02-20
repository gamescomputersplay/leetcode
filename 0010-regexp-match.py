''' https://leetcode.com/problems/regular-expression-matching/
'''

class Solution:

    def isMatch(self, s, p):
        ''' Return whether string s is matching the regexp pattern p
        '''

        def find_non_mask(pattern):
            ''' Find the first occurrence of a non-mask (that is without "."
            or "*") in the pattern
            '''

            # Find the first non-mask element in the pattern
            start_non_mask = 0
            while True:

                # We reached the end of the string. There are no non-mask characters
                if start_non_mask == len(pattern):
                    start_non_mask = None
                    break

                # It's a "a*" or ".*"
                elif start_non_mask + 1 <= len(pattern) - 1 and pattern[start_non_mask + 1] == "*":
                    start_non_mask += 2

                # it's a single "."
                elif pattern[start_non_mask] == ".":
                    start_non_mask += 1

                # Found the non-mask one 
                else:
                    break

            # Can;t find where non-mask starts - there is no non-mask
            if start_non_mask is None:
                return None

            # Find where the non-mask portion ends
            end_non_mask = start_non_mask
            while True:

                # We reached the end of the string. Break, keeping end_non_mask what it is
                if end_non_mask == len(pattern):
                    break

                # It the next thing is a "a*" or ".*"
                elif end_non_mask + 1 <= len(pattern) - 1 and pattern[end_non_mask + 1] == "*":
                    break

                # it's a single "."
                elif pattern[end_non_mask] == ".":
                    break

                # Non of the above: keep going right
                else:
                    end_non_mask += 1

            return pattern[start_non_mask:end_non_mask]
            
        print("Non-mask", find_non_mask(p))

def main():
    ''' test reverse
    '''
    test_cases = [
        ("aa", "a"), # False
        ("aa", "a*"), # True
        ("ab", ".*"), # True
        ("aabbccdee", "aab*cc.ee"), # True
        ("aaaaaaaab", "a*b"), # True
        ("aaaaaaaab", "a*a*b"), # True
        ("aaaaaaaab", "a*a*b"), # True
        ("aaaaaaxxxb", "a*.*b*"), # True
        ("aaabbbxxxb", "a*.*.*b*"), # True
        ("aaaaaaxxxb", "a*.*.*b*"), # True
        ("aaaaaaaaab", "a*.*.*b*"), # True
    ]

    solution = Solution()
    for string, pattern in test_cases:
        print()
        print(string, pattern)
        print(solution.isMatch(string, pattern))


if __name__ == "__main__":
    main()
