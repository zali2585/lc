class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        graph = defaultdict(list)
        heap = [(0, k)]
        visited = set()

        for u, v, t in times:
            graph[u].append((v, t))
        while heap:
            curr_path, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            answer = curr_path
            for neighbor, weight in graph[curr_node]:
                node_p = curr_path + weight
                heapq.heappush(heap, (node_p, neighbor))
        if len(visited) == n:
            return answer
        else:
            return -1
        



    










        # visited set to make sure we visited all nodes when popping from heap
        # after heap is empty, can do for i in range(i to n) if i not in visited, return -1 bc that means disconnected node not visited even after all edges explored 
        # min heap with (weight up to that node, node)
        # time complexity: O(E * log V^2) (for every edge vertices can be added twice) but move square to front bc of rules of log --> constant so O(E * logV)
        # k node starts with path = 0
    