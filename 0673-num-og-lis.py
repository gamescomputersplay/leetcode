''' https://leetcode.com/problems/number-of-longest-increasing-subsequence/
'''

class Solution:
    def findNumberOfLIS(self, nums):

        longsest_lis = 0
        count_of_longest_lis = 0

        # [(num, len so far, cont so far)]
        edges = []

        for num in nums:

            best_len_so_far = 0
            best_count_so_far = 1

            for edge, length, count in edges:
                if edge < num:
                    if length > best_len_so_far:
                        best_len_so_far = length
                        best_count_so_far = count
                    elif length == best_len_so_far:
                        best_count_so_far += count

            edges.append((num, best_len_so_far + 1, best_count_so_far))
            longsest_lis = max(longsest_lis, best_len_so_far + 1)

            #print(num, edges)

        # Iterate thorugh the list again and find the sum of counts of the longest chain
        for _, length, count in edges:
            if length == longsest_lis:
                count_of_longest_lis += count

        return count_of_longest_lis

def main():
    ''' Test findNumberOfLIS
    '''
    solution = Solution()

    test_cases = [
        [1,3,5,4,7], #2
        [2,2,2,2,2], #5
        [1],
        [1, 2, 3], 
        [3, 2, 1],
    ]
    for nums in test_cases:
        result = solution.findNumberOfLIS(nums)
        print(f"{nums}, {result}")

if __name__ == "__main__":
    main()