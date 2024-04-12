class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}
        for crs,prq in prerequisites :
            adj_list[crs].append(prq)
        
        result = []
        visited = set()
        cycle = set()
        def dfs(crs) :
            if crs in cycle : 
                return False
            if crs in visited :
                return True
            
            cycle.add(crs)
            for prq in adj_list[crs]:
                if not dfs(prq) :
                    return False
            cycle.remove(crs)
            visited.add(crs)
            result.append(crs)
            return True

        for crs in adj_list :
            if not dfs(crs):
                return []

        return result
        
    
