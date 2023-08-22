''' https://leetcode.com/problems/repeated-substring-pattern/
'''

class Solution:
    def repeatedSubstringPattern(self, s):

        # String length
        slen = len(s)

        for size in range(1, slen//2 + 1):

            # Only check if there are whole number of substrings
            if slen % size != 0:
                continue

            # Check if the first chunk matches remaining chunks
            first = s[0:size]
            for i in range(1, slen // size):
                if s[i * size:(i+1) * size] != first:
                    break
            else:
                return True

        return False

def main():
    ''' Test repeatedSubstringPattern
    '''
    solution = Solution()

    test_cases = [
       "abab",
       "aba",
       "abcabcabcabc",
       "abcdabcdabcdabcde",
       "a",
       "aa",
    ]
    for string in test_cases:
        result = solution.repeatedSubstringPattern(string)
        print(string, result)

if __name__ == "__main__":
    main()
