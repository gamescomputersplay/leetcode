''' https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
'''

class Solution:
    def canMakeArithmeticProgression(self, arr):

        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False

        return True

def main():
    ''' Test canMakeArithmeticProgression
    '''
    solution = Solution()

    test_cases = [
        [3,5,1],
        [1,2,4],
    ]
    for arr in test_cases:
        result = solution.canMakeArithmeticProgression(arr)
        print(arr, result)


if __name__ == "__main__":
    main()
