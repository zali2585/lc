from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)  
    
        if len(order) == numCourses:
            return order
        return []
"""
MAIN IDEA:
U CREATE A LIST WHERE AT INDEX OF PREREQ IS ALL COURSES THAT HAVE THAT CLASS AS PREREQ
EX: index 0 = [1, 3]; classes 1 and 3 have class 0 as a prereq
YOU HAVE ANOTHER LIST WHERE @ INDEX OF CLASS, YOU HAVE A COUNT OF HOW MANY PREREQS THAT CLASS HAS
THEN U CEATES A QUEUE AND ORDER LIST WHERE, WHILE QUEUE, YOU POP ITEM (QUEUE ONLY CONTAINS CLASSES WITH NO PREREQS) AND THEN ADD IT TO ORDER BC U KNOW UR NOT BREAKING ANY RULES BC IT HAS NO PREREQS. THEN FOR EACH COURSE IN THAT CURR COURSE' LIST (SO FOR EACH COURSE THAT HAS CURR COURSE AS PREREQ) U REDUCE PREREQ OR INDEGREE COUNT BY 1 (INDEGREE MEANS HOW MANY ARROWS POINT AT A THING OR IN THIS CASE HOW MANY PREREQS POINT AT A COURSE)
THEN, IF TAKING CURR COURSE MEANS U TOOK LAST PREREQ FOR ANY OTHER COURSE (IE ANY COURSE WITH CURR AS PREREQ INDEGREE BECOMES 0) U ADD TO QUEUE TO BE PROCESSED. 
AT VERY END, U CHECK IF ORDER LENGTH == NUM COURSES. IF NOT, THAT MEANS THERE WAS SOME CYCLE THAT MADE LENGTH TOO SHORT SO U RETURN EMPTY LIST
EX: 0 -> 1 AND 1 -> 0: BOTH INDEGREE[0] AND INDEGREE[1] == 1, SO NEITHER CAN BE ADDED TO QUEUE SO QUEUE STAYS EMPTY AND THUS, NOTHING IS EVER ADDED TO ORDER SO LEN(ORDER) = 0 < NUMCOURSES = 2.
"""