''' https://leetcode.com/problems/find-eventual-safe-states/
'''

class Solution:
    def eventualSafeNodes(self, graph):

        # Transform info list of sets
        graph = [set(node) for node in graph]
        #print(graph)

        # Terminal nodes are safe
        safe = set(i for i, node in enumerate(graph) if not node)
        #print("safe", safe)

        # Dict of nodes pointing to this node
        point_here = {}
        for from_node, to_nodes in enumerate(graph):
            for to_node in to_nodes:
                if to_node not in point_here:
                    point_here[to_node] = set()
                point_here[to_node].add(from_node)
        #print(point_here)

        # Flag to keep going as long as there are updates to list of safe
        keep_going = True
        while keep_going:
            keep_going = False

            # Put newly found safe nodes here
            new_safe = set()

            # Find all the nodes that poiunt to current safe nodes
            for safe_node in safe:
                if safe_node in point_here:
                    to_delete = []
                    for points_to_safe in point_here[safe_node]:

                        # If node points ONLY to safe nodes - it is safe
                        if graph[points_to_safe].issubset(safe):
                            new_safe.add(points_to_safe)
                            to_delete.append(points_to_safe)
                            keep_going = True

                    # Remove nodes that are safe
                    for item in to_delete:
                        point_here[safe_node].remove(item)

            safe.update(new_safe)

        return sorted(list(safe))

def main():
    ''' Test eventualSafeNodes
    '''
    solution = Solution()

    test_cases = [
        [[1,2],[2,3],[5],[0],[5],[],[]], #2456
        [[1,2,3,4],[1,2],[3,4],[0,4],[]], #4
        [[1],[]], #01
        [[]], #0
        [[0]], #-
        [[0],[1,2,3,4],[1,3,4],[2,4],[2]], #-
        [[],[0,2,3,4],[3],[4],[]], #01234
        [[1,2,3,4],[1,2,3,4],[3,4],[4],[]], #234
        [[1,2,3,4],[2],[1],[4],[]], #34
        [[1,3,4,5],[],[],[],[],[2,4]], #012345
        [[1,3,4,5],[],[],[],[2],[2,4]], #012345
    ]
    for graph in test_cases:
        result = solution.eventualSafeNodes(graph)
        print(f"{graph}, {result}")

if __name__ == "__main__":
    main()
