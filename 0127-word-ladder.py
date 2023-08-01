''' https://leetcode.com/problems/word-ladder/
'''

class Solution:    
    def ladderLength(self, beginWord, endWord, wordList):

        def one_letter_away(word1, word2):
            ''' Check if those 2 words are 1 letter apart
            '''
            mismatches = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    mismatches += 1
                    if mismatches == 2:
                        return False
            return True

        # Set for faster lookup
        wordlist_set = set(wordList)
        # In this case ladder is impossible
        if endWord not in wordlist_set:
            return 0

        # Words we just reach (use to look for the next step)
        just_reached = set([beginWord])
        # Seen words (can ignore)
        seen = set([beginWord])

        # count steps
        steps = 1

        # With every step expand out reach into the words
        while True:

            steps += 1

            # Track new reach
            new_reached = set()

            # Look at every word we have
            for word in just_reached:

                # And see if we can move to the next one
                for potential_reach in wordList:

                    # No need to check if we alreacy reached this word
                    if potential_reach in seen:
                        continue

                    if one_letter_away(word, potential_reach):
                        new_reached.add(potential_reach)

            if endWord in new_reached:
                return steps
            if len(new_reached) == 0:
                return 0

            just_reached = new_reached
            seen.update(just_reached)


def main():
    ''' Test ladderLength
    '''
    solution = Solution()

    test_cases = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"]), #5
        ("hit", "cog", ["hot","dot","dog","lot","log"]), #0
    ]
    for beginWord, endWord, wordList in test_cases:
        result = solution.ladderLength(beginWord, endWord, wordList)
        print(beginWord, endWord, wordList, result)


if __name__ == "__main__":
    main()
