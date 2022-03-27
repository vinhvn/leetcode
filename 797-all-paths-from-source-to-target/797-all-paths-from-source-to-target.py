class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        output = []

        def dfs(node, path):
            copy = list(path)
            copy.append(node)
            if node == n - 1:
                return output.append(copy)
            for v in graph[node]:
                dfs(v, copy)
        
        dfs(0, [])
        return output
