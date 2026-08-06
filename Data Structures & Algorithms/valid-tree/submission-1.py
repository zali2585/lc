class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        # intialized in range n bc must have adjacency list for each node, not edges bc especially if graph is disconnected (so less edges than nodes, causes indexing error)
        graph = [[] for _ in range(n)]
        for node, child in edges:
            # populate both ways bc graph is undirected
            graph[node].append(child)
            graph[child].append(node)
        visited = set()
            
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True
        # len(visited) checks that nodes are all connected bc can only be same if there is a path to all nodes
        return dfs(0, -1) and len(visited) == n

"""
MAIN IDEA: CHECK TREE FOR DEFINITION OF WHAT MAKES A TREE: NO CYCLES AND CONNECTED
TRAVERSE NEIGHBORS OF EACH NODE TO CHECK IF THERES NO CYCLE (IE CHECK THAT U CAN'T REVERSE TO A PREVIOUSLY VISITED NODE OTHER THAN PARENT)
CHECK CONNECTION BY COMPARING SET OF VISITED NODES TO LEN OF EDGES
"""