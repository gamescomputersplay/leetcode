''' https://leetcode.com/problems/reverse-integer/
'''

class Solution:
    def reverse(self, x):
        pass

def main():
    ''' test reverse
    '''
    test_cases = [
        123,
        -123,
        120
    ]

    solution = Solution()
    for number in test_cases:
        print(number, solution.reverse(number))


if __name__ == "__main__":
    main()
