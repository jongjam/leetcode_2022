"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# loop detection is possible because all you have to do is keep track of visited and traverse the graph
# and if you come across a visited node again it means that you are in a loop
# you would just need logic to detect a loop and exit in this case if this happens

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # returning an adjacency list
        # [ node 1 : [2, 4], node 2: [1, 3]]
        if node is None :
            return None

        # going to use bfs because in the case of cloning going down by level makes decent logical sense
        nodes = dict()

        def fill_map(first) :
            q = deque()
            visited = set()

            q.append(first)
            visited.add(first)

            
            while q :
                node = q.pop()
                nodes[node] = Node(node.val)
                for neighbor in node.neighbors :
                    if neighbor not in visited :
                        q.append(neighbor)
                    visited.add(neighbor) # visited is needed just to make sure we don't go over anything twice

        def bfs(first) :
            q = deque()
            visited = set()

            q.append(first)
            visited.add(first)

            while q :
                node = q.pop()
                for neighbor in node.neighbors :
                    nodes[node].neighbors.append(nodes[neighbor])
                    if neighbor not in visited :
                        q.append(neighbor)
                    visited.add(neighbor) # visited is needed just to make sure we don't go over anything twice
            
        fill_map(node)
        bfs(node)

        return nodes[node]
