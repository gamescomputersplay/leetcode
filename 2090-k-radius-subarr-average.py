''' https://leetcode.com/problems/k-radius-subarray-averages/
'''

class Solution:
    def getAverages(self, nums, k):

        # 0 radius - numbers themselves
        if k == 0:
            return nums

        # k radius bigger than array
        if len(nums) < 1 + 2 * k:
            return [-1] * len(nums)

        result = []
        running_sum = sum(nums[:k])

        for pos in range(len(nums)):

            if pos + k < len(nums):
                running_sum += nums[pos + k]
            if pos - k - 1 >= 0:
                running_sum -= nums[pos - k - 1]

            if pos + k >= len(nums) or pos - k < 0:
                result.append(-1)
            else:
                result.append(running_sum // (2 * k + 1))
            print(pos, running_sum, result[-1])

        return result


def main():
    ''' Test getAverages
    '''
    solution = Solution()

    test_cases = [
        ([7,4,3,9,1,8,5,2,6], 3),
        ([100000], 0),
        ([8], 100000),
        ([1, 2, 3, 4], 1,)
    ]
    for nums, k in test_cases:
        result = solution.getAverages(nums, k)
        print(nums, k, result)

if __name__ == "__main__":
    main()
