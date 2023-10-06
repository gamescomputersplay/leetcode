''' https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
'''

class Solution:
    def winnerOfGame(self, colors):

        # Moves that Alice and Bob can make
        alice, bob = 0, 0

        # Previous balls of this color
        aaa, bbb = 0, 0

        for ball in colors + " ":
            if ball == "A":
                aaa += 1
                if aaa > 2:
                    alice += 1
                bbb = 0
            elif ball == "B":
                bbb += 1
                if bbb > 2:
                    bob += 1
                aaa = 0

        return bob < alice

def main():
    ''' Test winnerOfGame
    '''
    solution = Solution()

    test_cases = [
        "AAABABB",
        "AA",
        "ABBBBBBBAAA",
    ]
    for colors in test_cases:
        result = solution.winnerOfGame(colors)
        print(colors, result)

if __name__ == "__main__":
    main()