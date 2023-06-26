''' https://leetcode.com/problems/decode-ways/
'''

class Solution:
    def __init__(self):
        self.cache = {}

    def numDecodings(self, s):

        if s=="":
            return 1

        if s[0] == "0":
            return 0

        if len(s) == 1:
            return 1

        if s in self.cache:
            return self.cache[s]

        # 3-9
        first = int(s[0])
        if first > 2:
            self.cache[s] = self.numDecodings(s[1:])
            return self.cache[s]

        # 1, 2 + 10-26
        second = int(s[1])
        if first == 1 or second < 7:
            self.cache[s] = self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            return self.cache[s]

        # 27 => 2
        self.cache[s] = self.numDecodings(s[1:])
        return self.cache[s]


def main():
    ''' Test numDecodings
    '''
    solution = Solution()

    test_cases = [
        "12",
        "123",
        "226",
        "06",
        "12345",
        "87246761216123537264182761",
        "111111111111111111111111111111111111111111111"
    ]
    for s in test_cases:
        result = solution.numDecodings(s)
        print(f"{s}: {result}")

if __name__ == "__main__":
    main()
