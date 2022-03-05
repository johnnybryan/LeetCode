"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # BFS
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        map, visited, queue = dict(), set(), collections.deque([node])
        while queue:
            n = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n not in map:
                map[n] = Node(n.val)
            for neighbor in n.neighbors:
                if neighbor not in map:
                    map[neighbor] = Node(neighbor.val)
                map[n].neighbors.append(map[neighbor])
                queue.append(neighbor)
        return map[node]