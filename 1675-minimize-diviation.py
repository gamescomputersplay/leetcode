''' https://leetcode.com/problems/minimize-deviation-in-array/
'''

class Solution:
    def minimumDeviation(self, nums):
        pass

def main():
    ''' Test minimumDeviation
    '''
    solution = Solution()

    test_cases = [
        [1, 2, 3, 4],
        [4, 1, 5, 20, 3],
        [2, 10, 8],
    ]
    for array in test_cases:
        result = solution.minimumDeviation(array)
        print(array, result)



if __name__ == "__main__":
    main()
