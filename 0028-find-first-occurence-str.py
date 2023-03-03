''' https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
'''

class Solution:
    def strStr(self, haystack, needle):
        
        def calc_hash(string):
            ''' Calculate the hash of a string
            '''
            hash = 0

            for char in string:
                hash += code[char]
            
            return hash

        # This invalid input will break hashing for haystack,
        # so let's get it out of the way
        if len(haystack) < len(needle):
            return -1

        # Some scrablisg to randomize the hash
        code = {char: pos + 100 * (pos % 7 + 3) + 11 for pos, char in enumerate("abcdefghijklmnopqrstuvwxyz")}

        needle_hash = calc_hash(needle)
        haystack_window_hash = calc_hash(haystack[:len(needle)])

        # Let's go through all possible position of needle in haystack
        for shift in range(len(haystack) - len(needle) + 1):

            # If hashes match, do the regular letter-by-letter slow match
            if needle_hash == haystack_window_hash:

                for letter_haystack, ketter_needle in \
                    zip(needle, haystack[shift: shift+len(needle)]):
                    if letter_haystack != ketter_needle:
                        break
                # No mismatches found - return current posisiton of the window
                else:
                    return shift

            # Update the haystack hash
            if shift < len(haystack) - len(needle):
                haystack_window_hash -= code[haystack[shift]]
                haystack_window_hash += code[haystack[shift + len(needle)]]

        return -1


def main():
    ''' test strStr
    '''
    test_cases = [
        ("sadbutsad", "sad"),
        ("leetcode", "leeto"),
        ("helloworld", "low"),
        ("a"*100000 + "b", "a"*50000 + "b"),
        ("b", "aaaa"),
        ("a", "b")
    ]

    solution = Solution()
    for haystack, needle in test_cases:
        print(haystack[-10:], needle[-10:], solution.strStr(haystack, needle))


if __name__ == "__main__":
    main()
