''' https://leetcode.com/problems/single-element-in-a-sorted-array/
'''

class Solution:
    def singleNonDuplicate(self, nums):
        return None


def main():
    ''' Test searchInsert
    '''
    solution = Solution()

    test_cases = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([1], 1),
        ([1, 1, 2], 2),
        ([1, 2, 2], 1)
    ]
    for array, answer in test_cases:
        result = solution.singleNonDuplicate(array)
        print(array, result, result == answer)



if __name__ == "__main__":
    main()