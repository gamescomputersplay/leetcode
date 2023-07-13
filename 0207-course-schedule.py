''' https://leetcode.com/problems/course-schedule/
'''

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # Dependency dict {course:{requisites},...}
        dependency = {n:set()for n in range(numCourses)}
        for to_take, must_have in prerequisites:
            dependency[to_take].add(must_have)
        print(dependency)

        has_taken = set()

        # Keep going uptil there are no dependencies left (success)
        # Or no progress achieved (failure)
        has_progress = True
        while dependency:
            has_progress = False

            new_dependency = {}
            for to_take, must_have in dependency.items():

                # We took all the required courses - can take this one
                if must_have.issubset(has_taken):
                    has_taken.add(to_take)
                    has_progress = True
                    continue

                # Otherwise just copy dependency to a new iteration
                new_dependency[to_take] = must_have

            # Return Fail if there is no progress after full iteration
            if not has_progress:
                return False

            # Update dependency for teh new iteration
            dependency = new_dependency

        # Dependencies list is empty - return Success
        return True

def main():
    ''' Test canFinish
    '''
    solution = Solution()

    test_cases = [
        (2, [[1,0]]),
        (2, [[1,0],[0,1]]),
        (5, [[0,1],[0,3],[3,2],[4,2],[2,1]])
    ]
    for numCourses, prerequisites in test_cases:
        result = solution.canFinish(numCourses, prerequisites)
        print(numCourses, prerequisites, result)

if __name__ == "__main__":
    main()
