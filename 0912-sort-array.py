''' https://leetcode.com/problems/sort-an-array/
'''

class Solution:

    def sortArray(self, nums):
                  
        def merge_arrays(left, right):
            ''' Merge two sorted arrays
            '''

            merged = []
            pointer_left = 0
            pointer_right = 0

            while pointer_left < len(left) or pointer_right < len(right):

                if pointer_left == len(left):
                    merged.append(right[pointer_right])
                    pointer_right += 1
                elif pointer_right == len(right):
                    merged.append(left[pointer_left])
                    pointer_left += 1
                elif left[pointer_left] <= right[pointer_right]:
                    merged.append(left[pointer_left])
                    pointer_left += 1
                else:                    
                    merged.append(right[pointer_right])
                    pointer_right += 1

            return merged

        def merge_sort(array):
            ''' Recursive sorting function'''

            # Exit the recursion if array is 0 or 1 long
            # Which makes it a sorted array
            if len(array) <= 1:
                return array
            
            # Break into two halfes
            left = array[:len(array)//2]
            right = array[len(array)//2:]

            # Sort each half
            left = merge_sort(left)
            right = merge_sort(right)

            # Merge results
            merged = merge_arrays(left, right)

            return merged

        return merge_sort(nums)


def main():
    ''' Test sortArray
    '''
    solution = Solution()

    test_cases = [
        [5,2,3,1],
        [5,1,1,2,0,0],
    ]
    for array in test_cases:
        original_array = array.copy()
        result = solution.sortArray(array)
        print(original_array, result)

def run_large_test(size):
    ''' Test and time one execution for size "size"
    '''
    solution = Solution()
    array = [random.randint(0, size) for _ in range(size)]
    start = time.time()
    solution.sortArray(array)
    elapsed = time.time() - start
    print(f"{size}: {elapsed}")


def test_speed():
    ''' Perform speed test for increasing sizes
    '''
    for power in range(20):
        size = 2 ** power
        run_large_test(size)

if __name__ == "__main__":
    import random
    import time
    #main()
    test_speed()
