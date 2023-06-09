''' https://leetcode.com/problems/find-smallest-letter-greater-than-target/
'''

class Solution:
    def nextGreatestLetter(self, letters, target):

        left = 0
        right = len(letters)

        while True:

            center = (left + right) // 2
            #print(left, center, right, letters[left], letters[center])

            # Reached teh beginning
            if center == 0 and letters[center] > target:
                return letters[center]
            # Found the place
            if letters[center - 1] <= target < letters[center]:
                return letters[center]
            # Reached the edge
            if center == len(letters) - 1:
                return letters[0]

            if letters[center] <= target:
                left = center
            else:
                right = center


    def nextGreatestLetter_brute(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

def main():
    ''' Test nextGreatestLetter
    '''
    solution = Solution()

    test_cases = [
        (["c","f","j"], "a"),
        (["c","f","j"], "c"),
        (["x","x","y","y"], "z"),
        (['b', 'd', 'd', 'e', 'g', 'g'], "c"),
    ]
    for letters, target in test_cases:
        result = solution.nextGreatestLetter(letters, target)
        result_brute = solution.nextGreatestLetter_brute(letters, target)
        print(f"{letters}, {target}, {result}, {result_brute}")

def random_test(runs=100):
    solution = Solution()
    for _ in range(runs):
        letters = [random.choice("abcdefg") for _ in range(random.randint(2, 10))]
        letters.sort()
        target = random.choice("abcdefg") 
        result = solution.nextGreatestLetter(letters, target)
        result_brute = solution.nextGreatestLetter_brute(letters, target)
        if result != result_brute:
            print(f"Fail at: {letters}, {target}: {result} != {result_brute}")
            break
    else:
        print(f"All {runs} random tests are okay")

if __name__ == "__main__":
    import random
    main()
    random_test(1000000)
