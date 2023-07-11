''' https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def distanceK(self, root, target, k):

        def create_child_to_parent(node):
            for branch in [node.left, node.right]:
                if branch is not None:
                    child_to_parent[branch] = node
                    create_child_to_parent(branch)

        # Create a dict of {child: parent}
        child_to_parent = {}
        create_child_to_parent(root)

        # print("child_to_parent")
        # for child, parent in child_to_parent.items():
        #     print(f"{child.val} <- {parent.val}")

        # Create a dict{node, distance}

        # First by tracing back up to root
        distance_to_node = {}
        curr = target
        curr_distance = 0

        # Stack to trace it down later
        stack = []
        # And Path Up to ignore while going through stack
        path_up = set()

        while True:

            distance_to_node[curr_distance] = [curr]
            stack.append((curr, curr_distance))
            path_up.add(curr)

            if curr == root:
                break

            parent = child_to_parent[curr]
            curr = parent
            curr_distance += 1

        # Than tracing down from each node on the way up
        while stack:
            node, distance = stack.pop()
            for branch in (node.left, node.right):
                if branch is not None:
                    if branch not in path_up:
                        new_distance = distance + 1
                        if new_distance not in distance_to_node:
                            distance_to_node[new_distance] = []
                        distance_to_node[new_distance].append(branch)
                        stack.append((branch, new_distance))

        # print("distance_to_node")
        # for distance, nodes in distance_to_node.items():
        #     print(f"{distance} : {[node.val for node in nodes]}")

        if k in distance_to_node:
            return [node.val for node in distance_to_node[k]]
        return []

def main():
    ''' Test distanceK
    '''
    solution = Solution()

    test_cases = [
        ([3,5,1,6,2,0,8,None,None,7,4],5, 2),
        ([1], 1, 3),
        ([0,1,None,None,2,None,3,None,4], 3, 0),
        ([0,None,1,2,5,None,3,None,None,None,4], 2, 2)

    ]
    for tree, target_value, k in test_cases:
        root = binarytree.level_order_2_tree(tree)
        target = binarytree.find_target_node(root, target_value)
        result = solution.distanceK(root, target, k)
        print(str(root)[:50], str(target), k, result)

if __name__ == "__main__":
    main()
