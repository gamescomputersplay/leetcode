''' https://leetcode.com/problems/regular-expression-matching/
'''

class Solution:

    def isMatch(self, s, p):
        ''' Return whether string s is matching the regexp pattern p
        '''

        # Break down pattern into elements ("a*", ".*", ".", "a")
        p_elements = []
        pointer = 0
        while pointer < len(p):

            # 2 characters
            if pointer < len(p) - 1 and p[pointer+1] == "*":
                p_elements.append(p[pointer:pointer+2])
                pointer += 2
            else:
                p_elements.append(p[pointer])
                pointer += 1

        # Keep track of legit position for each p_element
        possible_starts = [0]

        # Go through elements of the pattern
        for p_element in p_elements:

            new_possible_starts = []

            # "." is exactly one element, does not matter which
            if p_element == ".":
                new_possible_starts = [possible_start + 1 for possible_start in possible_starts]
            
            # All letters in "s" will fit this pattern
            elif p_element == ".*":
                new_possible_starts = [position for position in range(min(possible_starts), len(s) + 1)]

            # Here we deal with "a*" pattern
            elif len(p_element) == 2 and p_element[1] == "*":

                # This is the letter we'll be looking for
                repeated_element = p_element[0]

                # Go through all legal matching beginnings
                for possible_start in possible_starts:

                    # This one in case there are 0 such letters
                    new_possible_starts.append(possible_start)

                    # And then go from that spot for as long
                    # as there are this letter present
                    shift = 0
                    while possible_start + shift < len(s) and \
                          s[possible_start + shift] == repeated_element:
                        new_possible_starts.append(possible_start + shift + 1)
                        shift += 1


            # The p_element must be an individual letter
            else:
                # Check that we have that letter in possible starts
                for possible_start in possible_starts:
                    # If we do - the position after it is the possible start
                    # for the next patter element
                    if possible_start < len(s) and s[possible_start] == p_element:
                        new_possible_starts.append(possible_start + 1)

            
            possible_starts = list(set(new_possible_starts))
            if not possible_starts:
                return False

        # All pattern parts are over. If end of s is in possible starts
        # after that, matching successful
        if len(s) in possible_starts:
            return True
        return False    

def main():
    ''' test reverse
    '''
    test_cases = [
        ("aa", "a"), # False
        ("aa", "a*"), # True
        ("ab", ".*"), # True
        ("aabbccdeee", "aab*cc.e.*e"), # True
        ("aaaaaaaab", "a*b"), # True
        ("aaaaaaaab", "a*a*b"), # True
        ("ccaaaaaaaab", "c*a*a*b"), # True
        ("aaaaaaxxxb", "a*.*b*"), # True
        ("aaabbbxxxb", "a*.*.*b*"), # True
        ("aaaaaaxxxb", "a*.*.*b*"), # True
        ("aaaaccaaaaaddaaaaa", "a*cc.*adda*"), # True
        ("aaacbbb", "a*.b*"),
    ]

    solution = Solution()
    for string, pattern in test_cases:
        print()
        print(string, pattern)
        print(solution.isMatch(string, pattern))


if __name__ == "__main__":
    main()
