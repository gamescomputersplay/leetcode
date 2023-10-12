''' https://leetcode.com/problems/find-in-mountain-array/
'''

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, data):
        self.data = data

    def get(self, index):
        return self.data[index]

    def length(self):
        return len(self.data)

class Solution:

    def findInMountainArray(self, target, mountain_arr):

        def read(index):
            ''' Interface to MA that caches reads
            '''
            if index in cache:
                return cache[index]
            cache[index] = mountain_arr.get(index)
            return cache[index]

        def find_peak():
            ''' Find peak of a MA
            '''
            left = 0
            right = length

            while True:

                center = (left + right) // 2

                if read(center - 1) < read(center) > read(center + 1):
                    return center
                if read(center) > read(center + 1):
                    right = center
                else:
                    left = center

        def find_in_left(peak):
            ''' Tries to find target in the left half of MA [:peak + 1]
            '''

            left = 0
            right = peak + 1

            while True:

                center = (left + right) // 2

                if read(center) == target:
                    return center
                if right - left <= 1:
                    return -1

                if read(center) > target:
                    right = center
                else:
                    left = center

        def find_in_right(peak):
            ''' Tries to find target in the left half of MA [:peak + 1]
            '''

            left = peak
            right = length

            while True:

                center = (left + right) // 2

                if read(center) == target:
                    return center
                if right - left <= 1:
                    return -1

                if read(center) < target:
                    right = center
                else:
                    left = center


        cache = {}
        length = mountain_arr.length()

        # Find peak
        peak_index = find_peak()

        # Search in left and right parts of the array
        result = find_in_left(peak_index)
        if result >= 0:
            return result
        result = find_in_right(peak_index)

        return result


def main():
    ''' Test findInMountainArray
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,10,6,4,3,0], 11),
        ([1,2,3,4,5,3,1], 1),
        ([0,1,2,4,2,1], 3), 
        ([1, 3, 2], 0),
    ]
    for nums, target in test_cases:
        mountain_arr = MountainArray(nums)
        result = solution.findInMountainArray(target, mountain_arr)
        print(nums, target, result)


if __name__ == "__main__":
    main()
        