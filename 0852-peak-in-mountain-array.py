''' https://leetcode.com/problems/peak-index-in-a-mountain-array/
'''

class Solution:
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr)-1

        while True:

            center = (left + right) // 2

            if arr[center - 1] < arr[center] > arr[center + 1]:
                return center

            if arr[center - 1] < arr[center]:
                left = center
            else:
                right = center


def main():
    ''' Test peakIndexInMountainArray
    '''
    solution = Solution()

    test_cases = [
        [0,1,0],
        [0,2,1,0],
        [0,10,5,2],
        [0,1,2,3,4,7,4,3,2,1],
    ]
    for arr in test_cases:
        result = solution.peakIndexInMountainArray(arr)
        print(f"{arr}, {result}")

if __name__ == "__main__":
    main()
