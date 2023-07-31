''' https://leetcode.com/problems/word-break/
'''

class Solution:
    def wordBreak(self, s, wordDict):

        # List that shows that a word can be started at this position
        can_start_here = [True] + [False for _ in range(len(s))]

        # Go through all the positions in s
        for start in range(len(s)):

            # No words ended here - then we can't start here
            if not can_start_here[start]:
                continue

            # Go through all words
            for word in wordDict:

                # If they match the piece of s from start, then
                # new word can start from start + len(word)
                if s[start:].startswith(word):
                    can_start_here[start + len(word)] = True

        # If new word can start right after s ends - s has been covered
        return can_start_here[-1]

def main():
    ''' Test wordBreak
    '''
    solution = Solution()

    test_cases = [
        ("leetcode", ["leet","code"]),
        ("applepenapple", ["apple","pen"]),
        ("catsandog", ["cats","dog","sand","and","cat"]),
    ]
    for s, wordDict in test_cases:
        result = solution.wordBreak(s, wordDict)
        print(s, wordDict, result)


if __name__ == "__main__":
    main()
