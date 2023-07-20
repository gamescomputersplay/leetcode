''' https://leetcode.com/problems/longest-consecutive-sequence/
'''

class Solution:
    def longestConsecutive(self, nums):

        # Deduplicate nums
        nums = list(set(nums))

        def save_range(new_range):
            nonlocal longest_seq
            for i in range(2):
                if new_range[i] not in edges:
                    edges[new_range[i]] = []
                edges[new_range[i]].append(new_range)
            longest_seq = max(longest_seq, new_range[1] - new_range[0] - 1)

        def pop_range(num):
            range_to_pop = edges[num][-1]
            egde_left, edge_right = range_to_pop

            # Remove this range from both edges
            for edge_to_delete in egde_left, edge_right:
                edges[edge_to_delete].remove(range_to_pop)

            return range_to_pop

        longest_seq = 0

        # numbers that would extend current seqs:
        # {num: [[start_left_edge, end+left_edge], [start_right_edge, end_right_edge]]}
        edges = {}

        for num in nums:

            # This number is all alone now, not merging to any range
            if num not in edges:
                new_range = [num - 1, num + 1]
                save_range(new_range)

            # This number can extend one range
            elif num in edges and len(edges[num]) == 1:

                range_to_extend = pop_range(num)

                # Update the range edges
                if num == range_to_extend[0]:
                    range_to_extend[0] = num - 1
                if num == range_to_extend[1]:
                    range_to_extend[1] = num + 1

                # Save the range
                save_range(range_to_extend)

            # This number merges 2 ranges
            elif num in edges and len(edges[num]) == 2:

                combined = pop_range(num)
                combined.extend(pop_range(num))

                combined_range = [min(combined), max(combined)]

                # Save the range
                save_range(combined_range)

        return longest_seq

def main():
    ''' Test longestConsecutive
    '''
    solution = Solution()

    test_cases = [
        [1, 2, 0, 3, 5, 6, 4], #7
        [100,4,200,1,3,2], #4
        [0,3,7,2,5,8,4,6,0,1], #9

    ]
    for nums in test_cases:
        result = solution.longestConsecutive(nums)
        print(nums, result)


if __name__ == "__main__":
    main()
