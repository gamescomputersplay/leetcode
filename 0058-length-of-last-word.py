''' https://leetcode.com/problems/length-of-last-word/
'''


class Solution:
    def lengthOfLastWord(self, s):

        found_word = False
        word_length = 0
        for i in range(len(s)-1, -1, -1):

            if found_word:

                if s[i] == " ":
                    return word_length
                word_length += 1

            elif s[i] != " ":
                found_word = True
                word_length = 1

        return word_length

def main():
    ''' Test lengthOfLastWord
    '''
    solution = Solution()

    test_cases = [
        "Hello World",
        "   fly me   to   the moon  ",
        "oh",
        "",
    ]
    for string in test_cases:
        result = solution.lengthOfLastWord(string)
        print(string, result)

if __name__ == "__main__":
    main()
