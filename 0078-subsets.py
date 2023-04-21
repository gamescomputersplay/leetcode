''' https://leetcode.com/problems/subsets/
'''

class Solution:
    def subsets(self, nums):

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
    ''' Test subsets
    '''
    solution = Solution()

    test_cases = [
       [1,2,3], 
        [0],
        [1,2,3,4,5],
    ]

    for nums in test_cases:
        result = solution.subsets(nums)
        print(nums, result, len(result), "\n")

def time_test():
    solution = Solution()
    start = time.time()
    for _ in range(10):
        nums = [i for i in range(1, 16)]
        solution.subsets(nums)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    time_test()
