''' https://leetcode.com/problems/candy/
'''

class Solution:
    def candy(self, ratings):

        # One candy of there is one kid
        if len(ratings) == 1:
            return 1

        # Candy amount (start with 1 for all)
        candy = [1 for _ in range(len(ratings))]

        # Traverse rating left-to-right, then right-to-left
        for iterator in [range(len(ratings)), range(len(ratings)-1, -1, -1)]:
            for pos in iterator:

                # Look left
                if pos > 0:
                    neighbour_candy = candy[pos - 1]
                    neighbour_rating = ratings[pos - 1]
                    if neighbour_rating < ratings[pos] and neighbour_candy >= candy[pos]:
                        candy[pos] = neighbour_candy + 1

                # Look right
                if pos < len(ratings) - 1:
                    neighbour_candy = candy[pos + 1]
                    neighbour_rating = ratings[pos + 1]
                    if neighbour_rating < ratings[pos] and neighbour_candy >= candy[pos]:
                        candy[pos] = neighbour_candy + 1

        return sum(candy)

def main():
    ''' Test candy
    '''
    solution = Solution()

    test_cases = [
        [1,0,2], #5
        [1,2,2], #4
        [1,2,0,3,4,1,5,], #12
        [1,1,2,2,2,2,1,1], #10
        [1, 2, 3, 4, 5], #15
        [5, 4, 3, 2, 1], #15
    ]
    for ratings in test_cases:
        result = solution.candy(ratings)
        print(ratings, result)


if __name__ == "__main__":
    main()
