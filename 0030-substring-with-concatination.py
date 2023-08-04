''' https://leetcode.com/problems/substring-with-concatenation-of-all-words/
'''

class Solution:
    def findSubstring(self, s, words):

        result = []

        word_len = len(words[0])

        words_counts = {}
        for word in words:
            words_counts[word] = words_counts.get(word, 0) + 1

        # We start the window at all the position between 0 and word_len
        for window_start in range(word_len):

            found = {}
            for chunk_n in range(len(words)):
                chunk = s[window_start + chunk_n * word_len:window_start + (chunk_n + 1) * word_len]
                found[chunk] = found.get(chunk, 0) + 1

            if words_counts == found:
                result.append(window_start)

            for i in range((len(s) - window_start )// word_len - len(words)):
                outgoing = s[window_start + i * word_len:window_start + (i + 1) * word_len]
                incoming = s[window_start + (i + len(words)) * word_len:window_start + (i + len(words) + 1) * word_len]

                found[outgoing] -= 1
                if found[outgoing] == 0:
                    del found[outgoing]
                found[incoming] = found.get(incoming, 0) + 1

                if words_counts == found:
                    result.append(window_start + (i + 1) * word_len)

        return result


    def findSubstring_old(self, s, words):

        result = []

        # This is the word size we are looking for
        word_size = len(words[0])

        # Check word. Something we will use to check if
        # matches match all words, accounting for duplicates
        words.sort()
        check_word = "".join(words)

        # Transform words into set for faster search
        words_set = set(words)

        # This list will contain at which position any substrings were found
        substring_found_at = set()

        # Move the window through the string
        for pos in range(len(s) - word_size + 1):

            if s[pos:pos+word_size] in words_set:
                substring_found_at.add(pos)

        # Now find the subset that might be a match
        # (has right number matches at the right intervals)
        for first_match_at in substring_found_at:

            # Generate required match sequence
            for shift_count in range(1, len(words)):
                next_match = first_match_at + shift_count * word_size

                # If we didn't have a match where it should be
                # This is not a substring we are looking for
                if next_match not in substring_found_at:
                    break
            else:

                # At this point we know there is a place that matches
                # the right number fo words in a row, but we don't know
                # if those are the right words

                # We will break down the string, construct a check word
                # and see if it matches original check word
                new_words = [s[first_match_at + shift * word_size:first_match_at + (shift + 1) * word_size]
                               for shift in range(len(words))]
                new_words.sort()
                new_check_word = "".join(new_words)

                if new_check_word == check_word:
                    result.append(first_match_at)

        return result
    
def main():
    ''' Test findSubstring
    '''
    solution = Solution()

    test_cases = [
        ("barfoothefoobarman", ["foo","bar"]), # [0, 9]
        ("wordgoodgoodgoodbestword", ["word","good","best","word"]), # []
        ("barfoofoobarthefoobarman", ["bar","foo","the"]), # [6, 9, 12]
        ("a", ["a"]), # [0]
        ("aba", ["a"]), # [0, 2]
        ("a", ["a", "b"]), # []
    ]
    for string, words in test_cases:
        result = solution.findSubstring(string, words)
        print(string, words, result)

if __name__ == "__main__":
    main()
