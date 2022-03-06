class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = [[] for _ in range(n)]
        in_degrees = [0] * n
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            in_degrees[crs] += 1
        stack = [ crs for crs in range(n) if in_degrees[crs] == 0]
        while stack:
            pre = stack.pop()
            for crs in graph[pre]:
                in_degrees[crs] -= 1
                if in_degrees[crs] == 0:
                    stack.append(crs)
        return not any(in_degrees)
        