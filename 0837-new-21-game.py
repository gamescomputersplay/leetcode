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
            add_prob = current_prob / maxPts
            for step in range(pointer + 1, pointer + maxPts + 1):
                probs[step] += add_prob
            probs[pointer] = 0

            pointer += 1
            #print(probs)
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
        (5710, 5070, 8516),

    ]
    for n, k, maxPts in test_cases:
        result = solution.new21Game(n, k, maxPts)
        print(f"{n}, {k}, {maxPts}: {result}")



def long_case():
    solution = Solution()

    n, k, maxPts = (5710, 5070, 8516)
    start = time.time()
    result = solution.new21Game(n, k, maxPts)
    elapsed = time.time() - start

    print(n, k, maxPts, elapsed, "s")

if __name__ == "__main__":
    import time
    main()
    long_case()