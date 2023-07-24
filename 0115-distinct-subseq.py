''' https://leetcode.com/problems/distinct-subsequences/
'''

class Solution:
    def numDistinct(self, s, t):

        # How many matching substrings up to (and including) t[i]
        matches = [0 for _ in range(len(t))]

        for ch in s:

            for i in range(len(t)-1, -1, -1):

                if t[i] == ch:
                    if i > 0:
                        matches[i] += matches[i-1]
                    else:
                        matches[i] += 1

        return matches[-1]

def main():
    ''' Test numDistinct
    '''
    solution = Solution()

    test_cases = [
        ("rabbbit", "rabbit"), #3
        ("babgbag", "bag"), #5
        ("a", "a"),
        ("a", "aa"),
        ("aa", "a")
    ]
    for s, t in test_cases:
        result = solution.numDistinct(s, t)
        print(s, t, result)


if __name__ == "__main__":
    main()
