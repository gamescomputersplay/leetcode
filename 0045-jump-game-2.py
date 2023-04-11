''' https://leetcode.com/problems/jump-game-ii/
'''

class Solution:
    def jump(self, nums):

        if len(nums) == 1:
            return 0

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

        #print(best_cells)

        if len(best_cells) == 1:
            return 1

        # Now we walk back to count the steps using pointer in best_cells "p"
        p = len(best_cells) - 2
        # Count the jumps
        jump_counter = 1
        # Which cell we need to jump to
        get_to = len(best_cells) - 1

        while p >= 0:

            if best_cells[p] >= get_to and best_cells[p - 1] < get_to:
                jump_counter += 1
                get_to = p

            p -=1
        
        # Problem can't be solved (should not happen with these test cases)
        if get_to > best_cells[0]:
            return -1
        
        # We under count one first jump
        return jump_counter + 1


def main():
    ''' Test jump
    '''
    solution = Solution()

    test_cases = [
        [0],
        [1,0],
        [2, 1, 0],
        [1, 2, 0],
        [2,3,1,1,4],
        [2,3,0,1,4],
    ]
    for nums in test_cases:
        result = solution.jump(nums)
        print(nums, result)

def random_case(size=10):
    ''' Test jump
    '''
    #random.seed(0)
    solution = Solution()

    test_cases = [
        [random.randint(0, 4) for _ in range(size)]
    ]
    for nums in test_cases:
        result = solution.jump(nums)
        print(nums, result)

if __name__ == "__main__":
    import random
    main()
    random_case(20)
