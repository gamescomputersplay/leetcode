''' https://leetcode.com/problems/3sum/
'''

class Solution:
    def threeSum(self, nums):
        return []

def main():
    ''' Test threeSum
    '''
    solution = Solution()

    test_cases = [
        [-1, 0, 1, 2, -1, -4], # [[-1,-1,2],[-1,0,1]]
        [0, 1, 1], # []
        [0,0,0], # [[0,0,0]]
    ]
    for nums in test_cases:
        result = solution.threeSum(nums)
        print(nums, result)

if __name__ == "__main__":
    main()
