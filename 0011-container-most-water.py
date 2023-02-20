''' https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, height):
        ''' Return the max volume of water
        '''


def main():
    ''' test maxArea
    '''
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7], #49
        [1, 1], #1
    ]

    solution = Solution()
    for array in test_cases:
        print(array, solution.maxArea(array))


if __name__ == "__main__":
    main()
