''' https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
'''

class Solution:
    def maximumRequests(self, n, requests):

        def recurse(balance, done_requests, next_request):

            nonlocal max_requests

            # If there is a 0 balance, check if we have a max_requests
            if balance.count(0) == n:
                max_requests = max(max_requests, done_requests)

            # End of recursion when there is no more requests
            if next_request == len(requests):
                return

            # Try next requests, skipping 0 or several requests
            for i in range(next_request, len(requests)):

                building_from, building_to = requests[i]
                new_balance = balance.copy()
                new_balance[building_from] -= 1
                new_balance[building_to] += 1

                recurse(new_balance, done_requests + 1, i + 1)


        balance = [0 for _ in range(n)]
        max_requests = 0
        recurse(balance, 0, 0)

        return max_requests


def main():
    ''' Test maximumRequests
    '''
    solution = Solution()

    test_cases = [
        (5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]), #5
        (3, [[0,0],[1,2],[2,1]]), #3
        (4, [[0,3],[3,1],[1,2],[2,0]]), #4
    ]
    for n, requests in test_cases:
        result = solution.maximumRequests(n, requests)
        print(n, requests, result)


if __name__ == "__main__":
    main()
