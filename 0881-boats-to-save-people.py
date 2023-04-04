''' https://leetcode.com/problems/boats-to-save-people/
'''

class Solution:
    def numRescueBoats(self, people, limit):

        people.sort()

        # Triage people into:

        chubbies, skinnies, midsizes = 0, 0, 0

        for position, person in enumerate(people):

            if person < limit / 2:
                # Skinnies: Maybe can share a boat with a chubby,
                # but otherwise fit 2 in a boat
                skinnies  = position + 1

            if person > limit / 2:
                # Chubbies: Maybe can share a boat with a skinny,
                # but otherwise require a whole boat
                chubbies = len(people) - position
                break

        midsizes = len(people) - skinnies - chubbies

        #print(skinnies, midsizes, chubbies)
        
        # Pointer to see how many skinnies can boat up with chubbies
        skinny_pointer = skinnies - 1

        # Track the number of successful chubby-skinny matches
        found_pairs = 0

        # Flag that there are no more possible matches
        matching_possible = True

        # Go through the chubsters
        for chubby_pointer in range(len(people) - chubbies, len(people)):

            # Trying to find a suitable skinny for him
            while True:

                # Reached the end of the skinny list: no more matches
                if skinny_pointer < 0:
                    matching_possible = False
                    break

                # Found a skinny that maximized boat load
                if people[chubby_pointer] + people[skinny_pointer] <= limit:
                    #print("Match", chubby,  skinnies[skinny_pointer])
                    found_pairs += 1
                    skinny_pointer -= 1
                    break

                skinny_pointer -= 1

            if not matching_possible:
                break
        
        # Total number of boats is:
        # - Successful chubby-skinny pairs (1 pair per boat)
        # - Chubbies who didn't find a pair (1 chubster per boat)
        # - Remaining skinnies and midsizes (2 per boat)
        boats = found_pairs + \
                (chubbies - found_pairs) + \
                (skinnies - found_pairs + midsizes) / 2

        #print(found_pairs, (chubbies - found_pairs), (skinnies - found_pairs + midsizes) / 2)

        # Ceiling the number of boats
        return int(boats + 0.5)

    def numRescueBoats_v1(self, people, limit):
        people.sort()

        # Triage people into:

        chubbies, skinnies, midsizes = [], [], []

        for person in people:

            if person > limit / 2:
                # Chubbies: Maybe can share a boat with a skinny,
                # but otherwise require a whole boat
                chubbies.append(person)

            elif person < limit / 2:
                # Skinnies: Maybe can share a boat with a chubby,
                # but otherwise fit 2 in a boat
                skinnies.append(person)

            else:
                # Can share a boat with self or any skinny
                midsizes.append(person)

        #print(skinnies, midsizes, chubbies)
        
        # Pointer to see how many skinnies can boat up with chubbies
        skinny_pointer = len(skinnies) - 1

        # Track the number of successful chubby-skinny matches
        found_pairs = 0

        # Flag that there are no more possible matches
        matching_possible = True

        # Go through the chubsters
        for chubby in chubbies:

            # Trying to find a suitable skinny for him
            while True:

                # Reached the end of the skinny list: no more matches
                if skinny_pointer < 0:
                    matching_possible = False
                    break

                # Found a skinny that maximized boat load
                if chubby + skinnies[skinny_pointer] <= limit:
                    #print("Match", chubby,  skinnies[skinny_pointer])
                    found_pairs += 1
                    skinny_pointer -= 1
                    break

                skinny_pointer -= 1

            if not matching_possible:
                break
        
        # Total number of boats is:
        # - Successful chubby-skinny pairs (1 pair per boat)
        # - Chubbies who didn't find a pair (1 chubster per boat)
        # - Remaining skinnies and midsizes (2 per boat)
        boats = found_pairs + \
                (len(chubbies) - found_pairs) + \
                (len(skinnies) - found_pairs + len(midsizes)) / 2

        #print(found_pairs, (len(chubbies) - found_pairs), (len(skinnies) - found_pairs + len(midsizes)) / 2)

        # Ceiling the number of boats
        return int(boats + 0.5)

def main():
    ''' Test numRescueBoats
    '''
    solution = Solution()

    test_cases = [
        ([1,2], 3), # 1
        ([3,2,2,1], 3), # 3
        ([3,5,3,4], 5), # 4
        ([1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
        ([1], 1),
        ([1], 2),


    ]
    for people, limit in test_cases:
        result = solution.numRescueBoats(people, limit)
        print(f"{people[:10]}, {limit}, {result}\n")

if __name__ == "__main__":
    main()
