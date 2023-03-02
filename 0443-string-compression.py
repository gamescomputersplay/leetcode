''' https://leetcode.com/problems/string-compression/
'''

class Solution:
    def compress(self, chars):

        def write_group():
            ''' Things to do at the and of the group
            '''
            nonlocal write_pointer, group_count, current_group, current_char

            # Write the group's letter
            chars[write_pointer] = current_group
            write_pointer += 1

            # If there is only one letter, just rename the current group
            # and that's it
            if group_count == 1:
                current_group = current_char
                return
            
            # Otherwise we need to write in the number
            # Group size in text
            group_size_text = str(group_count)

            # Write it into the string
            for num_char in group_size_text:
                chars[write_pointer] = num_char
                write_pointer += 1

            # Initiate the new group
            current_group = current_char
            group_count = 1

        read_pointer = 1
        write_pointer = 0

        current_group = chars[0]
        current_char = chars[0]
        group_count = 1

        while read_pointer < len(chars):

            current_char = chars[read_pointer]

            # Case 1: Same char, keep counting the characters
            if current_char == current_group:
                group_count += 1
            
            # Case 2: Close the group (separate method,
            # as we will use it again outside of this look)
            else:
                write_group()
                
            read_pointer += 1

        # Close the last group
        write_group()

        # Truncate the string
        del chars[write_pointer:]

        return write_pointer

def main():
    ''' Test compress
    '''
    solution = Solution()

    test_cases = [
        ["a","a","b","b","c","c","c"],
        ["a"],
        ["a","b","b","b","b","b","b","b","b","b","b","b","b", "c"],
        ["a", "b", "c", "c"]

    ]
    for array in test_cases:
        array_original = array.copy()
        result = solution.compress(array)
        print("".join(array_original), "".join(array), result)



if __name__ == "__main__":
    main()
