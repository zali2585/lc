class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) 
        parent = list(range(n+1))
        size = [1] * (n + 1)

        def find(node):
            # continues until finds root
            # if parent = [0, 1, 1, 2], node 1 points to itself, node 2 points to 1 and node 3 points to 3, making a chain 3 -> 2 -> 1 where 1 is root
            # finds root and stops loop when parent[1] == 1
            # if parent[node] != node, calls find on parent[node]
            # EX: if ur at 3, and 3 != parent[3] which is 2, then u call on parent[3] so find(2) then 2 != parent[2] which is 1 so u call find(parent[2]) so find(1) and then u finally have 1 = parent[1] which is 1
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
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
            # returns false when a and b are already connected and then not of that is true so enters this if bc a, b results in creation of cycle
            if not union(a, b):
                return [a, b]


         