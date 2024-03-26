class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        # checking every cell and seeing if there is a path for them to max out or zero out
        # on the i axis AND the j axis.
        result = []
        # Every point can be checked but it will only continue the DFS if there is an adjacent point that is lower value. 
        # append only when lower
        # I guess don't really need a visited....

        # if grid[i][j] is at edge : then add to [i,j] to the result
        # DFS bc we want to touch the edge

          # CUR, L, R, U, D
        directions = ((-1,0), (1,0), (0,1), (0,-1))

        def pac_check(i, j) :
            i_case = True if i == 0 else False
            j_case = True if j == 0 else False

            # it doesn't matter if the i or the j is touching bc we will add the start point anyways
            return i_case or j_case

        def atl_check(i, j) :
            i_case = True if i == len(grid) - 1 else False
            j_case = True if j == len(grid[i]) - 1 else False

            return i_case or j_case
        
        # The iteration part is almost correct just need to figure out how to check the current node
        def dfs(i, j) :
            stack = deque()
            stack.append([i, j])
            pac = False
            atl = False
             

            # if pac and atl_check then True 
            while stack :
                i, j = stack.pop() 
                current = grid[i][j]
                
                pac = pac or pac_check(i, j)
                atl = atl or atl_check(i, j) # this might go wrong but I'm pretty sure it's best to check the current 

                for direction in directions : 
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    next_val = grid[next_i][next_j]
            
                    if next_i in range(len(grid)) and next_j in range(len(grid[i])) :
                        if next_val >= current : 
                            stack.append([next_i, next_j])
            return pac and atl
            
        # I think I might have an issue where the DFS is running too much
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                if dfs(i, j) :
                    # bounds check here or later will take some more thought
                    result.append([i, j])

        return result

