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

        print(p_elements)

        # Go through elements of the patterm
        
        return True
        

def main():
    ''' test reverse
    '''
    test_cases = [
        #("aa", "a"), # False
        #("aa", "a*"), # True
        #("ab", ".*"), # True
        ("aabbccdee", "aab*cc.e.*e"), # True
        #("aaaaaaaab", "a*b"), # True
        #("aaaaaaaab", "a*a*b"), # True
        #("aaaaaaaab", "cca*a*b"), # True
        #("aaaaaaxxxb", "a*.*b*"), # True
        #("aaabbbxxxb", "a*.*.*b*"), # True
        #("aaaaaaxxxb", "a*.*.*b*"), # True
        #("aaaaccaaaaaddaaaaa", "a*cc.*adda*"), # True
        #("aaacbbb", "a*.b*"),
    ]

    solution = Solution()
    for string, pattern in test_cases:
        print()
        print(string, pattern)
        print(solution.isMatch(string, pattern))


if __name__ == "__main__":
    main()
