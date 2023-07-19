''' https://leetcode.com/problems/non-overlapping-intervals/
'''

class Solution:
    def eraseOverlapIntervals(self, intervals):

        # 1. Remove duplicates
        original_len = len(intervals)
        intervals = (tuple(element) for element in intervals)
        intervals = list(sorted(set(intervals)))
        duplicates = original_len - len(intervals)

        # Count tiles to detect overlaps
        tiles = {}
        for start, end in intervals:
            for tile in range(start, end):
                if tile not in tiles:
                    tiles[tile] = []
                tiles[tile].append(end - start)

        removed = 0

        for start, end in intervals:

            if end - start != 2:
                continue

            # 2-tile, both overlap: remove the tile
            if len(tiles[start]) > 1 and len(tiles[start + 1]) > 1:
                removed += 1
                tiles[start].remove(2)
                tiles[start + 1].remove(2)

            # 2 and 1 tile overlap: remove the 2 tile
            if len(tiles[start]) > 1 and 1 in tiles[start] or \
               len(tiles[start + 1]) > 1 and 1 in tiles[start+1]:
                removed += 1
                tiles[start].remove(2)
                tiles[start + 1].remove(2)

            # 2 2-tiles overlap, delete the second one
            if len(tiles[start + 1]) > 1 and 2 in tiles[start+1]:
                removed += 1
                tiles[start + 1].remove(2)
                tiles[start + 2].remove(2)        

        return duplicates + removed


def main():
    ''' Test eraseOverlapIntervals
    '''
    solution = Solution()

    test_cases = [
        [[1,2],[2,3],[3,4],[1,3]], #1
        [[1,2],[1,2],[1,2]], #2
        [[1,2],[2,3]], #0

    ]
    for intervals in test_cases:
        result = solution.eraseOverlapIntervals(intervals)
        print(f"{intervals}: {result}")

if __name__ == "__main__":
    main()
