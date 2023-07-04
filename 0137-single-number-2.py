''' https://leetcode.com/problems/single-number-ii/
'''

class Solution:
    def singleNumber(self, nums):

        a, b = 0, 0
        for num in nums:
            a, b = (~b) & (a ^ num), (b ^ a) & (b ^ num)
        return a

def main():
    ''' Test singleNumber
    '''
    solution = Solution()

    test_cases = [
        [2,2,3,2],
        [0,1,0,1,0,1,99],
        [-2, -2, -2, -7]
    ]
    for nums in test_cases:
        result = solution.singleNumber(nums)
        print(nums, result)


if __name__ == "__main__":
    main()
