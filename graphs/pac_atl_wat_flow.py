class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        # CUR, L, R, U, D
        directions = ((-1,0), (1,0), (0,1), (0,-1))
        # If we touch pac or atl

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

          def pac_check(i, j) :
            i_case = True if i == 0 else False
            j_case = True if j == 0 else False

            # it doesn't matter if the i or the j is touching bc we will add the start point anyways
            return i_case or j_case

        def atl_check(i, j) :
            i_case = True if i == len(grid) - 1 else False
            j_case = True if j == len(grid[i]) - 1 else False

            return i_case or j_case

        # Starting backwards is a good idea. 
        def dfs(i, j) :
            stack = deque()
            stack.append([i, j])
            # if pac and atl_check then True 
            pac, atl = False, False
            while stack :
                i, j = stack.pop()
                visited.append((i, j))
                if pac_check(i, j) and atl_check(i, j) : 
                    return True

                for direction in directions : 
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    next_val = grid[next_i][next_j]
                    # Do not continue on visited grids            
                    if (next_i, next_j) not in visited and next_i in range(len(grid)) and next_j in range(len(grid[i])) :
                        if next_val <= current : 
                            stack.append([next_i, next_j])
                            
            return False
        # Need to start from all edges
        
        for i in range(COLS) :
            # Top : [0][i] in range(cols)
            if (0, i) not in visited:
                dfs(0, i)
            # Bottom : [rows - 1][i] in range(cols) 
            if (rows - 1, i) not in visited:
                dfs(rows - 1, i)
            
        for i in range(ROWS) :
            # Left : [i][0] in range(rows)
            if (i, 0) not in visited:
                dfs(i, 0)
            # Right : [cols - 1][i] in range(rows)
            if (cols - 1, i) not in visited:
                dfs(cols - 1, i)

        return result

