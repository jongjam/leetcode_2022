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
            print(a)
            return a
        
        # LRUD
        directions = ((-1,0), (1,0), (0,1), (0,-1))
        # minute calculations are wrong and likely need some kind of dfs 
        # haave to find the deepest orange from the rotten orange origin 

        # need to find the max distance between the furthest fresh orange from the first rotten one
        minutes = [0]
        
        def bfs(i, j) :
            q = deque()
            q.append((i,j))

            while q:
                x, y = q.popleft()
                for direction in directions :
                    next_x = x + direction[0]
                    next_y = y + direction[1]

                    if in_bounds(next_x, next_y) and grid[next_x][next_y] == 1 :
                        grid[next_x][next_y] = 2 
                        print(grid[next_x][next_y])
                        minutes[0] = max(minutes[0], abs(next_x - i) + abs(next_y - j))
                        q.append((next_x, next_y))

        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                if grid[i][j] == 2 :
                    bfs(i, j)
        
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                if grid[i][j] == 1 :
                    return -1

        return minutes[0]
