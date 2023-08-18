''' https://leetcode.com/problems/maximal-network-rank/
'''

class Solution:
    def maximalNetworkRank(self, n, roads):

        # 0 if there are no connections
        if not roads:
            return 0

        # Get the dict of how many roads connect to this node
        # Also create a lookup set for roads
        node_roads = {}
        roads_set = set()
        for road1, road2 in roads:
            roads_set.add((road1, road2))
            roads_set.add((road2, road1))
            for road in road1, road2:
                node_roads[road] = node_roads.get(road, 0) + 1
        #print(node_roads)

        # Find the count of top connected nodes
        road_count = sorted(list(node_roads.values()))
        #print(road_count)

        # Get nodes with highest count
        top_nodes = []
        for node, count in node_roads.items():
            if count == road_count[-1]:
                top_nodes.append(node)

        # If there are 2 or more nodes like that:
        # Rank is 2* their roads if their are not connected,
        # or that -1 if they are
        if len(top_nodes) > 1:
            for node1 in top_nodes:
                for node2 in top_nodes:
                    if node1 != node2 and (node1, node2) not in roads_set:
                        return road_count[-1] * 2
            return road_count[-1] * 2 - 1

        # If there is only one top node, we need to find second most connected nodes
        # Get nodes with highest count
        second_top_nodes = []
        for node, count in node_roads.items():
            if count == road_count[-2]:
                second_top_nodes.append(node)

        for node in second_top_nodes:
            if (node, top_nodes[0]) not in roads_set:
                return road_count[-1] + road_count[-2]
        return road_count[-1] + road_count[-2] - 1

    
def main():
    ''' Test maximalNetworkRank
    '''
    solution = Solution()

    test_cases = [
        (4, [[0,1],[0,3],[1,2],[1,3]]), #4
        (5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]), #5
        (8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]), #5
        (2, [])
    ]
    for n, roads in test_cases:
        result = solution.maximalNetworkRank(n, roads)
        print(n, roads, result)

if __name__ == "__main__":
    main()
