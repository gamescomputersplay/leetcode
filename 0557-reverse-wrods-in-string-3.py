''' https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''

class Solution:
    def reverseWords(self, s):
        words = [token[::-1] for token in s.split(" ")]
        return " ".join(words)

def main():
    ''' Test reverseWords
    '''
    solution = Solution()

    test_cases = [
        "Let's take LeetCode contest",
        "God Ding",
        "A",
    ]
    for s in test_cases:
        result = solution.reverseWords(s)
        print(f"{s}, {result}")

if __name__ == "__main__":
    main()
