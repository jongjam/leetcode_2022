class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        # space = O(n)
        # RT = O(2n) = O(n)
        # Using the sets for pac and alt will lead to at worse case performing DFS on every grid member two times
        ROWS = len(grid)
        COLS = len(grid[0])
        pac, atl = set(), set()

        # Check for current row or current column out of bounds
        def out_of_bounds(r, c) :
            row_oob = True if r < 0 or r >= ROWS else False 
            col_oob = True if c < 0 or c >= COLS else False
                
            return row_oob or col_oob

        def dfs(r, c, visit, prevHeight) :
            if out_of_bounds(r, c) or ((r,c) in visit) or grid[r][c] < prevHeight: 
                # if current is smaller 
                return                
            visit.add((r, c))
            #R
            dfs(r + 1, c, visit, grid[r][c])
            #L
            dfs(r - 1, c, visit, grid[r][c])
            #U
            dfs(r, c + 1, visit, grid[r][c])
            #D
            dfs(r, c - 1, visit, grid[r][c])

        # Iterating along all sides
        # Top and Bottom
        # Because we are starting at the ends... by default every eddge will work for either the pacific or atl
        # The bottom left and top right corner will be spotted in both adn will work
        # 6 will work because if we start in the cols we look at 5 and then look up
        # then it will be found in atl

        # Same will happen with rows eventually it will start at 6 and then from the pac set trickle down to 5

        for c in range(COLS) :
            # Top row
            dfs(0, c, pac, 0)
            # Bottom row
            dfs(ROWS - 1, c, atl, 0)
        # Left and Right 
        for r in range(ROWS) :
            # Left col
            dfs(r, 0, pac, 0)
            # Right col
            dfs(r, COLS - 1, atl, 0)

        for i in range(ROWS) :
            for j in range(COLS) :
                if (i, j) in atl and (i, j) in pac :
                    result.append([i, j])

        # 
        return result       
