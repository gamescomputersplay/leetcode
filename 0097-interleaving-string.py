''' https://leetcode.com/problems/interleaving-string/
'''

class Solution:
    def __init__(self):
        self.cache = {}

    def isInterleave(self, s1, s2, s3):

        if len(s1) + len(s2) != len(s3):
            return False

        if (s1, s2, s3) in self.cache:
            return self.cache[(s1, s2, s3)]

        # One side is empty
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3

        # Clearly letter belongs to one side
        if s1[0] == s3[0] and s2[0] != s3[0]:
            self.cache[(s1, s2, s3)] = self.isInterleave(s1[1:], s2, s3[1:])
            return self.cache[(s1, s2, s3)]
        if s1[0] != s3[0] and s2[0] == s3[0]:
            self.cache[(s1, s2, s3)] = self.isInterleave(s1, s2[1:], s3[1:])
            return self.cache[(s1, s2, s3)]

        # Letter can belong to either side
        if s1[0] == s3[0] and s2[0] == s3[0]:
            self.cache[(s1, s2, s3)] = self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
            return self.cache[(s1, s2, s3)]

        # Letter can belong to neither side
        if s1[0] != s3[0] and s2[0] != s3[0]:
            self.cache[(s1, s2, s3)] = False
            return False


def main():
    ''' Test isInterleave
    '''
    solution = Solution()

    test_cases = [

        ("abc", "def", "abcdef"),
        ("abc", "def", "aefbcd"),
        ("abc", "def", "adebcf"),
        ("abc", "def", "adbcef"),
        ("abc", "def", "adbecf"),
        ("abc", "def", "defabc"),
        ("aabcc", "dbbca", "aadbbcbcac"), #True
        ("aabcc", "dbbca", "aadbbbaccc"), #False
        ("", "", ""), #True
    ]

    for s1, s2, s3 in test_cases:
        result = solution.isInterleave(s1, s2, s3)
        print(f"{s1}, {s2}, {s3}: {result}")

def random_test(length=200):

    s3 = ""
    while len(s3) < length:
        s3 += random.choice("abcdefghjikl") * random.randint(50, 100)

    s1, s2 = "", ""
    for c in s3:
        if random.randint(0, 1):
            s1 += c
        else:
            s2 += c


    solution = Solution()
    start = time.time()
    result = solution.isInterleave(s1, s2, s3)
    elapsed = time.time() - start
    print(f"{len(s3)}, {result}, {elapsed}")
    
    solution = Solution()

def long_case():
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    solution = Solution()
    start = time.time()
    result = solution.isInterleave(s1, s2, s3)
    elapsed = time.time() - start
    print(f"{len(s3)}, {result}, {elapsed}")

if __name__ == "__main__":
    import  random
    import time
    main()
    random_test()
    long_case()
