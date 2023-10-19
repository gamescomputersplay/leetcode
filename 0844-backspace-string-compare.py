''' https://leetcode.com/problems/backspace-string-compare/
'''

class Solution:
    def backspaceCompare(self, s, t):


        def backspace(line, pointer):

            backspaces = 0
            while True:
                if backspaces == 0 and line[pointer] != "#" or pointer < 0:

                    return pointer
                if line[pointer] == "#":
                    backspaces += 1
                else:
                    backspaces -= 1
                pointer -= 1

        ps, pt = len(s) - 1, len(t) - 1

        ps = backspace(s, ps)
        pt = backspace(t, pt)

        while ps >= 0 or pt >= 0:

            # This happens if one line is over an one isn't
            if ps < 0 or pt < 0:
                return False

            if s[ps] != t[pt]:
                return False

            if s[ps] == t[pt] and t[pt] != "#":
                ps -= 1
                pt -= 1

            ps = backspace(s, ps)
            pt = backspace(t, pt)

        return True


def main():
    ''' Test backspaceCompare
    '''
    solution = Solution()

    test_cases = [
       ("ab#c", "ad#c"),
       ("ab##", "c#d#"),
       ("a#c", "b"),
       ("a##b###c", "c"),
       ("xywrrmp", "xywrrmu#p"),
    ]
    for s, t in test_cases:
        result = solution.backspaceCompare(s, t)
        print(f"{s}, {t}, {result}")

if __name__ == "__main__":
    main()
