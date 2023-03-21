''' https://leetcode.com/problems/substring-with-concatenation-of-all-words/
'''

class Solution:
    def findSubstring(self, s, words):
        return []
    
def main():
    ''' Test findSubstring
    '''
    solution = Solution()

    test_cases = [
        ("barfoothefoobarman", ["foo","bar"]), # [0, 9]
        ("wordgoodgoodgoodbestword", ["word","good","best","word"]), # []
        ("barfoofoobarthefoobarman", ["bar","foo","the"]), # [6, 9, 12]
    ]
    for string, words in test_cases:
        result = solution.findSubstring(string, words)
        print(string, words, result)

if __name__ == "__main__":
    main()
