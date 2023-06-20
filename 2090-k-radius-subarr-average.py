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

        size = 2 * k + 1

        result = [-1] * k + [None] * (len(nums) - 2 * k) + [-1] * k
        running_sum = sum(nums[:size])

        for pos in range(k, len(nums) - k):

            result[pos] = running_sum // size

            if pos + k + 1 < len(nums):
                running_sum += nums[pos + k + 1]
            running_sum -= nums[pos - k]

        return result


def main():
    ''' Test getAverages
    '''
    solution = Solution()

    test_cases = [
        ([7,4,3,9,1,8,5,2,6], 3),
        ([100000], 0),
        ([8], 100000),
        ([1, 2, 3, 4, 5, 6], 2,)
    ]
    for nums, k in test_cases:
        result = solution.getAverages(nums, k)
        print(nums, k, result)

if __name__ == "__main__":
    main()
