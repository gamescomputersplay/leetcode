''' https://leetcode.com/problems/zigzag-conversion/
'''


class Solution:

    def convert(self, s, numRows):
        ''' Do the string zigzagging
        '''
        # Sanitize. Solution breaks with 1 row. Yet, it is trivial
        if numRows == 1:
            return s

        # Lists, each representing a row
        rows = [[] for _ in range(numRows)]
        # Pointer to the row to put the next letter to
        row_pointer = 0
        # Increase that will determine the next row
        pointer_inc = 1

        # Go through the letters
        for letter in s:

            # Add it to the row
            rows[row_pointer].append(letter)

            # Modify pointer
            row_pointer += pointer_inc

            # If the pointer is on the edge, reverse it
            if row_pointer == 0:
                pointer_inc = 1
            if row_pointer == numRows - 1:
                pointer_inc = -1

        # Combine lists into one string
        output = ""
        for row in rows:
            for letter in row:
                output += letter
        return output

    def convert_old(self, s, numRows):
        ''' Do the string zigzagging
        '''

        # First we put together all teh indexes here
        zigzag_indexes = []

        # Indexes of all top row letters (it will be used
        # in calculations for other rows too)
        # It is a little longer than actual top row, to ensure
        # correct generation of middle rows
        top_row = [i for i in range(0, len(s) + numRows * 2, max(1, 2 * numRows - 2))]

        for row in range(numRows):

            # Top row
            if row == 0:
                zigzag_indexes += [i for i in top_row if i < len(s)]

            # Bottom row
            elif row == numRows - 1:
                zigzag_indexes += [top + numRows - 1 for top in top_row if top + numRows - 1 < len(s)]

            # Middle rows
            else:
                for top in top_row:
                    zigzag_indexes += [top + diff for diff in [-row, row] if 0 < top + diff < len(s)]

        # Indexes to letter
        zigzag_letters = [s[i] for i in zigzag_indexes]

        # Generate the string and return
        return "".join(zigzag_letters)



def run_with_time(func):
    ''' Time function func
    '''

    start = time.time()
    for _ in range(10000):
        func("ABCDEFGHIJKLMNOPQRSTUVWXYZ"*10, 10)
    print(f"Done in {time.time() - start}")

def main():
    ''' test convert
    '''

    test_cases = [
        ("PAYPALISHIRING", 3), # PAHNAPLSIIGYIR
        ("PAYPALISHIRING", 4), # PINALSIGYAHRPI
        ("A", 1), # A
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1), # PAHNAPLSIIGYIR
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2), # PINALSIGYAHRPI
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3), # A
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4), # A
        ("ABCD", 3)
    ]

    solution = Solution()
    for string, num_rows in test_cases:
        print(string, num_rows, solution.convert(string, num_rows))


    run_with_time(solution.convert_old)
    run_with_time(solution.convert)


if __name__ == "__main__":
    import time
    main()
