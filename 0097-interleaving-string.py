''' https://leetcode.com/problems/interleaving-string/
'''

class Solution:
    def isInterleave(self, s1, s2, s3):
        return False


def main():
    ''' Test isInterleave
    '''
    solution = Solution()

    test_cases = [

        ("aabcc", "dbbca", "aadbbcbcac"), #True
        ("aabcc", "dbbca", "aadbbbaccc"), #False
        ("", "", ""), #True
    ]

    for s1, s2, s3 in test_cases:
        result = solution.isInterleave(s1, s2, s3)
        print(f"{s1}, {s2}, {s3}: {result}")


if __name__ == "__main__":
    import time
    main()
