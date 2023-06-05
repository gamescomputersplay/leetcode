''' https://leetcode.com/problems/check-if-it-is-a-straight-line/
'''

class Solution:
    def checkStraightLine(self, coordinates):

        # y = kx + a

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # Case: vertiacl line. All coordinates whould hve the same x.
        if x1 == x2:
            for x, _ in coordinates:
                if x != x1:
                    return False
            return True

        # Case: horizontal line. All coordinates whould hve the same x.
        if y1 == y2:
            for _, y in coordinates:
                if y != y1:
                    return False
            return True

        # Calculate k and a
        k = (y2 - y1) / (x2 - x1)
        a = y1 - (k * x1)

        # Check the coordsinates
        for x, y in coordinates:
            if y != k * x + a:
                return False
        return True

def main():
    ''' Test checkStraightLine
    '''
    solution = Solution()

    test_cases = [
        [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],
        [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]],
        [[1,1], [1,2], [1,3], [1,4]],
        [[1,1], [3,1]]

    ]
    for coordinates in test_cases:
        result = solution.checkStraightLine(coordinates)
        print(coordinates, result)


if __name__ == "__main__":
    main()

