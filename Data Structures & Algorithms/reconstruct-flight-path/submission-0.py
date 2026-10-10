class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # builds graph of directed edges to represent flights
        from collections import defaultdict
        res = []
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        for key in graph:
            graph[key].sort(reverse=True)
        # DFS to find path that terminates (ie has no outgoing flights, then backtrack and see if theres diff path)
        def dfs(src):
            while graph[src]:
                n = graph[src].pop()
                dfs(n)
            res.append(src)
        dfs("JFK")
        res.reverse()
        return res
                


        
        