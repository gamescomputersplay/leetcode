''' https://leetcode.com/problems/number-of-longest-increasing-subsequence/
'''

class Solution:
    def findNumberOfLIS(self, nums):
        return 0

def main():
    ''' Test findNumberOfLIS
    '''
    solution = Solution()

    test_cases = [
        [1,3,5,4,7], #2
        [2,2,2,2,2], #2
    ]
    for nums in test_cases:
        result = solution.findNumberOfLIS(nums)
        print(f"{nums}, {result}")

if __name__ == "__main__":
    main()