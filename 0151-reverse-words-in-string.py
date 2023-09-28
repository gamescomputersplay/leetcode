''' https://leetcode.com/problems/reverse-words-in-a-string/
'''

class Solution:
    def reverseWords(self, s):
        words = []
        curr_word_start = None

        # Break the string into words by spaces
        for pos, ch in enumerate(s + " "):
            if ch != " " and curr_word_start is None:
                curr_word_start = pos
            if ch == " " and curr_word_start is not None:
                words.append(s[curr_word_start: pos])
                curr_word_start = None

        return " ".join(words[::-1])

def main():
    ''' Test reverseWords
    '''
    solution = Solution()

    test_cases = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
        "a",
        "   a   "
    ]
    for s in test_cases:
        result = solution.reverseWords(s)
        print(f"'{s}': {result}")


if __name__ == "__main__":
    main()
