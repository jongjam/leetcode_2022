class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adj list
        # map with keys as courses and a list of prereqs
        adj_list = dict() 

        # Start doing DFS from 0 to n - 1

        # Making adjacency list
        for i in range(len(prerequisites)) :
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]
            
            if course not in adj_list : 
                adj_list[course] = set()
            # I'm assuming there won't be duplicates
            adj_list[course].add(prereq)

        # topological sort

        # detecing cycles
        stack = deque()
        # Starting
        stack.append(0)

        # Neetcode approach :
        # Starting from 0, do dfs until an course with empty set in the map is found
        # Remove this course as a prerequisite from 
        # if all sets empty then return true

        print(adj_list)
        for course in adj_list :
            for prereq in adj_list[course] :
                # Cycle detection
                if prereq in adj_list and course in adj_list[prereq] :
                    return False

        return True



        
