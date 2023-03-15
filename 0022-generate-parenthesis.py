''' https://leetcode.com/problems/generate-parentheses/
'''

class Solution:

    def __init__(self):
        # Cache for dynamic programming
        self.cache = {}

    def generateParenthesis(self, n):

        # Result from cache
        if n in self.cache:
            return self.cache[n]

        # Recursions ends with 1 pair of parenthesis
        if n == 1:
            return ["()"]

        # Otherwise do the recursion

        # Use set, to deduplicate the results
        results = set()

        # For each combination for n-1 parenthesis
        for left_parenthesis in range(1, n):

            right_parenthesis = n - left_parenthesis

            for left_result in self.generateParenthesis(left_parenthesis):
                for right_result in self.generateParenthesis(right_parenthesis):
                    results.add(left_result + right_result)

            # There are several possible combinations with n parenthesis
        for center_result in self.generateParenthesis(n-1):
            results.add("(" + center_result + ")")
        
        # Convert to list to return
        self.cache[n] = list(results)
        return self.cache[n]

def main():
    ''' test by just running it with several N
    '''
    solution = Solution()
    for n in range(1, 15):
        start = time.time()
        results = solution.generateParenthesis(n)
        elapsed = time.time() - start
        print(f"{n}: {len(results)} results, {elapsed}s")

if __name__ == "__main__":
    import time
    main()