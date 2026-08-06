class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) 
        parent = list(range(n+1))
        size = [1] * (n + 1)

        def find(node):
            # continues until finds root
            # if parent = [0, 1, 1, 2], node 1 points to itself, node 2 points to 1 and node 3 points to 3, making a chain 3 -> 2 -> 1 where 1 is root
            # finds root and stops loop when parent[1] == 1
            while node != parent[node]:
                parent[node] = find(parent[node])
                node = parent[node]
            return node
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            
            # checks if theyre in same group ie share same root
            if root_a == root_b:
                return False
            # if a tree is smaller than b tree, swaps so that next code of setting parent can be universally true and optimal 
            # optimal in the sense that u dont add a long tree to the end of a super short tree, increasing depth  
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            
            parent[root_b] = root_a
            # size of root a is now root a + root b
            size[root_a] += size[root_b]
            return True
        
        
        for a, b in edges:
            # returns true when a, b in same group
            if not union(a, b):
                return [a, b]


         