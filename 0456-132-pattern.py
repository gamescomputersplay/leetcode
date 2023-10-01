''' https://leetcode.com/problems/132-pattern/
'''

class Solution:
    def find132pattern(self, nums):


        return False

def main():
    ''' Test find132pattern
    '''
    solution = Solution()

    test_cases = [
        [1,2,3,4],
        [3,1,4,2],
        [-1,3,2,0],
        [1],
        [1,2],
        [1,2,3],
        [1, 3, 2],
        [3,5,0,3,4],
        [1,0,1,-4,-3],
        [1,4,0,-1,-2,-3,-1,-2]
    ]
    for nums in test_cases:
        result = solution.find132pattern(nums)
        print(nums, result)

if __name__ == "__main__":
    main()