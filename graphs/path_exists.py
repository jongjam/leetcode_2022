class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # given list of edges
        # there are cycles but no cycles pointing to oneself.
        # finding a path from source to destination I can use either bfs or dfs
        if source == destination :
            return True
        adj_list = {i:[] for i in range(n)}
        for src,dest in edges :
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        

        # start the algorithm starting at source 
        stack = deque()
        stack.append(0)
        visited = set()
        # there is a cycle...

        while stack :
            current = stack.pop()
            visited.add(current)
            for neighbor in adj_list[current] :
                if neighbor == destination :
                    return True
                if neighbor not in visited :             
                    stack.append(neighbor)

        return False
        
        # the problem is bc adj list not supporting bidirectoional
