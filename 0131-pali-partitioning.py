''' https://leetcode.com/problems/palindrome-partitioning/
'''

class Solution:
    def partition(self, s):

        def is_pali(string):
            for i in range(len(string)//2):
                if string[i] != string[-1-i]:
                    return False
            return True

        def partition_remaining_string(start_with):
            ''' Do the partitioning for segment starting from "start_with"
            '''

            if len(s) - start_with == 1:
                return [[s[start_with]]]

            result = []

            # Also check if full string is a pali and include if it is
            if is_pali(s[start_with:]):
                result.append([s[start_with:]])

            # Check all possible lengths starting from the beginning
            for word_len in range(1, len(s) - start_with):

                # Skip non-palis
                word = s[start_with:start_with+word_len]
                if not is_pali(word):
                    continue

                # Check what the options for the remainder of teh string would be
                options = partition_remaining_string(start_with + word_len)
                
                # Combine them with the word
                for option in options:
                    new_option = [word]
                    new_option.extend(option)
                    result.append(new_option)

            return result

        return partition_remaining_string(0)

def main():
    ''' Test partition
    '''
    solution = Solution()

    test_cases = [
        "acabbaaa",
    ]
    for s in test_cases:
        result = solution.partition(s)
        print(s, result)


if __name__ == "__main__":
    main()
