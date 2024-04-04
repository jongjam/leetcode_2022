class Solution:
    def scanFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        # If a set is empty then no problems    
        
                


        
