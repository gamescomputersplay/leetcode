''' https://leetcode.com/problems/predict-the-winner/
'''

class Solution:
    def PredictTheWinner(self, nums):

        def minimax(pointers, score, whos_turn):

            # Right pointer went to the left of left pointer:
            # No more nums to take - who's the winner?
            if pointers[1] - pointers[0] < 0:
                return score[0] >= score[1]

            cache_key = tuple(pointers + score + [whos_turn])
            if cache_key in cache:
                return cache[cache_key]

            outcome = []
            for move in (0, 1):

                # Data for the next round
                num = nums[pointers[move]]
                new_pointers = pointers.copy()
                if move == 0:
                    new_pointers[0] += 1
                else:
                    new_pointers[1] -= 1

                new_score = score.copy()
                new_score[whos_turn] += num
                new_whos_turn = 1 if whos_turn == 0 else 0

                result = minimax(new_pointers, new_score, new_whos_turn)

                # Player 0 needs just 1 victory of player 0
                if whos_turn == 0 and result:
                    cache[cache_key] = True
                    return True

                outcome.append(result)

            # Player 1 needs only 1 loss of player 0
            cache[cache_key] = outcome[0] and outcome[1]
            return cache[cache_key]

        cache = {}

        return minimax([0, len(nums)-1], [0, 0], 0)

def large_case():
    solution = Solution()
    nums = list(range(1, 50))
    start = time.time()
    result = solution.PredictTheWinner(nums)
    elapsed = time.time() - start
    print(nums, result, elapsed)
    
def main():
    ''' Test PredictTheWinner
    '''
    solution = Solution()

    test_cases = [
        [1,5,2], #False
        [1,5,233,7], #True
    ]
    for nums in test_cases:
        result = solution.PredictTheWinner(nums)
        print(nums, result)

if __name__ == "__main__":
    import time
    main()
    large_case()
