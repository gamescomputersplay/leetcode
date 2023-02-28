''' https://leetcode.com/problems/regular-expression-matching/
'''

class Solution:

    def isMatch(self, s, p):
        ''' Return whether string s is matching the regexp pattern p
        '''

        def find_occurrences_indexes(haystack, needle):
            ''' Find all indexes at which "needle" occur in "haystack"
            '''
            search_from = 0
            found_occurrences = []
            while True:
                found_one = haystack.find(needle, search_from)
                if found_one == -1:
                    return found_occurrences
                found_occurrences.append(found_one)
                search_from = found_one + 1


        def find_first_non_mask(pattern):
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
        
        # Find the first occurrence of a "non-mask" in the pattern,
        # a fragment that has no "."" or "[character]*" in it
        first_non_mask = find_first_non_mask(p)
        print("Non-mask in", p, "is", first_non_mask)

        if first_non_mask:
            # If the string does not have it - failed match
            if first_non_mask not in s:
                return False
            
            # Otherwise find all occurrence of non-mask
            # in the searched string and pattern, permutate them
            for p_non_mask in find_occurrences_indexes(p, first_non_mask):
                for s_non_mask in find_occurrences_indexes(s, first_non_mask):

                    # Break both s and p by the non-mask
                    left_s, left_p = s[:s_non_mask], p[:p_non_mask]
                    right_s, right_p = s[s_non_mask + len(first_non_mask):], \
                        p[p_non_mask + len(first_non_mask):]

                    # And recursively try matches in both halves
                    # Match successful if moth halves match
                    print("Recursion for", left_s, left_p, "and", right_s, right_p)
                    if self.isMatch(left_s, left_p) and self.isMatch(right_s, right_p):
                        return True
            
            # After trying all possible halves, no luck: match fail
            return False

        # Placeholder so recursion would work correctly
        return True

        

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
        ("aaaaaaaab", "cca*a*b"), # True
        ("aaaaaaxxxb", "a*.*b*"), # True
        ("aaabbbxxxb", "a*.*.*b*"), # True
        ("aaaaaaxxxb", "a*.*.*b*"), # True
        ("aaaaccaaaaaddaaaaa", "a*cc.*adda*"), # True
    ]

    solution = Solution()
    for string, pattern in test_cases:
        print()
        print(string, pattern)
        print(solution.isMatch(string, pattern))


if __name__ == "__main__":
    main()
