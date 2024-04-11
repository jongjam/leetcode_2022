class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adj list
        # map with keys as courses and a list of prereqs
        adj_list = dict() 

        # Start doing DFS from 0 to n - 1

        # Making adjacency list
        adj_list = {i:set() for i in range(numCourses)}
        for crs, prereq in prerequisites :
            adj_list[crs].add(prereq)
        print(adj_list)
        visited = set()
        def dfs(crs, stack) :
            if crs in visited :
                if crs in stack :
                    return True # Cycle spotted bc this course is being processed as a prereq elsewhere

                # not being processed anywhere but just visited, bubbling up same result
                return False
            visited.add(crs) # currently processing
            stack.append(crs)

            # Going to process prereqs/neighbors now as well
            for i in adj_list[crs]:
                if dfs(i, stack) : # if cycle in prereqs return this
                    return True # bubbling up the result 
            
            stack.pop()
            return False #no cycle 

        for crs in range(numCourses) :
            if dfs(crs, deque()) :
                return False
        return True            

            



        
