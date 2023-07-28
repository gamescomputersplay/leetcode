''' https://leetcode.com/problems/predict-the-winner/
'''

class Solution:
    def PredictTheWinner(self, nums):

        def minimax(remaining_nums, score, whos_turn):

            # No more nums to take - who's the winner?
            if not remaining_nums:
                return score[0] >= score[1]

            cache_key = tuple(remaining_nums + score + [whos_turn])
            if cache_key in cache:
                return cache[cache_key]

            outcome = []
            for move in (0, -1):

                # Data for the next round
                num = remaining_nums[move]
                new_remaining_nums = remaining_nums[1:] if move == 0 else remaining_nums[:-1]
                new_score = score.copy()
                new_score[whos_turn] += num
                new_whos_turn = 1 if whos_turn == 0 else 0

                result = minimax(new_remaining_nums, new_score, new_whos_turn)

                # Player 0 needs just 1 victory of player 0
                if whos_turn == 0 and result:
                    cache[cache_key] = True
                    return True

                outcome.append(result)

            # Player 1 needs only 1 loss of player 0
            cache[cache_key] = outcome[0] and outcome[1]
            return cache[cache_key]

        cache = {}

        return minimax(nums, [0, 0], 0)

def large_case():
    solution = Solution()
    nums = list(range(1, 23))
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
