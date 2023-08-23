''' https://leetcode.com/problems/reorganize-string/
'''

class Solution:
    def reorganizeString(self, s):

        # Create dict {"char":count, ...}
        characters = {}
        for ch in s:
            characters[ch] = characters.get(ch, 0) + 1

        # Convert it into a list[(character, count)],
        # and sort by counts, desc
        characters_list = list(characters.items())
        characters_list.sort(key=lambda x: -x[1])

        # If the most popular character is more than half length of the string
        # Can't have unrepeated characters
        if characters_list[0][1] > (len(s) + 1)// 2:
            return ""

        # list with slots for the new string
        result_str = [None for _ in range(len(s))]

        # Populate the string even than odd indexes,
        # starting from most popular character
        pos = 0
        for ch, count in characters_list:
            for _ in range(count):
                result_str[pos] = ch
                pos += 2
                if pos >= len(result_str):
                    pos = 1

        return "".join(result_str)

def main():
    ''' Test reorganizeString
    '''
    solution = Solution()

    test_cases = [
        "a",
        "aab",
        "aaaabb",
        "aaaabbbcccdddddddd",
    ]
    for s in test_cases:
        result = solution.reorganizeString(s)
        print(f"{s}: {result}")

if __name__ == "__main__":
    main()
