''' https://leetcode.com/problems/new-21-game/
'''

class Solution:
    def new21Game(self, n, k, maxPts):
        ''' k: stop hitting
        n last before busted
        '''
        # probabilities of getting points
        probs = [1] + [0] * (k + maxPts)
        pointer = 0

        for _ in range(k):

            current_prob = probs[pointer]
            for step in range(1, maxPts + 1):
                probs[pointer + step] += current_prob / maxPts
            probs[pointer] = 0

            pointer += 1

        answer = sum(probs[:n+1])

        return answer

def main():
    ''' Test new21Game
    '''
    solution = Solution()

    test_cases = [
        (10, 1, 10),
        (6, 1, 10),
        (21, 17, 10),
        (9811, 8776, 1096),

    ]
    for n, k, maxPts in test_cases:
        result = solution.new21Game(n, k, maxPts)
        print(f"{n}, {k}, {maxPts}: {result}")



def long_case():
    solution = Solution()

    n, k, maxPts = (9811, 8776, 1096)
    start = time.time()
    result = solution.new21Game(n, k, maxPts)
    elapsed = time.time() - start

    print(n, k, maxPts, elapsed, "s")

if __name__ == "__main__":
    import time
    main()
    long_case()