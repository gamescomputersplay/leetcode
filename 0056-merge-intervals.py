''' https://leetcode.com/problems/merge-intervals/
'''

class Solution:
    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])

        result = []

        current_from, current_to = intervals[0]

        for pos, (frm, to) in enumerate(intervals):

            # Close the interval
            if frm > current_to:
                result.append([current_from, current_to])
                current_from = frm
                current_to = to

            # Extend interval
            else:
                current_to = max(current_to, to)

            # Write the last interval
            if pos == len(intervals) - 1:
                result.append([current_from, current_to])

            #print(pos, (frm, to), result, [current_from, current_to])

        return result

def main():
    ''' Test merge
    '''
    solution = Solution()

    test_cases = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]],
        [[1, 5], [2, 5], [3, 6]],
        [[1, 2]],
        [[1,4],[0,4]],
    ]
    for intervals in test_cases:
        result = solution.merge(intervals)
        print(intervals, result)

if __name__ == "__main__":
    main()
