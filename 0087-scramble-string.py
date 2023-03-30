''' https://leetcode.com/problems/scramble-string/
'''

class Solution:
    def isScramble(self, s1, s2):

        # 1-letter strings
        if len(s1) == 1:
            return s1[0] == s2[0]

        # 2 letter string. As long as they are the same letters, they are good
        if len(s1) == 2:
            return sorted(s1) == sorted(s2)

        # Otherwise, split strings at all possible locations
        for cut in range(1, len(s1)):

            # Cut left string
            left1, right1 = s1[:cut], s1[cut:]

            # Cut right string in direct and reversed way
            left2_d, right2_d = s2[:cut], s2[cut:]
            left2_r, right2_r = s2[-cut:], s2[:-cut]

            # Run checks for both direct and reverse cuts
            for left2, right2 in ((left2_d, right2_d), (left2_r, right2_r)):
                # If at any of the locations scramble is possible, it's True
                if sorted(left1) == sorted(left2) and sorted(right1) == sorted(right2):
                    if self.isScramble(left1, left2) and self.isScramble(right1, right2):
                        return True

        # If in all locations it's impossible, it's False
        return False


def main():
    ''' Test isScramble
    '''
    solution = Solution()

    test_cases = [
        ("great", "rgeat"), #True
        ("abcde", "caebd"), #False
        ("a", "a"), # True
        ("ab", "ba"), 
        ("ab", "ba"), 
        ("aa", "aa"), 
        ("aaaaaaaaBa", "aBaaaaaaaa"), 
        ("abcdefghikjlmnopqrstuvwxyzabcd", "nopqrstuvwxyzabcdhikjlmcdefgab"),
        ("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd")
    ]
    for s1, s2 in test_cases:
        print(s1, s2, solution.isScramble(s1, s2))

if __name__ == "__main__":
    main()
