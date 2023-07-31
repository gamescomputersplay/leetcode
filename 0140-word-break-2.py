''' https://leetcode.com/problems/word-break-ii/
'''

class Solution:
    def wordBreak(self, s, wordDict):

        # List of possible words that end here
        end_here = [[""]] + [[] for _ in range(len(s))]

        separator = ""

        # Go through all the positions in s
        for position in range(len(s)):

            # No words ended here - then we can't start here
            if not end_here[position] and position != 0:
                continue

            # Go through all words
            for word in wordDict:

                # If they match the piece of s from start, then
                # new word can start from start + len(word)

                if s[position:].startswith(word):
                    all_words_so_far = end_here[position]

                    # Take all teh combinations we had so far
                    for words_so_far in all_words_so_far:

                        # Add possible new matching words to those we had so far
                        end_here[position + len(word)].append(words_so_far + separator + word)

            separator = " "

        # All the combination emerged at "string + 1", is the answer
        return end_here[-1]

def main():
    ''' Test wordBreak
    '''
    solution = Solution()

    test_cases = [
        ("leetcode", ["leet","code"]),
        ("applepenapple", ["apple","pen"]),
        ("catsandog", ["cats","dog","sand","and","cat"]),
        ("catsanddog", ["cat","cats","and","sand","dog"]),
        ("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]),
    ]
    for s, wordDict in test_cases:
        result = solution.wordBreak(s, wordDict)
        print(s, wordDict, result)


if __name__ == "__main__":
    main()
