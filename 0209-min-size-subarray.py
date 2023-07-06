''' https://leetcode.com/problems/minimum-size-subarray-sum/
'''

class Solution:
    def minSubArrayLen(self, target, nums):
        start, end = 0, 1
        curr_sum = nums[0]
        min_len = float("inf")

        while True:

            # Sum in the window smaller than target
            # Keep increasing the window 
            if curr_sum < target:
                if end < len(nums):
                    curr_sum += nums[end]
                    end += 1
                # Unless array is over than stop
                else:
                    break

            # Sum in the window reaches the target
            else:
                # Track the min length
                min_len = min(min_len, end - start)
                # Can we make a window smaller?
                if start < end - 1:
                    curr_sum -= nums[start]
                    start += 1
                # If not, the answer is 1
                else:
                    return 1

        if min_len == float("inf"):
            return 0
        return min_len

def main():
    ''' Test minSubArrayLen
    '''
    solution = Solution()

    test_cases = [
        (7, [2,3,1,2,4,3]),
        (4, [1,4,4]),
        (11, [1,1,1,1,1,1,1,1]),
        (100, [1]),
        (0, [1]),
        (1, [1]),
        (10, [1, 2, 3, 4, 5, 6, 7, 8, 7, 10, 1, 1])

    ]
    for target, nums in test_cases:
        result = solution.minSubArrayLen(target, nums)
        print(target, nums, result)

if __name__ == "__main__":
    main()
