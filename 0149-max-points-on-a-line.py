''' https://leetcode.com/problems/max-points-on-a-line/
'''

class Solution:
    def maxPoints(self, points):

        if len(points) == 1:
            return 1

        points.sort()

        # To track points on lines as in {(tilt, shift): [points]}
        lines = {}

        # Go through all pairs
        for i, point1 in enumerate(points):
            for point2 in points[:i]:

                # Calculte tile and shift (y = tilt * x + shift)
                (x1, y1), (x2, y2) = point1, point2
                dx, dy = x2 - x1, y2 - y1
                tilt = None if dx == 0 else dy / dx
                # rounding to prevent weird floating-point calclation issue
                shift = y1 if dy == 0 else round(x1 - (dx * y1) / dy, 7)

                lines[(tilt, shift)] = lines.get(((tilt, shift)), 0) + 1

        # Restore number of points from numner of pair
        return int((2 * max(lines.values())) ** 0.5) + 1

def main():
    ''' Test maxPoints
    '''
    solution = Solution()

    test_cases = [
        [[1,1],[2,2],[3,3]], #3
        [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], #4
        [[0,0]],
        [[7,3],[19,19],[-16,3],[13,17],[-18,1],[-18,-17],[13,-3],[3,7],[-11,12],[7,19],[19,-12],[20,-18],[-16,-15],[-10,-15],[-16,-18],[-14,-1],[18,10],[-13,8],[7,-5],[-4,-9],[-11,2],[-9,-9],[-5,-16],[10,14],[-3,4],[1,-20],[2,16],[0,14],[-14,5],[15,-11],[3,11],[11,-10],[-1,-7],[16,7],[1,-11],[-8,-3],[1,-6],[19,7],[3,6],[-1,-2],[7,-3],[-6,-8],[7,1],[-15,12],[-17,9],[19,-9],[1,0],[9,-10],[6,20],[-12,-4],[-16,-17],[14,3],[0,-1],[-18,9],[-15,15],[-3,-15],[-5,20],[15,-14],[9,-17],[10,-14],[-7,-11],[14,9],[1,-1],[15,12],[-5,-1],[-17,-5],[15,-2],[-12,11],[19,-18],[8,7],[-5,-3],[-17,-1],[-18,13],[15,-3],[4,18],[-14,-15],[15,8],[-18,-12],[-15,19],[-9,16],[-9,14],[-12,-14],[-2,-20],[-3,-13],[10,-7],[-2,-10],[9,10],[-1,7],[-17,-6],[-15,20],[5,-17],[6,-6],[-11,-8]], #6
        [[1,0],[0,0]], #2
        [[-783,-667],[-870,-747],[87,133],[0,53],[261,293],[-609,-507],[-435,-347],[870,853],[435,453],[609,613],[174,213],[-261,-187],[-348,-267],[-87,-27],[-174,-107],[783,773],[696,693]], #17
        
    ]

    for points in test_cases:
        result = solution.maxPoints(points)
        print(points, result)


if __name__ == "__main__":
    main()
