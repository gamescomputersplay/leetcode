''' https://leetcode.com/problems/reverse-words-in-a-string/
'''

class Solution:
    def reverseWords(self, s):
        words = s.split(" ")
        return " ".join([word for word in words if word][::-1])

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
