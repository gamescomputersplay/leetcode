''' https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums):

        total = sum(nums)

        # Minimum sum on the right side of the array
        # [n] means n-th is the first element NOT in the sum 
        min_sum_right = [0]
        running_sum = 0
        # We skip the last element, because at least
        # one element has to be left in the subarray
        for num in nums[:0:-1]:
            running_sum += num
            min_sum_right.append(min(min_sum_right[-1], running_sum))

        # Several things are done here
        # - keep the track of the sum of the i left elements
        # - keep track of teh minimum of such sum
        # - keep track of 
        # (best total - minimal sum from the left - minimal sum from the right)
        best_sum = float("-inf")
        running_sum = 0
        min_sum_left = 0
        for i, num in enumerate(nums):

            min_sum_left = min(min_sum_left, running_sum)
            best_sum = max(best_sum, total - min_sum_left - min_sum_right[-i-1])

            # Sum update is in the end of the cycle, as as it is
            # the sum of elements to the left of current item
            running_sum += num

        return best_sum
    
    def maxSubArray_brute(self, nums):
        max_sum = sum(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                max_sum = max(max_sum, sum(nums[i:j]))
        return max_sum

def random_test(runs=10):
    solution = Solution()
    for _ in range(runs):
        nums = [random.randint(-10, 10) for _ in range(1, 5)]
        result = solution.maxSubArray(nums)
        result2 = solution.maxSubArray_brute(nums)
        if result2 != result:
            print(f"Error in {nums}")
            break
    else:
        print(f"{runs} tests okay")

def main():
    ''' Test maxSubArray
    '''
    solution = Solution()

    test_cases = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [5,4,-1,7,8],
        [-3, -2, -1, 10, -1, -2, -3],
        [0, -8, -10, -6, 2, -5, -3, -5, 8],
        [-6, -2, -3, 0],
        [-3, -4, -7, -7]
    ]
    for nums in test_cases:
        result = solution.maxSubArray(nums)
        result2 = solution.maxSubArray_brute(nums)
        print(nums, result2, result, result2 == result)

if __name__ == "__main__":
    import random
    main()
    random_test(10000)
