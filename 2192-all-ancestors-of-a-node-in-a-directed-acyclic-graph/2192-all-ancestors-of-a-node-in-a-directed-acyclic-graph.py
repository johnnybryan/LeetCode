class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = dict()
        
        for parent, child in edges:
            graph[child] = graph.get(child, []) + [parent]
        
        answer = [[] for i in range(n)]
        
        for parent in graph:
            seen = set()
            paths = [parent]
            while len(paths) > 0:
                current = paths.pop()
                for child in graph.get(current, []):
                    if child not in seen:
                        seen.add(child)
                        paths.append(child)
            answer[parent] = sorted(seen)
        
        return answer
                        
        