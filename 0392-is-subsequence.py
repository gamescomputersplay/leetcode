''' https://leetcode.com/problems/is-subsequence/
'''

class Solution:
    def isSubsequence(self, s, t):
        if s == "":
            return True
        if t == "":
            return False

        ps, pt = 0, 0

        while pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                if ps == len(s):
                    return True
            pt += 1

        return False

def main():
    ''' Test isSubsequence
    '''
    solution = Solution()

    test_cases = [
        ("abc", "ahbgdc"),
        ("axc", "ahbgdc"),
    ]
    for s, t in test_cases:
        result = solution.isSubsequence(s, t)
        print(f"{s}, {t}: {result}")

if __name__ == "__main__":
    main()
