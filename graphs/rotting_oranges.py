class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time is counted by level of traversal and this seems like BFS as we can see in the diagrams
        # Basically traverse over the grid and if we have a 2
        # Check if any adjacent cells are 1 
        # If so add them to queue and change them to 2, marking them as visited
        # figure out how to increase time only per level

        minutes = 0

        # LRUD
        directions = ((-1,0), (1,0), (0,1), (0,-1))

        def bfs(i, j) :
            q = deque()
            q.append((i,j))

            while q:
                i, j = q.popleft()
                
                for direction in directions :
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    if grid[next_i][next_j] == '1' :
                        grid[next_i][next_j] = '2'
                        q.append((next_i, next_j))
            minutes += 1

        for i range(len(grid)) :
            for j in range(len(grid[i])) :
                if grid[i][j] == 2 :
                    bfs()
        
        for i range(len(grid)) :
            for j in range(len(grid[i])) :
                if grid[i][j] == 1 :
                    return -1

        return minutes
