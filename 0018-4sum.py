''' https://leetcode.com/problems/4sum/
'''

class Solution:
    def fourSum(self, nums, target):
        return []

    def fourSumBrute(self, nums, target):

        solutions = set()

        for a, num_1 in enumerate(nums):
            for b, num_2 in enumerate(nums[:a]):
                for c, num_3 in enumerate(nums[:b]):
                    for d, num_4 in enumerate(nums[:c]):

                        if num_1 + num_2 + num_3 + num_4 == target:
                            solution = [num_1, num_2, num_3, num_4]
                            solution.sort()
                            solutions.add(tuple(solution))

        return [list(solution) for solution in solutions]

def main():
    ''' Test threeSum
    '''
    solution = Solution()

    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0), # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        ([2, 2, 2, 2, 2], 8), # [[2,2,2,2]]
        ([1, 2, 3, 4, 5, 6, 7, 8], 13),
    ]
    for nums, target in test_cases:
        result1 = solution.fourSum(nums, target)
        result2 = solution.fourSumBrute(nums, target)
        print(nums, target, result1, result2)

if __name__ == "__main__":
    main()
