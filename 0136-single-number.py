''' https://leetcode.com/problems/single-number/
'''

class Solution:
    def singleNumber(self, nums):

        a = 0
        for num in nums:
            a ^= num
        return a

def main():
    ''' Test singleNumber
    '''
    solution = Solution()

    test_cases = [
        [2,3,2],
        [0,1,0,1,99],
        [-2, -2, -7]
    ]
    for nums in test_cases:
        result = solution.singleNumber(nums)
        print(nums, result)


if __name__ == "__main__":
    main()
