class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        path = set()
        # memory of "safe" classes, if u already saw a class in a path that had no cycle, then that means it wont ever have a cycle after so it saves recursive work
        visited = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True
            
            path.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            path.remove(course)
            visited.add(course)
            return True
          
        # in case theres disjointedness between courses like 
        # 0 - 1
        # 2 - 3 - 2 
        # if u only called in loop, you would never even access 2 and see loop there

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True








        