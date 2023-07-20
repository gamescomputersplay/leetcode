''' https://leetcode.com/problems/longest-consecutive-sequence/
'''

class Solution:
    def longestConsecutive(self, nums):

        # Deduplicate nums
        nums = list(set(nums))

        def save_range(beg, end):
            nonlocal longest_seq
            for key, val in [(beg, end), (end, beg)]:
                if key not in edges:
                    edges[key] = []
                edges[key].append(val)
            longest_seq = max(longest_seq, end - beg - 1)

        def pop_range(key):
            val = edges[key].pop()
            # Remove the other edge
            edges[val].remove(key)

            return min(key, val), max(key, val)

        longest_seq = 0

        # numbers that would extend current seqs:
        # {num: [[start_left_edge, end+left_edge], [start_right_edge, end_right_edge]]}
        edges = {}

        for num in nums:

            # This number is all alone now, not merging to any range
            if num not in edges:
                save_range(num - 1, num + 1)

            # This number can extend one range
            elif num in edges and len(edges[num]) == 1:

                beg, end = pop_range(num)

                # Update the range edges
                if num == beg:
                    beg = num - 1
                if num == end:
                    end = num + 1

                save_range(beg, end)

            # This number merges 2 ranges
            elif num in edges and len(edges[num]) == 2:

                a, b = pop_range(num)
                c, d = pop_range(num)

                save_range(min(a, b, c, d), max(a, b, c, d))

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
