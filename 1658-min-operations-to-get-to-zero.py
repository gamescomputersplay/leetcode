''' https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
'''

class Solution:
    def minOperations(self, nums, x):

        # What should be teh sum of the central section
        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        # Central section is limited by two pointers
        p1, p2 = 0, 0
        # Sum in the central section
        central = 0

        # Minimal items to remove
        min_removal = float("inf")
        while True:

            if central == target:
                removals = len(nums) - (p2 - p1)
                min_removal = min(min_removal, removals)
                central -= nums[p1]
                p1 += 1

            elif central < target:
                if p2 == len(nums):
                    break
                central += nums[p2]
                p2 += 1

            elif central > target:
                central -= nums[p1]
                p1 += 1           

        if min_removal == float("inf"):
            min_removal = -1
        return min_removal

def main():
    ''' Test minOperations
    '''
    solution = Solution()

    test_cases = [
        ([1,1,4,2,3], 5), # 2
        ([5,6,7,8,9], 4), # -1
        ([3,2,20,1,1,3], 10), # 5
        ([1], 0),
        ([5,2,3,1,1], 5), #1
        ([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365), #16

    ]
    for nums, x in test_cases:
        result = solution.minOperations(nums, x)
        print(nums, x, result)

if __name__ == "__main__":
    main()