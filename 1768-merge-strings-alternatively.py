''' https://leetcode.com/problems/merge-strings-alternately/
'''

class Solution:
    def mergeAlternately(self, word1, word2):

        combined = []

        for pos in range(max(len(word1), len(word2))):
            if pos < len(word1):
                combined.append(word1[pos])
            if pos < len(word2):
                combined.append(word2[pos])

        return "".join(combined)

def main():
    ''' Test mergeAlternately
    '''
    solution = Solution()

    test_cases = [
        ("ab", "pqrs"),
        ("abcd", "pq"),
        ("a", "b"),
        ("a", "bcdefghijk"),
        ("abcdefghijk", "z"),

    ]
    for word1, word2 in test_cases:
        result = solution.mergeAlternately(word1, word2)
        print(word1, word2, result)

if __name__ == "__main__":
    main()