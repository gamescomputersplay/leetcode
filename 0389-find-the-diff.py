''' https://leetcode.com/problems/find-the-difference/
'''

class Solution:
    def findTheDifference(self, s, t) -> str:

        # count letters in the bigger one
        letters = {}
        for ch in t:
            letters[ch] = letters.get(ch, 0) + 1

        # subtract teh smaller one
        for ch in s:
            letters[ch] -= 1

        # Whichever letter still has 1 is the answer
        for k, v in letters.items():
            if v == 1:
                return k

        return ""

def main():
    ''' Test findTheDifference
    '''
    solution = Solution()

    test_cases = [
        ("abcd", "abcde"),
        ("", "y"),
    ]
    for s, t in test_cases:
        result = solution.findTheDifference(s, t)
        print(f"{s}, {t}: {result}")

if __name__ == "__main__":
    main()
