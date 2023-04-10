''' https://leetcode.com/problems/jump-game-ii/
'''

class Solution:
    def jump(self, nums):

        best_cells = []
        best_cell = None
        farthest = None

        for pos, value in enumerate(nums):
            
            if best_cell is None or pos + value > farthest:
                best_cell = pos
                farthest = pos + value

            best_cells.append(farthest)

            if farthest >= len(nums) - 1:
                break

        print(best_cells)
        return 0


def main():
    ''' Test jump
    '''
    solution = Solution()

    test_cases = [
        [2,3,1,1,4],
        [2,3,0,1,4],
    ]
    for nums in test_cases:
        result = solution.jump(nums)
        print(nums, result)

def random_case(size=10):
    ''' Test jump
    '''
    random.seed(0)
    solution = Solution()

    test_cases = [
        [random.randint(0, 4) for _ in range(size)]
    ]
    for nums in test_cases:
        result = solution.jump(nums)
        print(nums, result)

if __name__ == "__main__":
    import random
    #main()
    random_case(20)
