''' https://leetcode.com/problems/longest-consecutive-sequence/
'''

class Solution:
    def longestConsecutive(self, nums):

        longest_seq = 0

        # numbers that would extend current seqs:
        # {num: [[start_left_edge, end+left_edge], [start_right_edge, end_right_edge]]}
        edges = {}

        for num in nums:

            # This number is all alone now, not merging to any range
            if num not in edges:
                new_range = [num - 1, num + 1]
                edges[num + 1] = [new_range]
                edges[num - 1] = [new_range]
                longest_seq = max(longest_seq, 1)

            # This number can extend one range
            elif num in edges and len(edges[num]) == 1:

                range_to_extend = edges[num][0]
                egde_left, edge_right = range_to_extend

                if egde_left == num:
                    del edges[num].remove(range_to_extend)
                    range_to_extend[0] = num - 1
                    if num - 1 not in edges:
                        edges[num - 1] = []
                    edges[num - 1].append(range_to_extend)
                    
                    


            # This number merges 2 ranges
            # elif num in edges and len(edges[num]) == 2:
            #     both_ranges = edges[num][0].extend(edges[num][1])
            #     new_range = [min(both_ranges), max(both_ranges)]

            print(num, edges)

        return longest_seq

def main():
    ''' Test longestConsecutive
    '''
    solution = Solution()

    test_cases = [
        [1, 2],
        # [100,4,200,1,3,2], #4
        # [0,3,7,2,5,8,4,6,0,1], #9

    ]
    for nums in test_cases:
        result = solution.longestConsecutive(nums)
        print(nums, result)


if __name__ == "__main__":
    main()
