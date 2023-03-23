''' https://leetcode.com/problems/search-in-rotated-sorted-array/
'''

class Solution:
    def search(self, nums, target):

        def binary_search(first, last):
            ''' Search in the segment nums[first: last],
            assuming there are no rotation.
            It is assumed that last > first (meaning the segment is not empty)
            '''

            left, right = first, last

            while True:

                center = (left + right) // 2

                if nums[center] == target:
                    return center

                if nums[center] > target and (center == first or nums[center - 1] < target):
                    return -1
                if nums[center] < target and (center == last - 1 or nums[center + 1] > target):
                    return -1

                if nums[center] > target:
                    right = center
                else:
                    left = center 

        # First, check that the array was rotated at all
        # "=" will also cover 1-element array
        if nums[-1] >= nums[0]:
            return binary_search(0, len(nums))

        # Find the rotation point (first element of the right part)
        left, right = 0, len(nums)
        while True:

            center = (left + right) // 2

            if center < len(nums) - 2 and nums[center] > nums[center + 1]:
                rotation = center + 1
                break

            if center > 0 and nums[center] < nums[center - 1]:
                rotation = center
                break

            if nums[center] < nums[-1]:
                right = center
            else:
                left = center 

        if nums[0] <= target:
            return binary_search(0, rotation)
        
        return binary_search(rotation, len(nums))

    
def main():
    ''' Test search
    '''
    solution = Solution()

    test_cases = [
        ([3, 4,5,6,7,0,1,2], 0),
        ([4,5,6,7,0,1,2], 3),
        ([1, 3], 2),
        ([1, 2], 0),
        ([1], 0),
        ([1], 1),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8 ], 3),
        ([2], 3),
        ([3], 3),
        ([8], 3),
        ([2, 3], 3),
        ([3, 2], 3),
        ([8, 7], 3),
        ([7, 8], 3),
        ([7, 8, 9, 10, 3, 6], 7),
        ([4,5,6,7,0,1,2], 7),

    ]
    for array, target in test_cases:
        result = solution.search(array, target)
        check = array[result] == target if target in array else result == -1
        print(array, target, result, check)

def random_tests(runs):
    solution = Solution()
    for _ in range(runs):
        array = [random.randint(0, 10) for _ in range(random.randint(1, 10))]
        array = list(set(array))
        array.sort()
        rotation = random.randint(0, len(array))
        array = array[rotation:] + array[:rotation]
        target = random.randint(0, 10)
        result = solution.search(array, target)
        check = array[result] == target if target in array else result == -1
        if not check:
            print(array, target, result, check)
            break
    print(f"{runs} test okay")

if __name__ == "__main__":
    import random
    main()
    random_tests(1000)
