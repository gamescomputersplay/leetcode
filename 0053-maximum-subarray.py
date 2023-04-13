''' https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums):

        total = sum(nums)
        #print(total)

        # Minimum sum on the left side of the array
        # [n] means n-th is the first element NOT in the sum 
        min_sum_left = [0]
        running_sum = 0
        # We skip the last element, because at least
        # one element has to be left in the subarray
        for num in nums[:-1]:
            running_sum += num
            min_sum_left.append(min(min_sum_left[-1], running_sum))

        #print(min_sum_left)

        # Same from the right
        min_sum_right = [0]
        running_sum = 0
        for num in nums[:0:-1]:
            running_sum += num
            min_sum_right.append(min(min_sum_right[-1], running_sum))

        #print(min_sum_right[::-1])

        # Check which combination can produce the best sum
        best_sum = float("-inf")
        for i in range(len(min_sum_left)):
            best_sum = max(best_sum, total - min_sum_left[i] - min_sum_right[-i-1])

        return best_sum
    
    def maxSubArray_brute(self, nums):
        max_sum = sum(nums)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums) + 1):
                max_sum = max(max_sum, sum(nums[i:j]))
        return max_sum

def main():
    ''' Test maxSubArray
    '''
    solution = Solution()

    test_cases = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [5,4,-1,7,8],
        [-3, -2, -1, 10, -1, -2, -3],
    ]
    for nums in test_cases:
        result = solution.maxSubArray(nums)
        result2 = solution.maxSubArray_brute(nums)
        print(nums, result2, result, result2 == result)

if __name__ == "__main__":
    main()
