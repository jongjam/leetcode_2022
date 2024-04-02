class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time is counted by level of traversal and this seems like BFS as we can see in the diagrams
        # Basically traverse over the grid and if we have a 2
        # Check if any adjacent cells are 1 
        # If so add them to queue and change them to 2, marking them as visited
        # figure out how to increase time only per level

        # Minutes is really the x + y distance from the last level of oranges
        
        ROWS = len(grid)
        COLS = len(grid[0])

        def in_bounds(x, y) :
            a = x in range(ROWS) and y in range(COLS)
            return a
        
        # LRUD
        directions = ((-1,0), (1,0), (0,1), (0,-1))
        # minute calculations are wrong and likely need some kind of dfs 
        # haave to find the deepest orange from the rotten orange origin 
        # SO THEY USED O(N^2) SPACE SO THERE IS SOMETHING ELSE TO TRACK THE LCOATIONS AND DISTANCES
        # need to find the max distance between the furthest fresh orange from the first rotten one
        minutes = [0]
        fresh = 0
        
        q = deque()
        
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2 :
                    q.append((i, j))

        while fresh > 0 and q:
            for i in range(len(q)) :
                x, y = q.popleft()
                for direction in directions :
                    next_x = x + direction[0]
                    next_y = y + direction[1]

                    if in_bounds(next_x, next_y) and grid[next_x][next_y] == 1 :
                        fresh -= 1
                        grid[next_x][next_y] = 2 
                        q.append((next_x, next_y))
            minutes[0] += 1 # too many things are getting appended here?    
                
        return minutes[0] if fresh == 0 else -1
