''' https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

class Solution:
    def twoSum(self, numbers, target):

        p1 = 0
        p2 = len(numbers) - 1

        while numbers[p1] + numbers[p2] != target:

            if numbers[p1] + numbers[p2] > target:
                p2 -=1
            else:
                p1 += 1

        return [p1 + 1, p2 + 1]

def main():
    ''' Test twoSum
    '''
    solution = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
    ]
    for numbers, target in test_cases:
        result = solution.twoSum(numbers, target)
        print(numbers, target, result)

if __name__ == "__main__":
    main()
