''' https://leetcode.com/problems/remove-duplicate-letters/
'''

class Solution:
    def removeDuplicateLetters(self, s):

        def keep_leftmost(letter):
            ''' Keep only leftmost instance of letter
            '''
            nonlocal left_smaller
            while len(letters[letter]) > 1 and letters[letter][0] < left_smaller:
                pos = letters[letter].pop(0)
                s[pos] = ""

            for to_delete in letters[letter][1:]:
                s[to_delete] = ""
            letters[letter] = [letters[letter][0]]
            left_smaller = letters[letter][0]


        def try_to_delete_up_to(up_to_pos):
            ''' Try to delete letters to the left of position.
            Only delete if there is an instance to the right of position
            Also, if you keep a letter, don't delete smaller letters to the left
            '''
            
            for pos in range(up_to_pos - 1, -1, -1):
                if s[pos] == "":
                    continue
                letter = s[pos]
                if letters[letter][-1] > up_to_pos and letter >= s[up_to_pos]:
                    pos = letters[letter].pop(0)
                    s[pos] = ""
                else:
                    break


        # List if way easier to work with
        s = list(s)

        # List of all letters and their position
        # {"a": [2, 3, 6], "b": [1, 5], ...}
        letters = {}
        for pos, ch in enumerate(s):
            if ch not in letters:
                letters[ch] = []
            letters[ch].append(pos)

        left_smaller = 0

        for letter in sorted(letters.keys()):
            print(letter, s)
            keep_leftmost(letter)
            try_to_delete_up_to(letters[letter][0])

        return "".join(s)


def main():
    ''' Test removeDuplicateLetters
    '''
    solution = Solution()

    test_cases = [
        # "bcabc",
        "cbacdcbc",
        # "dddeffsbbbbaaebabbsf",
        # "abacb",
        # "bcbac", # bac
    ]

    for s in test_cases:
        result = solution.removeDuplicateLetters(s)
        print(s, result)


if __name__ == "__main__":
    main()
        