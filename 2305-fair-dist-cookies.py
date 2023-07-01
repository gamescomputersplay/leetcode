''' https://leetcode.com/problems/fair-distribution-of-cookies/
'''

class Solution:
    def distributeCookies(self, cookies, k):


        def recurse(so_far, n):
            # Recursively place the cookie
            # So far: what children have so far
            # n: which cookie to place next (index in cookies)

            nonlocal best_fairness

            # Recursion end:
            if n == len(cookies):
                best_fairness = min(best_fairness, max(so_far))
                return

            for pos, child in enumerate(so_far):

                new_so_far = so_far.copy()
                new_so_far[pos] += cookies[n]
                recurse(new_so_far, n + 1)

                # If it's child's first cookie, break
                # We don't need to test several zeros
                if child == 0:
                    break

        best_fairness = float("inf")
        so_far = [0 for _ in range(k)]
        recurse(so_far, 0)

        return best_fairness


def main():
    ''' Test distributeCookies
    '''
    solution = Solution()

    test_cases = [
        ([8,15,10,20,8], 2),
        ([6,1,3,2,2,4,1,2], 3),
    ]
    for cookies, k in test_cases:

        result = solution.distributeCookies(cookies, k)
        print(cookies, k, result)


if __name__ == "__main__":
    main()