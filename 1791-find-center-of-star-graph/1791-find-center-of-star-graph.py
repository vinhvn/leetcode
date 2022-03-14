class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        maxEdges = -1
        maxNode = -1
        nodeFreq = defaultdict(int)
        for edge in edges:
            for node in edge:
                nodeFreq[node] += 1
                if nodeFreq[node] > maxEdges:
                    maxEdges = nodeFreq[node]
                    maxNode = node
        return maxNode
