''' https://leetcode.com/problems/subsets/
'''

# This is almost the exact copy of the 0078.
# The only difference is that subsets are sorted first,
# before they chacked on being a duplicate

class Solution:
    def subsetsWithDup(self, nums):

        def subset_rec(array):
            ''' Recursive implementation + dynamic programming
            '''
            # Keep all results here
            nonlocal subsets, done

            # End recursion at 1 element
            if len(array) == 1:
                return
            
            for i in range(len(array)):

                # Delete all elements one by one
                array_copy = array.copy()
                del array_copy[i]
                # Following is the only line that is added in 0090
                array_copy.sort()

                # If we didn't do such array before:
                # store the result and recurse
                if tuple(array_copy) not in done:
                    subsets.add(tuple(array_copy))
                    subset_rec(array_copy)

            # Keep track of what's done
            done.add(tuple(array))

        done = set()
        subsets = set()

        subset_rec(nums)

        return [list(subset) for subset in subsets] + [[]] + [nums]
    
def main():
    ''' Test subsetsWithDup
    '''
    solution = Solution()

    test_cases = [

        [1,2,2], 
        [0],
        [4,4,4,1,4],
    ]

    for nums in test_cases:
        result = solution.subsetsWithDup(nums)
        print(nums, result, len(result), "\n")

def time_test():
    solution = Solution()
    start = time.time()
    for _ in range(10):
        nums = [i for i in range(1, 16)]
        solution.subsetsWithDup(nums)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    time_test()
