''' https://leetcode.com/problems/minimum-penalty-for-a-shop/
'''

class Solution:
    def bestClosingTime(self, customers):

        curr_penalty = 0
        best_penalty = curr_penalty
        best_closing = len(customers)

        for pos in range(len(customers)-1, -1, -1):
            if customers[pos] == "Y":
                curr_penalty += 1
            else:
                curr_penalty -= 1

            if curr_penalty <= best_penalty:
                best_penalty = curr_penalty
                best_closing = pos

        return best_closing

def main():
    ''' Test bestClosingTime
    '''
    solution = Solution()

    test_cases = [
        "YYNY",
        "NNNNN",
        "YYYY",
        "Y",
        "N",
    ]
    for string in test_cases:

        result = solution.bestClosingTime(string)
        print(string, result)


if __name__ == "__main__":
    main()
