''' https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


class Solution():

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Start of a current non-repeat window
        window_start = 0
        # Max encountered length of non-repeat  window
        max_length = 0
        # Set of letters in a current non-repeat window
        letters_in_window = set()

        for position, letter in enumerate(s):

            # If a letter is not in a non-repeat window:
            if letter not in letters_in_window:

                # Add it to the set
                letters_in_window.add(letter)

                # Check if it is the biggest window we had seen
                max_length = max(max_length, position - window_start + 1)

            # There is a repetition
            else:

                # Go through the window
                for i in range(window_start, position):

                    # Until we find the first instance of the repeated letter
                    if s[i] == letter:
                        # And reset the left size of the non-repeat window
                        # Right after the repeating letter
                        window_start = i + 1
                        break

                    # And remove all letters up until the repeating one
                    # from the set of letters in teh window
                    letters_in_window.remove(s[i])

        return max_length

def main():
    ''' Test lengthOfLongestSubstring
    '''
    solution = Solution()

    test_cases = [
        "abcabcbb", # 3
        "bbbbb", # 1
        "pwwkew", # 3
        "", # 0
        "abcdasfwaaab" * 100000
    ]
    for string  in test_cases:
        print(solution.lengthOfLongestSubstring(string))

if __name__ == "__main__":
    main()
