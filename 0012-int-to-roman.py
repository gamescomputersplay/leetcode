''' https://leetcode.com/problems/integer-to-roman/
'''

class Solution:
    def intToRoman(self, num):
        pass


def main():
    ''' Test intToRoman
    '''
    solution = Solution()

    test_cases = [
        i for i in range(1, 50, 7)
    ]
    for num in test_cases:
        result = solution.intToRoman(num)
        print(num, result)



if __name__ == "__main__":
    main()
