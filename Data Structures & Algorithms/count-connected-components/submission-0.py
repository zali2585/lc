class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()

        def dfs(node):
            seen.add(node)

            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        components = 0

        for node in range(n):
            if node not in seen:
                dfs(node)
                components += 1


        return components

"""
MAIN IDEA : create adjacency map of node to neighbors
for each node, call dfs on node if its not yet seen before. if its not seen before, it must be in a seperate component bc all nodes connected and previously seen are put into seen set. for each neighbor, if node is not in seen, call dfs on it and increment components count.
dfs basically traverses whole tree if its new only 
"""         